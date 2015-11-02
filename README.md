# bulkvote

bulkvote is a Django based system to quickly make votes on lots of items - like voting yes or no to 100s of items. You can copy/paste in the list of items to be votes on, and you can pick the choices the user can choose between freely.

Each bulkvote created is assigned a unique URL which should be shared only with the people you want to participate in the vote.

# Development
bulkvote is under development. See the CHANGELOG for details.

# Installation
See requirements.txt for a list of packages used by bulkvote. You will also need something
to serve the application. I prefer uwsgi behind an nginx server. YMMV.

Create a database, anything supported by Django is fine.

Copy environment_settings.py.dist to environment_settings.py and change:
- SECRET_KEY (make it a 100+ chars random string)
- ALLOWED_HOSTS (the domainname of your bulkvote instance)
- DATABASES section (database info and credentials)

Run "manage.py migrate" to populate the database, and then update 
the 'name' and 'domain' columns in the 'django_site' db table to match
your bulkvote instance.

