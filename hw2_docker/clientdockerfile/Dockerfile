FROM python:latest
ADD ./client_persistent_storage/ /client_storage/
WORKDIR /client_storage/
EXPOSE 7788
CMD ["python3","client.py"]