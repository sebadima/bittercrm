from django.http import HttpResponse
from django.views.generic import ListView


from clienti.models import Clienti

def index(request):
    return HttpResponse("Started Mass Mailing.")

import sqlite3



def pippo(request):

    import smtplib

    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587

    sender = 'sebastiano.dimartina@gmail.com'
    password = 'saranjwnfamygrpj'
    recipient = 'sebastiano.dimartina@gmail.com'
    subject = ' Cosa sono i programmi di marketing (CRM)?'

    body  = '''

<br>
Ti diamo 3 buoni motivi per non cestinare questa email
<br>
<br>
1) Non vendiamo nulla, vi aiutiamo a ricollocarvi in un settore emergente, quello dei CRM - il software di marketing targetizzato
<br>
<br>
2) Forniamo consulenza, come e quando deciderete, per la installazione e mantenimento della infrastruttura informatica
<br>
<br>
3) Formiamo a costo zero i link e le risorse (pdf, youtube) per integrare in vostri processi aziendali su Internet
Se conosci il software open source dai una occhiata a questo link
<br>
<br>
http://www.sugarcrm.com/
<br>
<br>
Se sei appena curioso e non vuoi spendere alcunche rispondi "OK" a questa email...
Ti invieremo gratuitamente i link e il materiale per partire da solo ed espandere il tuo business! 
<br>

    '''

    headers = ["From: " + sender, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)

    #recipient = 'sebastiano.dimartina@gmail.com'
    #session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    #session.quit()

    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()
    cursor.execute("select email from clienti_clienti where categoria_id = 2")
    a = cursor.fetchall() 
    risp = ""
    for x in range(len(a)):
       tmp = str(a[x])
       tmp2 = tmp[3:]
       tmp3 = tmp2[:-3]
       risp = risp + tmp3
       recipient = tmp3
       recipient = recipient + ".btag.it" 
       session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()

    ans = """

<html>

  <head>
  </head>

  <body>
    <a href="http://www.speedystack.com:8042/admin/">Mailing Successfully terminated. Back to Home</a>
  </body>

</html>

    """
    return HttpResponse(ans)





def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)



class PublisherList(ListView):
    model = Clienti



