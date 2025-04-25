

FROM selenium/standalone-chromium:latest

USER root

# Установка переменных окружения
ENV HEADLESS=True
ENV PYTEST_VERBOSE=True
ENV ALLURE_RESULTS_DIR=/app/allure-results

# Установка Java, wget, unzip, python3-pip и bash
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    openjdk-17-jre-headless \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Установка последней версии Allure
RUN ALLURE_VERSION=$(wget -q -O - https://api.github.com/repos/allure-framework/allure2/releases/latest | grep -oP '"tag_name": "\K[0-9.]+') \
    && wget -q https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip \
    && unzip allure-${ALLURE_VERSION}.zip -d /opt/ \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure \
    && chmod +x /opt/allure-${ALLURE_VERSION}/bin/allure \
    && rm allure-${ALLURE_VERSION}.zip

# Установка Python-зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --timeout=100 --retries=3 -r requirements.txt

# Копирование файлов проекта
COPY . .

# Проверка содержимого /app
RUN ls -la /app

# ENTRYPOINT ["python", "-m", "pytest", "--alluredir=allure-results", "tests"]
# CMD ["/bin/bash", "-c", "python -m pytest --browser_name=chrome --alluredir=/app/allure-results/allure-results-$(date +%Y%m%d_%H%M%S) --verbose tests && sleep infinity"]
CMD ["/bin/bash", "-c", "python -m pytest --browser_name=chrome --alluredir=/app/allure-results --verbose tests && sleep infinity"]


# FROM --platform=linux/amd64 python:3.12-slim

# # Переключаемся на root для установки зависимостей
# USER root

# # Устанавливаем системные зависимости
# RUN apt-get update && apt-get install -y \
#     wget gnupg unzip curl xvfb fonts-liberation libappindicator3-1 libasound2 \
#     libatk-bridge2.0-0 libnspr4 libnss3 libxss1 libxtst6 xdg-utils ca-certificates \
#     && rm -rf /var/lib/apt/lists/*

# # Установка libssl1.1 (для selenium-manager)
# RUN wget http://deb.debian.org/debian/pool/main/o/openssl/libssl1.1_1.1.1w-0+deb11u1_amd64.deb \
#     && dpkg -i libssl1.1_1.1.1w-0+deb11u1_amd64.deb \
#     && rm libssl1.1_1.1.1w-0+deb11u1_amd64.deb

# # Добавляем ключ и репозиторий Google Chrome
# RUN wget -q -O /tmp/google-chrome-key.asc https://dl-ssl.google.com/linux/linux_signing_key.pub \
#     && gpg --dearmor /tmp/google-chrome-key.asc \
#     && mv /tmp/google-chrome-key.asc.gpg /etc/apt/trusted.gpg.d/google-chrome.gpg \
#     && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
#     && rm /tmp/google-chrome-key.asc

# # Устанавливаем дополнительные зависимости для webdriver-manager
# RUN apt-get update && apt-get install -y \
#     wget unzip curl \
#     && rm -rf /var/lib/apt/lists/*

# # Установка последней версии Allure
# RUN ALLURE_VERSION=$(wget -q -O - https://api.github.com/repos/allure-framework/allure2/releases/latest | grep -oP '"tag_name": "\K[0-9.]+') \
#     && wget -q https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip \
#     && unzip allure-${ALLURE_VERSION}.zip -d /opt/ \
#     && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure \
#     && chmod +x /opt/allure-${ALLURE_VERSION}/bin/allure \
#     && rm allure-${ALLURE_VERSION}.zip

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

# # Копируем тесты внутрь контейнера
# COPY . .

# # Точка входа по умолчанию
# ENTRYPOINT ["python", "-m", "pytest", "--alluredir=allure-results", "tests"]