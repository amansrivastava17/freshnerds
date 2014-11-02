import re
import os
import argparse
import json
#b="{'list':['a','b','list:'],'group':{'list':['hello','hi'],'aman':'srivastava'},'a':'b'}\n{'list':['a','b','list:'],'group':{'list':['hello','hi'],'aman':'srivastava'},'a':'b'}{'list':['a','b','list:'],'group':{'list':['hello','hi'],'aman':'srivastava'},'a':'b'}"
def pretty(filename):
	diri=os.getcwd()
	f=open(diri+"/"+filename,'r')
	read = f.readlines()
	f.close()
	b="".join(read)
	b=b.replace("'","\"")
	i = 0
	k=0;
	p=[]
	idn=""
	while i<len(b)-1:
		if b[i] == '{' :
			p.append(b[i])
			p.append("\n")
			p.append("\n")
			idn=idn+"  "	
			p.append(idn)
		elif (b[i]=='}') & (b[i+1]==',') :
			idn=idn[0:-2]
		
			p.append("\n")
			p.append("\n")
			p.append(idn)
			p.append(b[i])
			p.append(b[i+1])
			p.append("\n")
			p.append("\n")
			p.append(idn)
			i=i+1
		
		elif b[i]==',':
			d=b[i:-1]
			if(re.match(',[\s]*\"[\w]+\":',d)):
				p.append(b[i])
				p.append("\n")
				p.append("\n")
				p.append(idn)
			else:
				p.append(b[i])





		elif b[i]=='}':
			idn=idn[0:-2]
			
			p.append("\n")
			p.append("\n")
			p.append(idn)
			p.append(b[i])
			p.append(idn)
		
		elif (b[i]==' ')| (b[i]=='\n'):
			pass

		else:
			p.append(b[i])
		i=i+1
	p.append(b[len(b)-1])
	ans= "".join(p)
	f=open(diri+"/"+filename,'w')
	f.write(ans)
	f.close()
	return True

def Main():
	print "1"
	parser=argparse.ArgumentParser()
	parser.add_argument("filename",help="input json file you want to pretify",type=str)
	args=parser.parse_args()
	result=pretty(args.filename)
	if(result):
		print "your json file pretified succesfully"
	else:
		print "Process Unsuccessful"

if __name__=='__main__':
	Main()

     
