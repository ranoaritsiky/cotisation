# 
FROM python:3.10.6-slim-bullseye


# 
WORKDIR  /usr/src/app

# 
COPY ./requirements.txt  .

RUN  pip install --upgrade pip
# 
RUN pip install --no-cache-dir --upgrade -r  /usr/src/app/requirements.txt

# 
COPY . .

# 
# RUN python main.py

EXPOSE 8002

CMD ["python3.10", "server/main.py"]