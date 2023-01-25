podman run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -v ./data:/var/lib/mysql -d docker.io/library/mariadb
podman run --network="host" -e DB_PASS=mypass mypyapp:latest