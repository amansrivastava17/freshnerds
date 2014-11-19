import socket
import os
import json 

setupfile=open('setup.json','rb')
read=setupfile.read()
read=json.loads(read)

dest_folder=read['directory_upload']
HOST=read['host']
PORT_NO=read['port']

def create_dir(dir_struct):
	for item in dir_struct:
		l=item.split('/')
		f="/"
		for item2 in l:
			if not os.path.exists(dest_folder+f+item2):
				os.mkdir(dest_folder+f+item2)
				f=f+item2+"/"
			else:
				f=f+item2+"/"


def receiving(s):
	#print "1"
	s.send("allowed")
	data2=s.recv(1024)
	filename=data2[12:]
	s.send("send size")
	
	k=s.recv(1024)

	filesize=long(k[4:])
	#yprint filesize
	s.send("send file")
		#f.write(data)
	f=open(dest_folder+"/"+filename,'wb')
	print "downloading file "+data2.split('/')[-1]
	#print "receivingggg"
	data=s.recv(1024)
	if data=="null":
		f.close()
	else:
		totalrecv=len(data)
		f.write(data)
		while totalrecv<filesize:
			#print "55"
			data=s.recv(1024)
			totalrecv+=len(data)
			f.write(data)
			print '{0:2f}'.format((totalrecv/float(filesize))*100)+"% Done"
		f.close()
	s.send("send next")
	nexti=s.recv(1024)
	#print nexti
	if nexti== "next file":
		#print "2"
		receiving(s)
	else:
		return


def Main():
	print "1"
	host=HOST
	port=PORT_NO

	s=socket.socket()
	s.connect((host,port))

	filename=raw_input("Enter File-->");
	if filename !='q':
		s.send(filename)
		data=s.recv(1024)
		if data[:6]=="filess":
			filesize=long(data[6:])
			message=raw_input('File exists,'+str(filesize)+'Bytes ,download(Y/N)?==>')
			if (message=='Y')|(message=='y'):
				s.send('OK')
				f=open(dest_folder+'/'+filename,'wb')
				data=s.recv(1024)
				totalrecv=len(data)
				f.write(data)
				while totalrecv<filesize:
					data=s.recv(1024)
					totalrecv+=len(data)
					f.write(data)
					print "{0:2f}".format((totalrecv/float(filesize))*100)+\
							"% Done"
				f.close()
			print "Download complete"

		elif data[:6]=="folder":
			#filesize=long(data[6:])
			message=raw_input('Folder exists,download(Y/N)?==>')
			if (message=='Y')| (message=='y'):
				s.send('OK')
				file_structure=s.recv(1024)
				if file_structure=="null":
					os.mkdir(dest_folder+filename)
				else:
					create_dir(file_structure.split('^'))
				
				#f=open('//home/aman/Desktop/new_'+filename,'wb')
				receiving(s)
			print "Download complete"
				
		else:
			print "File does not exists!"
	s.close()

if __name__=='__main__':
	Main()
