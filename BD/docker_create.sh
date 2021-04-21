#! /bin/bash
docker run \
  -e MYSQL_DATABASE="p06" \
  -e MYSQL_USER="mabo" \
  -e MYSQL_PASSWORD="obam" \
  -e MYSQL_RANDOM_ROOT_PASSWORD="true" \
  --mount type=bind,src=/home/data/data,dst=/var/lib/mysql \
  -p 3306:3306 \
  --restart on-failure \
  --name mysqli mysql
