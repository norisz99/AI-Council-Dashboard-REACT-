# 🎛️ Project: Norisz Corp AI Vezérlőpult

![Python](https://img.shields.io/badge/Python-3.x-blue) ![React](https://img.shields.io/badge/React-Vite-61DAFB?logo=react) ![Socket.IO](https://img.shields.io/badge/Socket.IO-WebSocket-black?logo=socket.io) ![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## 📌 Áttekintés (Overview)

Ez a projekt egy valós idejű, interaktív **AI Vezérlőpult**, amely egy Python backendből (adatforrás) és egy modern React frontendből (megjelenítő) áll. A rendszer Socket.IO segítségével kommunikál, és dupla hálózati alagutakon (Ngrok & Cloudflare) keresztül biztosítja, hogy a lokális hálózaton futó szerverek és a "Taktikai Tojmó" vezérlőközpont publikusan, bármilyen okoseszközről elérhetőek legyenek.

## 🛠️ Funkciók

* 📡 **Valós idejű telemetria:** Élő CPU és RAM terheltségi adatok streamelése a szerverről a kliensre.
* ⚡ **WebSocket Kommunikáció:** Késleltetés nélküli, kétirányú adatkapcsolat a háttér és a frontend között.
* 🌍 **Dual-Tunnel Exfiltration:** Lokális hálózati korlátozások megkerülése (Ngrok a backendnek, Cloudflare a frontendnek).
* 🤖 **AI Tanács Integráció:** (Fejlesztés alatt) Mesterséges intelligencia ügynökök folyamatos adatfeldolgozása és válaszadása.

## ⚙️ Technikai Részletek

* **Frontend:** React (Vite környezetben felépítve)
* **Backend:** Python 3.x
* **Hálózati Könyvtárak:** `Flask`, `Flask-SocketIO`, `socket.io-client`
* **Protokoll:** WebSocket (WSS) / HTTP

## ⚖️ Jogi Nyilatkozat (Disclaimer)

A szoftver "ahogy van" (as is) kerül biztosításra, mindennemű garancia nélkül, legyen az kifejezett vagy vélelmezett, beleértve, de nem kizárólagosan az eladhatóságra, egy adott célra való alkalmasságra és a jogsértés hiányára vonatkozó garanciákat. A szerzők vagy a szerzői jogok birtokosai semmilyen körülmények között nem tehetők felelőssé semmilyen követelésért, kárért vagy egyéb felelősségért, akár szerződéses jogviszonyból, akár versenyjogból vagy másból eredően, amely a szoftverből, annak használatából, vagy a szoftverrel kapcsolatos egyéb tranzakciókból fakad.