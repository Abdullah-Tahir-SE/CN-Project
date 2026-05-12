# 🌐 NET-PRO Dashboard — TCP/UDP Socket Communication

A **Computer Networks** semester project featuring a professional **Flask-based web dashboard** for real-time TCP and UDP socket communication. Send custom messages to servers and visualize the entire request/response lifecycle through an interactive terminal console.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![Sockets](https://img.shields.io/badge/Protocol-TCP%20%2F%20UDP-teal)

---

## 📸 Features

| Feature | Description |
|---------|-------------|
| 🔁 **TCP Client-Server** | Reliable, connection-oriented communication with 3-way handshake |
| ⚡ **UDP Client-Server** | Fast, connectionless datagram transmission |
| 🖥️ **Web Dashboard** | Modern, responsive UI to trigger and monitor socket operations |
| 📝 **Custom Payloads** | Send your own messages through the input field |
| 🖳 **Live Console Logs** | Dark-themed terminal showing timestamped network activity |
| 🎨 **Professional UI** | Glassmorphism cards, hover animations, and clean design |

---

## 🏗️ Project Structure

```
CN-Project/
├── app.py              # Flask web server + TCP/UDP client logic
├── tcp_server.py        # Standalone TCP server (port 12346)
├── udp_server.py        # Standalone UDP server (port 54321)
├── templates/
│   └── index.html       # Web dashboard frontend
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

```
┌──────────────┐       HTTP        ┌──────────────┐      TCP/UDP      ┌──────────────┐
│   Browser    │  ──────────────►  │  Flask App   │  ──────────────►  │   TCP/UDP    │
│  (Frontend)  │  ◄──────────────  │  (app.py)    │  ◄──────────────  │   Server     │
└──────────────┘     JSON Resp     └──────────────┘     Response      └──────────────┘
```

1. **User** enters a message in the web dashboard and clicks TCP or UDP button.
2. **Flask** (`app.py`) receives the HTTP request and opens a raw socket connection.
3. **TCP/UDP Server** receives the packet, logs it, and sends back a response.
4. **Flask** returns the server response as JSON to the frontend.
5. **Dashboard** displays the result and logs the activity in the terminal console.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed
- **Flask** library

### Installation

```bash
# Clone the repository
git clone https://github.com/Abdullah-Tahir-SE/CN-Project.git
cd CN-Project

# Install Flask
pip install flask
```

### Running the Project

You need **3 terminals** running simultaneously:

**Terminal 1 — Start TCP Server:**
```bash
python tcp_server.py
# Output: TCP Server active on Port 12346 ...
```

**Terminal 2 — Start UDP Server:**
```bash
python udp_server.py
# Output: UDP Server active on Port 54321 ...
```

**Terminal 3 — Start Flask Web App:**
```bash
python app.py
# Output: Flask Server started on http://127.0.0.1:5000
```

Now open your browser and go to **http://127.0.0.1:5000** 🎉

---

## 🔧 Configuration

All server settings are defined in `app.py`:

```python
SERVER_IP = '127.0.0.1'
TCP_PORT  = 12346
UDP_PORT  = 54321
```

---

## 🧠 Concepts Demonstrated

- **Socket Programming** — `socket.AF_INET`, `SOCK_STREAM` (TCP), `SOCK_DGRAM` (UDP)
- **Client-Server Architecture** — Separate server processes communicating via sockets
- **TCP vs UDP** — Comparing reliable vs fast protocols side by side
- **Flask Web Framework** — REST API endpoints serving JSON responses
- **Asynchronous Frontend** — Fetch API for non-blocking HTTP calls

---

## 👨‍💻 Developed By

**Abdullah Tahir** — Computer Networks Project, Semester 4

---

## ScreenShots
<img width="1918" height="1010" alt="Screenshot 2026-05-01 012353" src="https://github.com/user-attachments/assets/5620d0f3-d1ae-497d-84c7-1157507d5efb" />
<img width="1919" height="1005" alt="Screenshot 2026-05-01 012429" src="https://github.com/user-attachments/assets/318ffdfb-8431-4970-98bf-5bd6be64e8e9" />
<img width="1919" height="1007" alt="Screenshot 2026-05-01 012446" src="https://github.com/user-attachments/assets/f01bd5db-3645-4d2d-82fc-edd09b968cec" />



