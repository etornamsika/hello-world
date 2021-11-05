#a =(1,2,3)
#type (a)'''
#a ,b,c = [1,'a',3.14]
#print (a)

#print(b)
#print (c)

#d = {'a':1 , 'b' :2, 'c':3, 'd':3.14}
#for e in d:
   # print(e)
    #for e in d.values():
       # print (e)
        #dict1 ={'q':1, 'r':4}
        #for e in dict1.items():
            #q,r = e
            #print('key = {0},value={1}'.format(q ,r))'''


#extended Unpacking
#l = [1,2,3,4,5,6]
#a = l[0]
#b =l[1:]
#print (a)
#print (b)
#(a ,*b) = l
 

 #ARGS

def func1(a, b, *c):
     print(a)
     print(b)
     print(c)
func1(10,20)
func1(10, 20, 30, 1, 2, 3)

def avg(*args):
    count = len(args)
    total = sum(args)
    return total/count
if (count == 0):
        return 0
else: 
        return total/count
    avg = ( 2, 2, 4, 4)