import socket

server = socket.socket()
server.bind( ("0.0.0.0", 1234) )
server.listen()

print("Server is waiting for a connection...")

conn, client_address = server.accept()
print("Connected to Client_IP:", client_address[0])

while True:
	data = conn.recv(1024).decode()
	if data.lower() == "bye":
		print("Client disconnected")
		break
	print("Received from client:", data)

	response = input("Responding to client: ")
	conn.send(response.encode())


conn.close()
server.close()
print("connection is CLOSED!")





