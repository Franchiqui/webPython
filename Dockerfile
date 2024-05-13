# Usa la imagen oficial de Python
FROM python:3.11-slim

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install\
    libgl1\
    libgl1-mesa-glx \
    libglib2.0-0 -y && \
    rm -rf /var/lib/apt/lists/*

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo Python al contenedor
COPY server.py /app/server.py

# Copiar el archivo de requerimientos
COPY requirements.txt .

RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"

RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar todo el contenido del directorio actual al directorio de trabajo del contenedor
COPY . .

# Instala las dependencias del servidor (en este caso, solo el módulo 'socket')
RUN pip install socket

# Expone el puerto 8888 para que el servidor sea accesible desde fuera del contenedor
EXPOSE 8888

# Ejecuta el script Python cuando se inicie el contenedor
CMD ["python", "server.py"]
