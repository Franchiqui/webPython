import socket

from traductor import traductor

host, port = '127.0.0.1', 8888
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, port))
serversocket.listen(1)
print('Servidor en el puerto', port)

def process_request(request):
    parts = request.split()
    method = parts[0]
    path = parts[1]

    if path == '/':
        myfile = 'index.html'
    else:
        myfile = path.lstrip('/')

    try:
        if method == 'GET' and path == '/':
            header = 'HTTP/1.1 200 OK\n\n'
            response = '<html><body>Hello, world!</body></html>'.encode('utf-8')
        elif method == 'POST' and path == '/traductor':
            request_data = request.split('\r\n\r\n')[1]
            translate_text, target_lang = request_data.split('&')
            translate_text = translate_text.split('=')[1]
            target_lang = target_lang.split('=')[1]
            traduccion = traductor(translate_text, target_lang)
            response = f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n{traduccion}'.encode('utf-8')
        else:
            response = 'HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\nError 404: Recurso no encontrado'.encode('utf-8')

        return response
    except Exception as e:
        return f'HTTP/1.1 500 Internal Server Error\nContent-Type: text/plain\n\n{str(e)}'.encode('utf-8')

while True:
    connection, address = serversocket.accept()
    request = connection.recv(1024).decode('utf-8')
    print('Cliente solicitó', request)

    response = process_request(request)
    connection.send(response)
    connection.close()