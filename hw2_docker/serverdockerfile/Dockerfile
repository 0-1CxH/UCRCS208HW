FROM python:latest
ADD ./server_persistent_storage/ /server_storage/
WORKDIR /server_storage/
EXPOSE 7789
CMD ["python3","server.py"]