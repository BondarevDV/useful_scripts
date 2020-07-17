docker-compose down
docker rm -fv $(docker ps -aq)
sudo lsof -i -P -n | grep <port number>
