G='posts'
F='following'
E='followers'
B=Exception
C=open
A=print
import os,bs4
from bs4 import BeautifulSoup as N
H='\x1b[1;32m'
I='\x1b[1;91m'
J='\x1b[1;97m'
O='\x1b[1;94m'
def D():
	A(f"""
_________ .___                 __          
\\_   ___ \\|   | ____   _______/  |______   
/    \\  \\/|   |/    \\ /  ___/\\   __\\__  \\  
\\     \\___|   |   |  \\___ \\  |  |  / __ \\_
 \\______  /___|___|  /____  > |__| (____  /
        \\/         \\/     \\/            \\/ 
        
\t   Github.com/zhukov-z
\t   t.me/a_life07
""");id=C('ok.txt','r').read().splitlines()
	for D in id:
		E,F=D.split('|')[0],D.split('|')[1];G=M(E,F)
		try:G.print_info()
		except B as H:A(' {} User Name: {}'.format(I,E))
import requests as K
from bs4 import BeautifulSoup as L
class M:
	def __init__(A,uid,pas):A.username=str(uid);A.pas=str(pas)
	def get_request(A):
		C=K.get('https://www.instagram.com/'+A.username)
		if C.status_code==200:return C.content
		else:raise B(' This username is not used: {}'.format(A.username))
	def content_parser(A):B=A.get_request();C=L(B,'html.parser');return C
	def get_info(D):H=D.content_parser();I=H.find('meta',{'property':'og:description'}).get('content');A=I.split('-')[0];B=A[0:A.index('Followers')];A=A.replace(B+'Followers, ','');C=A[0:A.index('Following')];A=A.replace(C+'Following, ','');J=A[0:A.index('Posts')];K={E:B,F:C,G:J};return K
	def print_info(B):D=B.get_info();A(H);A(' User Name: {}'.format(B.username));A(' password: {}'.format(B.pas));A(' Followers: {}'.format(D[E]));A(' Following: {}'.format(D[F]));A(' Posts: {}'.format(D[G]));C('igfres.txt','a').write('%s|%s\n'%(B.username,B.pas));A(' -'*15);A(J)
class P:
	@staticmethod
	def read_file(filename):A=[A.rstrip('\n')for A in C(filename,encoding='utf8')];return A
D()
