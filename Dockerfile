

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
CMD ["/bin/bash", "-c", "python -m pytest -n auto --reruns 3 --browser_name=chrome  --alluredir=/app/allure-results --verbose tests && sleep infinity"]
