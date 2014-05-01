

This project is a skinny alternative to bigger crm applications, (Sugacrm) with a simple mailing workflow.

The app is already working, and i use it on daily base for my office job marketing.

----------------------------------------------------------------------------------------------


To run the project:


1) execute 'cp setup.sample setup' in main project directory, and customize newly created file with your real gmail credentials.


2) launch the app with  'sh runserver' this will execute the code on ip port 8044.


3) edit runserver file to change the ip port .


----------------------------------------------------------------------------------------------


4) if you want to execute the app with a real http server (cherrypy):

   pip istall cherrypy

   python server.py &

   do not forget the ampersand '&' at the end of command

   press return.
