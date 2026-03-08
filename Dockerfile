# 1. Alap operációs rendszer és Python verzió (egy letisztult, könnyűsúlyú Linux)
FROM python:3.12-slim

# 2. Létrehozunk egy mappát a konténeren belül, és belemegyünk
WORKDIR /app

# 3. Telepítjük a szükséges csomagokat (pont, ahogy te is csináltad a terminálban)
RUN pip install --no-cache-dir flask flask-cors flask-socketio psutil

# 4. Bemásoljuk a saját kódunkat a te gépedről a konténerbe
COPY conference_room.py .

# 5. Kinyitjuk az 5000-es portot a külvilág felé, hogy a React lássa
EXPOSE 5000

# 6. A parancs, ami elindul, amikor a konténer életre kel
CMD ["python", "-u", "conference_room.py"]