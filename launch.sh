!#/bin/bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py loaddata viagens/fixtures/inital.json