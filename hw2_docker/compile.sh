docker network create hw2net --subnet=172.71.0.0/24
docker build -t hw2server ./serverdockerfile
docker build -t hw2client ./clientdockerfile
