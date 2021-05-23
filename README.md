To start app use following command
```sh
sudo docker-compose up --build
```
To load fixtures you need to enter to the api container:
```sh
sudo docker-compose run api bash
```
Then write 2 commands:
```sh
python3 manage.py loaddata users.json
python3 manage.py loaddata budgets.json
```