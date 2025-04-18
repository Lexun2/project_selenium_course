FROM python:3.9-slim

# Установка зависимостей для Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# Установка Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Установка Python-зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем тесты внутрь контейнера
COPY . .

# Точка входа по умолчанию
CMD ["python", "-m", "pytest", "tests", "--alluredir=allure-results"]


# FROM --platform=linux/amd64 python:3.12-slim

# # Переключаемся на root для установки зависимостей
# USER root

# # Устанавливаем системные зависимости
# RUN apt-get update && apt-get install -y \
#     wget gnupg unzip curl xvfb fonts-liberation libappindicator3-1 libasound2 \
#     libatk-bridge2.0-0 libnspr4 libnss3 libxss1 libxtst6 xdg-utils ca-certificates \
#     && rm -rf /var/lib/apt/lists/*

# # # Добавляем ключ и репозиторий Google Chrome
# # RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | \
# #     gpg --dearmor -o /usr/share/keyrings/google-linux-signing-keyring.gpg && \
# #     echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-signing-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | \
# #     tee /etc/apt/sources.list.d/google-chrome.list && \
# #     apt-get update && \
# #     apt-get install -y google-chrome-stable

# # Устанавливаем фиксированную версию ChromeDriver 
# #RUN wget -q "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/135.0.7049.84/linux64/chromedriver-linux64.zip" -O /tmp/chromedriver.zip && \
# #    unzip /tmp/chromedriver.zip -d /tmp && \
# #    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
# #    chmod +x /usr/local/bin/chromedriver && \
# #    rm -rf /tmp/chromedriver.zip /tmp/chromedriver-linux64    


# # Установка Chrome
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# # Установка ChromeDriver
# RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
#     && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
#     && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


# # Устанавливаем дополнительные зависимости для webdriver-manager
# RUN apt-get update && apt-get install -y \
#     wget unzip curl \
#     && rm -rf /var/lib/apt/lists/*

# # Создаем директорию для кэша webdriver-manager и даем права
# RUN mkdir -p /root/.wdm && chmod -R 777 /root/.wdm

# # Настраиваем переменные окружения для webdriver-manager
# ENV PYTHONUNBUFFERED=1 \
#     WDM_LOG_LEVEL=0 \
#     WDM_PROGRESS_BAR=0 \
#     WDM_SSL_VERIFY=0


# # Создаём рабочую директорию
# WORKDIR /app

# # Копируем requirements и устанавливаем Python-зависимости
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Копируем тесты внутрь контейнера
COPY . .

# Точка входа по умолчанию
ENTRYPOINT ["python", "-m", "pytest", "tests", "--alluredir=allure-results"]

