import socket
from app.traductor import traductor_func
from app.video import video_func
from pydantic import BaseModel


class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: str


def handle_client(client_socket):
    while True:
        # Recibir datos del cliente
        request = client_socket.recv(1024).decode('utf-8')

        # Procesar la solicitud y generar una respuesta
        response = process_request(request)

        # Enviar la respuesta al cliente
        client_socket.send(response.encode('utf-8'))

        # Cerrar la conexión si es necesario
        # Aquí debes implementar la lógica para decidir cuándo cerrar la conexión

    # Cerrar el socket del cliente cuando termines de manejar la conexión
    client_socket.close()


def process_request(request):
    parts = request.split()
    method = parts[0]
    path = parts[1]

    if method == 'GET' and path == '/':
        return 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\nHola, Pythonianos'

    elif method == 'GET' and path.startswith('/libros'):
        if len(parts) > 2:
            libro_id = parts[2].lstrip('/')
            return f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\nMostrando libro {libro_id}'
        else:
            return 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\nLista de libros'

    elif method == 'POST' and path == '/libros':
        data = path.split('\r\n\r\n')[1]
        data_parts = data.split('&')
        libro_data = {}
        for part in data_parts:
            key, value = part.split('=')
            libro_data[key] = value
        libro = Libro(**libro_data)
        return f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\nLibro {libro.titulo} insertado'

    elif method == 'PUT' and path.startswith('/libros'):
        libro_id = path.split('/')[-1]
        data = path.split('\r\n\r\n')[1]
        data_parts = data.split('&')
        libro_data = {}
        for part in data_parts:
            key, value = part.split('=')
            libro_data[key] = value
        libro = Libro(**libro_data)
        return f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\nLibro {libro.titulo} actualizado'

    elif method == 'DELETE' and path.startswith('/libros'):
        libro_id = path.split('/')[-1]
        return f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\nLibro {libro_id} eliminado'

    elif method == 'GET' and path == '/video':
        return video_func()

    elif method == 'POST' and path == '/traductor':
        request_data = path.split('\r\n\r\n')[1]
        translate_text, target_lang = request_data.split('&')
        translate_text = translate_text.split('=')[1]
        target_lang = target_lang.split('=')[1]
        traduccion = traductor_func(translate_text, target_lang)
        return f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n{traduccion}'

    else:
        return 'HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\nError 404: Recurso no encontrado'


def main():
    # Configurar el servidor
    host = '127.0.0.1'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f'Servidor escuchando en {host}:{port}')

    while True:
        # Esperar una conexión entrante
        client_socket, addr = server_socket.accept()
        print(f'Conexión entrante desde {addr}')

        # Manejar la conexión en un hilo separado
        handle_client(client_socket)


if __name__ == "__main__":
    main()
