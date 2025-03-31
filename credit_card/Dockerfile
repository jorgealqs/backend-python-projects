# Usa la última versión estable de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Configura variables de entorno para mejorar el rendimiento
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependencias del sistema necesarias para algunas librerías
RUN apt-get update && apt-get install -y \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia solo el archivo de requisitos para aprovechar la caché de Docker
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del proyecto después de instalar las dependencias
COPY . /app/

# Expone el puerto del contenedor
EXPOSE ${PORT_DEFAULT}

# Comando por defecto para correr el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:${PORT_DEFAULT}"]