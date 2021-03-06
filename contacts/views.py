
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.generic import ListView

import sqlite3

from contacts.models import Contact



def index(request):

    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()

    cursor.execute("select email from contacts_contact")
    getemail = cursor.fetchall() 

    template = loader.get_template('contacts/index.html')
    context = RequestContext(request, { 'getemail': getemail,  })
    return HttpResponse(template.render(context))



def test(request):

    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()

    cursor.execute("select email from contacts_contact")
    getemail = cursor.fetchall() 

    template = loader.get_template('contacts/test.html')
    context = RequestContext(request, { 'getemail': getemail,  })
    return HttpResponse(template.render(context))



def prova(request):

    conn = sqlite3.connect("sqlite.db")
    cursor = conn.cursor()

    cursor.execute("select code from contacts_message")
    getcode = cursor.fetchall() 

    cursor.execute("select desc from contacts_message")
    getdesc = cursor.fetchall() 

    md = zip(getcode, getdesc)

    cursor.execute("select code from contacts_category")
    getcode = cursor.fetchall() 

    cursor.execute("select desc from contacts_category")
    getdesc  = cursor.fetchall() 
    cd = zip(getcode, getdesc)


    template = loader.get_template('contacts/prova.html')
    context = RequestContext(request, { 'md': md, 'cd': cd,  })
    return HttpResponse(template.render(context))




def mailing(request, param1, param2):

    import smtplib

    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587


    load_profile = open('setup', "r")
    read_it = load_profile.read()
    myLines = []

    for line in read_it.splitlines():
        if line.startswith("mail-login="):
            sender = line.replace("mail-login=", "")
        if line.startswith("mail-password="):
            password = line.replace("mail-password=", "")
            myLines.append(line)


    subject = '*** '
    recipient = sender
    conn = sqlite3.connect("sqlite.db")
    body = ""

    cursor = conn.cursor()
    query = "select desc from contacts_message where code = 'ANCHOR'"
    query = query.replace('ANCHOR', param1)
    cursor.execute(query)
    a = cursor.fetchall() 
    for x in range(len(a)):
       subject = subject + str(a[x])[3:][:-3]


    headers = ["From: " + sender, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)


    cursor = conn.cursor()
    query = "select body from contacts_message where code = 'ANCHOR'"
    query = query.replace('ANCHOR', param1)
    cursor.execute(query)
    a = cursor.fetchall() 
    for x in range(len(a)):
       body = body + str(a[x])[3:][:-3]


    cursor = conn.cursor()
    query = "select email from contacts_contact where (category_id = ANCHOR) and (action_id = '01')"
    query = query.replace('ANCHOR', param2)
    cursor.execute(query)
    body = body + "<br> msg:id:/ " + param1 + ' / ' + param2 
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
    <a href="http://www.speedystack.com:8044/admin/">Mailing Successfully terminated. Back to Home or close this Tab</a>
  </body>
</html>

    """

    return HttpResponse(ans)




def candidates(request):
    latest_poll_list = Contact.objects.order_by('nickname').filter(action_id = 1)[:20]
    ans = '<br> '.join([p.nickname for p in latest_poll_list])
    ans = ans + """
<html>
  <head>
  </head>
  <body>
    <br>
    <br>
 These Email addresses will receive your Mail Campaign... presse BACK button on your Browser
    <br>
    <br>
  </body>
</html>
    """

    return HttpResponse(ans)

