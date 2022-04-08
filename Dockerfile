FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
# run this before copying requirements for cache efficiency
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/




# docker-compose -f docker-compose-users.yml up -d --build

# docker build -t duvanmelius1/novo_usuarios:users_1 -f Dockerfile.users .

# docker push duvanmelius1/novo_usuarios:users_1