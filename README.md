# 🎛️ Project: Norisz Corp AI Vezérlőpult

`Python 3.12` `React Vite` `Docker` `Kubernetes` `Socket.IO` `Status: Active`

🌐 **Élő Rendszer Elérése:** [Kattints ide a Vezérlőpulthoz](https://ide-jon-a-cloudflare-linked.trycloudflare.com)
*(Megjegyzés: Mivel a rendszer lokális fejlesztés alatt áll, a Cloudflare alagút linkje minden indításnál változhat. Kérd a legfrissebb linket az üzemeltetőtől!)*

## 📌 Áttekintés (Overview)

Ez a projekt egy valós idejű, interaktív **AI Vezérlőpult**, amely egy robusztus, mikroszolgáltatás (Microservices) architektúrára épül. A rendszer "agya" egy elszigetelt Kubernetes konténerben futó Python backend, míg a megjelenítésért egy modern React frontend felel. A két oldal Socket.IO segítségével kommunikál, és dupla hálózati alagutakon (Ngrok & Cloudflare) keresztül biztosítja, hogy a lokális szerverek és a vezérlőközpont publikusan, bármilyen okoseszközről elérhetőek legyenek.

## 🛠️ Funkciók

* 📦 **Konténerizált Backend (K8s):** A Python motor egy erőforrás-optimalizált Docker konténerben fut, teljes elszigeteltségben, helyi Kubernetes orchestrációval.
* 🛰️ **Valós idejű telemetria:** Élő CPU és RAM terheltségi adatok streamelése a szerverről a kliensre, minimális késleltetéssel.
* ⚡ **WebSocket Kommunikáció:** Kétirányú, folyamatos adatkapcsolat a háttér és a frontend között.
* 🌍 **Dual-Tunnel Exfiltration:** Lokális hálózati korlátozások megkerülése (Ngrok a backendnek, Cloudflare a frontendnek).
* 🤖 **AI Tanács Integráció:** *(Fejlesztés alatt)* Mesterséges intelligencia ügynökök folyamatos adatfeldolgozása és válaszadása.

## ⚙️ Technikai Részletek

A rendszer teljesen szétválasztott (Decoupled) környezetben működik:

* **Frontend:** React (Vite környezetben felépítve)
* **Backend:** Python 3.12
* **Infrastruktúra & DevOps:** Docker Desktop, lokális Kubernetes (K8s)
* **Hálózati Könyvtárak:** `Flask`, `Flask-SocketIO`, `socket.io-client`
* **Kulcsfájlok a repóban:** * `Dockerfile`: A backend konténer felépítésének receptje.
  * `backend.yaml`: A Kubernetes kottája (Deployment és LoadBalancer Service).

## ⚖️ Jogi Nyilatkozat (Disclaimer)

A szoftver fejlesztés alatt áll, "ahogy van" (as is) kerül biztosításra. A rendszer használata, valamint a hálózati portok és alagutak (Ngrok, Cloudflare) megnyitása saját felelősségre történik. A készítő semmilyen felelősséget nem vállal az esetleges adatvesztésért, hálózati sebezhetőségekért, vagy a szoftver használatából fakadó bármilyen kárért.