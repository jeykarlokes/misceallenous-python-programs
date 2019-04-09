import sys
import cv2

encrypt={}
decrypt={}


def encry(b,im,key):
	i=0
	
	s=im.shape
	for x in range(s[0]):
		for y in range(s[1]):
			if i == len(b):
				val=encrypt['/']
				ci='{:b}'.format(im[x,y,key[1]]).zfill(8)
				cb='{:b}'.format(val).zfill(key[0])
				ci=ci[0:8-key[0]]+cb
				im[x,y,key[1]]=int(ci,2)	
				return im

			if b[i]==' ':
				val=encrypt['@']

			elif b[i]=='\n':
				val=encrypt['\\n']

			else:
				val=encrypt[b[i]]

			ci='{:b}'.format(im[x,y,key[1]]).zfill(8)
			cb='{:b}'.format(val).zfill(key[0])
			ci=ci[0:8-key[0]]+cb
			im[x,y,key[1]]=int(ci,2)	
			
			
			i+=1		


def decry(im,key):
		img=cv2.imread(im,1)
		mssg=''
		s=img.shape
		for x in range(s[0]):
			for y in range(s[1]):
				ci='{:b}'.format(img[x,y,key[1]]).zfill(8)
				cc=ci[8-key[0]:8]
				cc=int(cc,2)
				if cc>=40:
					return mssg
				if cc == 37:
					mssg+=' '
				else:
					mssg+=decrypt[cc]
								
				

def main():
	
	sym=input('Enter the symbol info file (symbol.txt):')
	fname=input('Enter the file containing message:')
	imgname=input('Enter the image name:')
	key=input('Enter the keys as "no of bits , plane":')
	key=key.split(',')
	key=(int(key[0]),int(key[1]))
	fname2=input('Enter the file to store the decrypted message:')
	fp=open(sym,'r')
	buf=fp.read().split('\n')
	for x in buf:
		x=x.split(' ')
		if len(x) == 2:
			encrypt.update({x[1]:int(x[0])})
			decrypt.update({int(x[0]):x[1]})	
	fp.close()
	fp=open(fname,'r')
	img=cv2.imread(imgname,1)
	s=img.shape
	s=s[0]*s[1]
	buf=fp.read()
	f=len(buf)
	if (f >= s):
		print("ERROR: message size too large, choose a larger image")
	else:
		im=encry(buf,img,key)
		cv2.imwrite('encry.tiff',im)		
		cv2.imshow('HIDDEN-INFO-IMAGE',im)
		cv2.waitKey(0)
		
	mssg=decry('encry.tiff',key)	
	fp=open(fname2,'w')
	fp.write(mssg)
	fp.close()
	print("OPEN FILE  "+ fname2+" TO VIEW YOUR DECRYPTED MESSAGE")

if __name__=='__main__':
	main()
	
