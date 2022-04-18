FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
# run this before copying requirements for cache efficiency
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/


# expose the port 8000
EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

# docker-compose -f docker-compose.yml up --build

# docker build -t duvanmelius1/transturismo -f Dockerfile .

# docker push duvanmelius1/transturismo