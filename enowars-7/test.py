import socket

def netcat(host, port): # Også legge til ,message
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect((host, port))
        print(f"Koblet til {host}:{port}")

        #client_socket.sendall(message.encode())
        
        response = client_socket.recv(4096)
        print(f"Respons:\n{response.decode()}")

    except ConnectionRefusedError:
        print("Nonono")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    target_ip = "10.0.13.37"
    target_port = 1337
    message_to_send = "{message}"

    netcat(target_ip, target_port)
    #netcat(target_ip, target_port, message_to_send)
