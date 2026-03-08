from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import psutil
import logging

app = Flask(__name__)
CORS(app)

# WebSocket inicializálása
socketio = SocketIO(app, cors_allowed_origins="*")

# --- KONFIGURÁCIÓ ÉS VÁLTOZÓK ---
# Megtisztítva a duplikációktól és a szintaktikai hibáktól
AGENTS_ORDER = ["PythonAgent", "JavaAgent"] 
current_turn_index = 0
conversation_history = []
current_topic = "Várakozás a felhasználó kérdésére..."
is_active = False

print("🛑 A TANÁCS SZERVER ELINDULT. Várakozás a moderátorra...")

# --- WEBSOCKET HÁTTÉRFOLYAMAT (AZ ÚJ MOTOR) ---
def hatter_radar():
    """Végtelenített ciklus, ami másodpercenként tolja az adatot a csövön."""
    while True:
        socketio.sleep(1)
        adat = {
            "is_active": is_active,
            "current_turn": AGENTS_ORDER[current_turn_index],
            "current_topic": current_topic,
            "cpu_load": psutil.cpu_percent(interval=0.1),
            "ram_load": psutil.virtual_memory().percent
        }
        socketio.emit('rendszer_allapot', adat)

@socketio.on('connect')
def kliens_csatlakozott():
    # Először a titkos "X-Forwarded-For" zsebet nézzük meg, ha nincs, marad az alap IP
    valodi_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Kinyerjük az eszköz és a nyelv adatait
    user_agent = request.headers.get('User-Agent', 'Ismeretlen eszköz')
    language = request.headers.get('Accept-Language', 'Ismeretlen nyelv')
    
    # A jelentés kiírása
    print(f"\n[+] --- ÚJ LÁTOGATÓ A RADARON ---")
    print(f"[+] Valódi IP: {valodi_ip}")
    print(f"[+] Eszköz:    {user_agent}")
    print(f"[+] Nyelv:     {language}")
    print(f"[+] ---------------------------------------------\n")
    
    socketio.start_background_task(target=hatter_radar)


# --- REST API VÉGPONTOK  ---

@app.route('/status', methods=['GET'])
def get_status():
    # Összevontam a két return-t egybe, hogy a te logikád és a hardver adatok is kimenjenek
    if is_active:
        active_agent = AGENTS_ORDER[current_turn_index]
    else:
        active_agent = None
        
    return jsonify({
        "is_active": is_active,
        "current_turn": active_agent,
        "topic": current_topic,
        "history": conversation_history,
        "cpu_load": psutil.cpu_percent(interval=0.1),
        "ram_load": psutil.virtual_memory().percent
    })

@app.route('/speak', methods=['POST'])
def post_message():
    global current_turn_index
    data = request.json
    sender = data.get("sender")
    message = data.get("message")
    
    conversation_history.append({"sender": sender, "message": message})
    print(f"🗣️  {sender}: {message}")
    
    # Következő kör
    current_turn_index = (current_turn_index + 1) % len(AGENTS_ORDER)
    return jsonify({"status": "accepted"})

@app.route('/api/new_topic', methods=['POST'])
def new_topic():
    global current_topic, conversation_history, current_turn_index, is_active
    
    data = request.json
    new_question = data.get("topic")
    
    # Reset
    conversation_history = []
    current_turn_index = 0
    current_topic = new_question
    is_active = True 
    
    print(f"\n📢 ÚJ FELHASZNÁLÓI KÉRDÉS: {current_topic}")
    print("------------------------------------------------------")
    
    return jsonify({"status": "Topic updated", "topic": current_topic})


if __name__ == '__main__':
    # LECSERÉLVE: Mostantól a SocketIO indítja a szervert, nem a sima app.run
    socketio.run(app,host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)