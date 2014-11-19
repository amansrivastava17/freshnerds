import os
import threading
import socket
import json 

setupfile=open('setup.json','rb')
read=setupfile.read()
read=json.loads(read)

current_dir=read['directory_share']
PORT_NO=read['port']

lenth=len(current_dir)
def dir_struct(roots):
	dir_path_list=[]
	for root,directory,files in os.walk(roots):
		for dire in directory:
			dirpath=os.path.join(root,dire)
			print dirpath
			dir_path_list.append(dirpath[lenth:])

	return dir_path_list
		
def file_list_all(roots):
	file_path_list=[]
	for root,directory,files in os.walk(roots):
		for filename in files:
			filepath=os.path.join(root,filename)
			file_path_list.append(filepath[lenth:])	
	return file_path_list
		
def recievefile(name,socket):
	filename=socket.recv(1024)
	
	if os.path.isfile(current_dir+filename):
		socket.send("filess"+str(os.path.getsize(current_dir+filename)))
		userresponse=socket.recv(1024)
		if userresponse[:2]=='OK':
			#print "1"
			with open(current_dir+filename,'rb') as f:
				bytestosend=f.read(1024)
				socket.send(bytestosend)
				while bytestosend !="":
					bytestosend=f.read(1024)
					socket.send(bytestosend)
			f.close()
	elif os.path.isdir(current_dir+filename):
		socket.send("folder"+str(os.path.getsize(current_dir+filename)))
		#current_dir=os.getcwd()+"/"
		userresponse=socket.recv(1024)
		if userresponse[:2]=='OK':
			#print "1"
			filestruct=dir_struct(current_dir+filename)
			#print "2"
			print filestruct
			filestruct="^".join(filestruct)
			if filestruct =="":
				socket.send("null")
			else:
				socket.send(filestruct)
			print "3"
			file_list=file_list_all(current_dir+filename)
			#print file_list
			for files in file_list:
				permission=socket.recv(1024)
				if permission=="allowed":
					socket.send("sending file"+files)
					userresponse2=socket.recv(1024)
					if userresponse2=="send size":
						#print current_dir+files
						filesize=os.path.getsize(current_dir+files)
						#print filesize
						socket.send("size"+str(filesize))
						send=socket.recv(1024)
						if send == "send file":
							with open(current_dir+files,'rb') as f:
								#print "1"
								bytestosend=f.read(1024)
								#print "15555"
								#socket.send(bytestosend)
								if bytestosend!="":
									while bytestosend !="":
									#print "2"
										socket.send(bytestosend)
										bytestosend=f.read(1024)
									#print "3"
								else:
									socket.send("null")

								f.close()


								check=socket.recv(1024)
								if check=="send next":
									if files !=file_list[-1]:
										#print files
										socket.send("next file")
									else:
										socket.send("over")

	else:
		socket.send("Err")

def Main():
	host='127.0.0.1'
	port=PORT_NO
	s=socket.socket()
	s.bind((host,port))
	s.listen(5)

	print "server started"

	while True:
		c,addr=s.accept()
		print "client connected <"+str(addr)+">"
		t=threading.Thread(target=recievefile,args=('retrieve',c))
		t.start()
	s.close()

if __name__=='__main__':
	Main()