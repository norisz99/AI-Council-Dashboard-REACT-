import { useState, useEffect } from 'react';
import { io } from 'socket.io-client';
import './App.css';
import ServerCard from './ServerCard';

const socket = io('https://apathetic-unsupplanted-jerrica.ngrok-free.dev/', {
  extraHeaders: {
    "ngrok-skip-browser-warning": "true"
  }
});;

function App() {
  const [pythonData, setPythonData] = useState(null);
  const [hiba, setHiba] = useState(null);

  useEffect(() => {
  socket.on('connect', () => {
      setHiba(null);
      console.log("🟢 Rácsatlakoztunk a Python WebSocketre!");
    });

    // Ha leáll a Python szerver, azonnal észrevesszük
    socket.on('disconnect', () => {
      setHiba("🔴 Megszakadt a kapcsolat a Python szerverrel!");
    });

    // 3. A VARÁZSLAT: Itt figyeljük a 'rendszer_allapot' csatornát.
    // Amint a Python lő egy új adatot, ez azonnal lefut és frissíti a kártyát!
    socket.on('rendszer_allapot', (adat) => {
      setPythonData(adat);
    });

    // Takarítás, ha bezárnád a böngészőt
    return () => {
      socket.off('connect');
      socket.off('disconnect');
      socket.off('rendszer_allapot');
    };
  }, []);

  return (
    <div className="app-container">
      <h1>Norisz Corp - Vezérlőpult</h1>
      <p>Élő adatok a Python szervertől (Auto-frissítés aktív):</p>
      
      <div style={{ display: 'flex', justifyContent: 'center', marginTop: '40px' }}>
        
        {hiba ? (
          <p style={{ color: 'red' }}>{hiba}</p>
        ) : !pythonData ? (
          <p>⏳ Kapcsolódás a Pythonhoz...</p>
        ) : (
          <ServerCard 
            name="Python Tanácsterem" 
            status={pythonData.is_active ? "Online" : "Várakozik"} 
            load={pythonData.cpu_load} 
            ram_load={pythonData.ram_load} // <--- ITT ADJUK ÁT AZ ÚJ RAM ADATOT A KÁRTYÁNAK
          />
        )}

      </div>
    </div>
  );
}

export default App;