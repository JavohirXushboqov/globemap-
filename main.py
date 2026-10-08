from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8080

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print("GLOBEMAP ishga tushdi!")
print(f"Brauzerda oching: http://127.0.0.1:{PORT}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer to'xtatildi.")
    server.server_close()
