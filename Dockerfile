FROM python:3.10.12-slim

WORKDIR /core
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
# in production, we must remove --reload
# I use it for dev purposes
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8080","--reload"]
