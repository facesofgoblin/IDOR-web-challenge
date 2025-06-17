# Gunakan image Python
FROM python:3.12-slim

# Set direktori kerja
WORKDIR /app

# Salin requirements & install dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua kode ke container
COPY . .
COPY flag.txt /app/flag.txt  

# Jalankan migrate, seed, lalu start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py shell < seed.py && rm seed.py && python manage.py runserver 0.0.0.0:8000"]
