# Usa la imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en /app
WORKDIR /server

RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"


RUN pip install deepl

# Copia el archivo Python al contenedor
COPY server.py /app/server.py

# Expone el puerto 8888 para que el servidor sea accesible desde fuera del contenedor
EXPOSE 8888

# Ejecuta el script Python cuando se inicie el contenedor
CMD ["python", "server.py"]
