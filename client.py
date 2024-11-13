import socket

client = socket.socket()
server_ip = "3.111.29.223"  
server_port = 1234

client.connect((server_ip, server_port))
print(f"connection is established from {server_ip}:{server_port}")

while True:
	message = input("Enter your message: ")
	client.send(message.encode())

	if message.lower() == "bye":
		print("connection closing..")
		break

	data = client.recv(1024).decode()
	print("Received from server:", data)
		 
client.close()
print("ENDED!")

