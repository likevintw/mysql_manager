docker run \
    --name mysql_demo -dit \
    --rm \
    -p 3306:3306 \
    --cpus='0.5' \
    --memory='2gb' \
    -e MYSQL_DATABASE=demo \
    -e MYSQL_ROOT_PASSWORD=testpassword \
    mysql:8.2.0