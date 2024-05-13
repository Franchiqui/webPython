# Usa la imagen oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"


# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/requirements.txt

# Instala los módulos especificados en requirements.txt
RUN pip install -r requirements.txt

# Copia el archivo Python al contenedor
COPY server.py /app/server.py

# Expone el puerto 8888 para que el servidor sea accesible desde fuera del contenedor
EXPOSE 8888

# Ejecuta el script Python cuando se inicie el contenedor
CMD ["python", "/app/server.py"]
