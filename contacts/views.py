
from django.http import HttpResponse
from django.views.generic import ListView


from contacts.models import Contact

def index(request):
    return HttpResponse("Started Mass Mailing.")

import sqlite3



def mailing(request):

    import smtplib

    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587

    sender = 'sebastiano.dimartina@gmail.com'
    password = 'saranjwnfamygrpj'
    subject = ' Cosa sono i programmi di marketing (CRM)?'
    recipient = 'sebastiano.dimartina@gmail.com'

    body  =  "mailing nuova vers"


    headers = ["From: " + sender, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)

    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()
    cursor.execute("select email from contacts_contact where action_id = 1")
    a = cursor.fetchall() 
    risp = ""
    for x in range(len(a)):
       tmp = str(a[x])
       tmp2 = tmp[3:]
       tmp3 = tmp2[:-3]
       risp = risp + tmp3
       recipient = tmp3
       session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()

    ans = """

<html>

  <head>
  </head>

  <body>
    <a href="http://www.speedystack.com:8044/admin/">Mailing Successfully terminated. Back to Home</a>
  </body>

</html>

    """
    return HttpResponse(ans)




def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)



class PublisherList(ListView):
    model = Contact



