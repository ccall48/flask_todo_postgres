## Getting started...
<p>
This is just a quick example of creating a development testing flask app using flask-sqlalchemy and a postgres database running in a docker environment using docker compose.
If you plan in using flask in production use gunicorn or the like to serve the application behind a reverse proxy like nginx or apache.
I will not cover how to do that here, the internet is a big place with plenty of examples how this can be done.
</P>
<p>
I did come accross some issues right now trying to run this on my m1 mbp with the latest version of postgres
"sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SCRAM authentication requires libpq version 10 or above." This seems to be a docker issue on all m1 arm
machines atm.. issue: [Github Issue](https://github.com/psycopg/psycopg2/issues/1360)
</p>

### Pull and Build container images.
```
docker-compose build
```

### Start project
```
docker-compose up -d
```

### Initalize Database
<p>
exec into python app container and initialize the database for use...
</p>
<p>
replace 'flask_todo' with your python container name if it is different or you renamed it.
</p>

```
docker exec -it flask_todo /bin/bash
```

Once inside the python container run.
```
flask createdb or flask initdb
```
The flask app is running in debug mode, so changes should reload container directly. To watch changes you can either load container with `docker-compose up` or just view container logs with `docker logs -f flask_todo`
<p>

The postgres database should servive between startups and rebuilds as we are keeping it in a local volume on the host machine.
`docker volume ls` will show you volumes on your machine. To remove/delete a volume use `docker volume rm <VOLUME_NAME>`.

</p>
