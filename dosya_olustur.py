import random
f=open("dosya.txt","w")
s=[]
level=10
aralik=level*500
f.write("Sayi:"+str(random.randint(1,aralik))+"\n")
f.close()