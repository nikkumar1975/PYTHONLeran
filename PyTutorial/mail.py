import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('nileshkashyap@gmail.com', 'nileshkashyap@gatech.edu',
"""To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
""")
server.quit()
