FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    curl \
    ca-certificates \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

RUN node -v && npm -v

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ui/static_src/package.json ui/static_src/package-lock.json ./ui/static_src/

WORKDIR /app/ui/static_src
RUN npm install -g yarn && yarn install

WORKDIR /app
COPY . .

VOLUME /app/media

RUN python manage.py makemigrations
RUN python manage.py migrate

RUN mkdir -p /app/staticfiles

RUN python manage.py collectstatic --noinput

RUN python manage.py tailwind build

RUN python manage.py create_admin

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=settings.settings
ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "settings.wsgi:application"]