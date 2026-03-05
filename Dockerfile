#Базовый образ с Python
FROM python:3.11-slim

#Папка внутри контейнера
WORKDIR /app

#Копируем список библиотек
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Копируем код
COPY vdt_webprog_lab1.py .

#Открываем порт 4200
EXPOSE 4200

#Команда запуска
CMD ["uvicorn", "vdt_webprog_lab1:app", "--host", "0.0.0.0", "--port", "4200"]