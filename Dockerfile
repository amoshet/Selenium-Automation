FROM python:3.9-slim

#installing packages
RUN pip install selenium

#setting directory where app will  be after install
WORKDIR /autopark

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#adds everything in folder from host to the container
COPY . .

#command to auto execute script on startup
#cannot auto execute script if needing user input
#CMD ["python", "autopark.py"]