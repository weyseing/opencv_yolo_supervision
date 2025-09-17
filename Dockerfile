FROM python:3.10-slim
WORKDIR /app

# install system dependencies
RUN apt-get update -y && \
    apt-get install -y libgl1 libglx-mesa0  libglib2.0-0

# copy files
COPY . /app

# install python library
RUN pip install  --default-timeout=600 --no-cache-dir -r requirements.txt

# entrypoint
ENTRYPOINT ["tail", "-f", "/dev/null"]