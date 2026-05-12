from flask import Flask, render_template, jsonify
import socket

app = Flask(__name__)

# --- CONFIGURATION ---
SERVER_IP = '127.0.0.1'
TCP_PORT = 12346
UDP_PORT = 54321

# 1. TCP Client Logic
def run_tcp_client():
    try:
        # Socket create karna (TCP)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(3) # 3 seconds timeout agar server na mile
        
        # Connect to server
        client.connect((SERVER_IP, TCP_PORT))
        
        # Message bhejna
        message = "Hello Server! TCP Request from Web."
        client.send(message.encode())
        
        # Response receive karna
        response = client.recv(1024).decode()
        client.close()
        return response
    except Exception as e:
        return f"TCP Error: {str(e)}"

# 2. UDP Client Logic
def run_udp_client():
    try:
        # Socket create karna (UDP)
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(3)
        
        # UDP mein connect nahi karte, direct sendto karte hain
        message = "Hi! UDP Packet from Web Dashboard."
        client.sendto(message.encode(), (SERVER_IP, UDP_PORT))
        
        # Response receive karna
        data, addr = client.recvfrom(1024)
        client.close()
        return data.decode()
    except Exception as e:
        return f"UDP Error: {str(e)}"

# --- ROUTES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-tcp')
def tcp_route():
    result = run_tcp_client()
    return jsonify({"message": result})

@app.route('/run-udp')
def udp_route():
    result = run_udp_client()
    return jsonify({"message": result})

if __name__ == '__main__':
    print("Flask Server started on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)