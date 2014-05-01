
This project is simple alternative to bigger crm applications, (Sugacrm) with a simple mailing workflow.

At this moment my apps is just in a pre alpha release, but i would like to collaborate with some python Django programmer.

The app is already working, and i use it on daily base for my daily job marketing.




To run the project:

1) create a file named "setup" in main project directory
   with the following content:


------------- setup ---------------
[mail]
mail-login=your-gmail-login
mail-password=your-gmail-password
------------- setup ---------------


2) launch the app with : sh runserver
   this will execute the code on ip port 8044

3) edit runserver file to change the port 

4) if you want to execute the app with a real http server (cherrypy):
   pip istall cherrypy
   python server.py &
   do not forget the ampersand '&' at the end of command
