# Imagen base ligera con Python 3.11
FROM python:3.11-slim

# Evita archivos .pyc y salida bufferizada
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto (sin el .env, gracias al .dockerignore)
COPY . .

# Expone el puerto en el que corre Flask
EXPOSE 8000

# Comando de inicio
CMD ["python", "app.py"]
