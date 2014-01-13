import socket, sys, ssl

from ssl import wrap_socket, CERT_NONE, SSLError, PROTOCOL_SSLv23

def computerExpr(num1, op, num2):
	num1  =  int(num1)
	num2  =  int(num2)
	if  op == '-' :
		return num1 - num2
	elif op == '+' :
		return num1 + num2
	elif op == '*' :
		return num1 * num2
	elif op == '/' :
		return num1 / num2


DEFAULT_PORT  =  27993
DEFUALT_SSL_PORT  =  27994

HOST  =  sys.argv[1]
NUID  =  sys.argv[2]
PORT  =  int(sys.argv[3])
SSL   =  int(sys.argv[4])


if PORT  <  0: 
	PORT  =  DEFAULT_PORT 
 
snossl  =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if SSL  ==  1 :
	PORT  =  DEFUALT_SSL_PORT
	s  =  ssl.wrap_socket(snossl, None, None, False, CERT_NONE, PROTOCOL_SSLv23, None, True, True, None)
else :
	s  =  snossl

s.settimeout(5)
s.connect ((HOST, PORT))

s.sendall('cs5700spring2014 HELLO ' + '%s\n'%NUID)

while True:
	data  =  s.recv(256)
	print	'received : ', data
	strs =  data.split()
	if len(strs)  ==  5 :
		ret  =  computerExpr(strs[-3], strs[-2], strs[-1])
		s.sendall( 'cs5700spring2014 ' + '%d\n'%ret )
	elif len(strs) == 3 :
		secret  =  strs[1]
		print secret
		break

s.close()
