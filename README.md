
This project is a skinny alternative to bigger crm applications, (Sugacrm) with a simple mailing workflow.

The app is already working, and i use it on daily base for my office job marketing.

------------------

5) QUICK INSTALL:

apt-get install python-setuptools python-dev build-essential

easy_install virtualenv

virtualenv --no-site-packages bittercrm

source bittercrm/bin/activate

cd bittercrm

pip install -e git+https://github.com/django/django.git@1.5b2#egg=django

pip install south

git clone https://github.com/sebadima/bittercrm.git

cd bittercrm

sh django_server

------------------



To customize the project:


1) execute 'cp setup.sample setup' in main project directory, and customize newly created file with your real gmail  credentials.


2) launch the app with  'sh runserver' this will execute the code on ip port 8044.


3) edit django_server file to change the ip port.


------


If you want to execute the app with a real http server (cherrypy, much simpler than apache):

   pip istall cherrypy

   python server.py & 
   
   do not forget the ampersand '&' at the end of command

   press return.


