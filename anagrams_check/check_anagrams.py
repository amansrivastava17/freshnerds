import math
def check_anagram():
	str1=raw_input("enter string 1: ")
	str2=raw_input("enter string 2: ")

	str1wl=str1.split(' ')
	str2wl=str2.split(' ')
	
	str1cwl=[]
	str2cwl=[]
	
	for item in str1wl:
		item2=list(item)
		item2.sort()
		str1cwl.append(item2)

	for item in str2wl:
		item2=list(item)
		item2.sort()
		str2cwl.append(item2)

	str1sortedw=[]
	str2sortedw=[]
	
	for item in str1cwl:
		str1sortedw.append(''.join(item))

	for item in str2cwl:
		str2sortedw.append(''.join(item))
	
	str1dic={}
	str2dic={}

	for item in str1sortedw:
		str1dic[item]=1

	for item in str2sortedw:
		str2dic[item]=1
	
	i=min(len(str1dic),len(str2dic))
	count=0
	j=0

	for item in str1dic:
		if(j<i):
			if(str2dic.get(item,0)!=0):
				count=count+1
		else:
			break
		j=j+1
	
	if count==i:
		print "strings are anagrams"

if __name__=='__main__':
	check_anagram()
	a
					

