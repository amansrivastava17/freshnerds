import re
import os
import argparse
import json

def pretty(filename):					# we pass json filename 
	try:
		diri=os.getcwd()			
		f=open(diri+"/"+filename,'r')
		b = str(json.loads(f.read()))						#read all file content 
		f.close()
		b=b.replace("'","\"")
		i = 0
		k=0;
		p=[]								#p is a list of all character which comes in pretttify json file
		idn=""								#idn is used for spacing like when braces closes we have to decrease spaces by 2 whitespaces 
		while i<len(b)-1:                   #loop through each character of json file
			if b[i] == '{' :
				#starting point of object  
				p.append(b[i])
				p.append("\n")
				p.append("\n")
				#idn is append with two white spaces for keys come under object 
				idn=idn+"  "	
				p.append(idn)
			elif (b[i]=='}') & (b[i+1]==',') :
				#when an object closes and there are further more objects present
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
				#for each comma
				d=b[i:-1]
				#now check if after comma if any key comes or any value if key comes break line and for value continue in same line
				if(re.match(',[\s]*\"[\w]+\":',d)):
					#regular expression to check if after comma key comes
					p.append(b[i])
					p.append("\n")
					p.append("\n")
					p.append(idn)
				else:
					#if any value occurs after comma
					p.append(b[i])
		
			elif b[i]=='}':
				#for closing of object and there are no further objects present
				idn=idn[0:-2]
				p.append("\n")
				p.append("\n")
				p.append(idn)
				p.append(b[i])
				p.append(idn)
			
			elif (b[i]==' ')| (b[i]=='\n'):
				#ignore spaces and break line characters
				pass

			else:
				#for all characters other than special charcter mentioned above
				p.append(b[i])
			i=i+1
		p.append(b[len(b)-1])
		ans= "".join(p)
		f=open(diri+"/"+filename,'w')
		f.write(ans)
		f.close()
		return True
	except ValueError, e:
		print ("JSON object issue: %s") % e
		return False

def Main():
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

     
