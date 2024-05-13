# Usa la imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo Python al contenedor
COPY server.py /app/server.py


# Instala las dependencias del servidor (en este caso, solo el módulo 'socket')

RUN pip install deepl

# Expone el puerto 8888 para que el servidor sea accesible desde fuera del contenedor
EXPOSE 8888

# Ejecuta el script Python cuando se inicie el contenedor
CMD ["python", "server.py"]
