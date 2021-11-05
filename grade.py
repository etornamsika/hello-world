Science = float(input("Score for  int.science :   "))
Mathematics =  float(input("Score for maths :   "))
English =   float(input("Score for English:    "))
Social_studies = float(input("Score for social studies:    ")) 
Ict = float(input("Score for ICT :    "))
Language        = float(input("Score for Ghanaian Language :   "))
avg = (Science+Mathematics+English+Social_studies+Ict+Language)/6
if avg <= 100:
    print ("EXCELLENT")
elif avg <=99:
       print("Very good")
elif avg <= 89 :
           print("Good")
elif avg <=69 :   
               print("pass")
elif avg<=59 :
                   print("fair")
else:
                     print ("fail!!")
