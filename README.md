# StockReadingApp
A minimal inventory management app

## Local Setup

- You should start by creating a virtualenv
- Install requirement
   ```sh
   $ pip install -r requirements
   ```
- Setup your postgresql database named 'stockreading'. Or edit the database name in the setting to match yours.
- Migrate the database by running
   ```sh
   $ python manage.py migrate
   ```
- Then run
   ```sh
   $ python manage.py collectstatic
   ```
- Run your server
   ```sh
   $ python manage runserver
   ```
You are all set !