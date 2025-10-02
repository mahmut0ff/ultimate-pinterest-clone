# Базовый образ
FROM python:3.12-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y gcc libpq-dev

# Рабочая директория
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Команда по умолчанию
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]