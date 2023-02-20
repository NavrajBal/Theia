```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser 
docker-compose exec web python manage.py collectstatic
docker-compose exec web coverage run manage.py test
docker-compose exec web coverage run --omit='*/venv/*' manage.py test
docker-compose exec web coverage report
docker-compose exec web coverage html
```