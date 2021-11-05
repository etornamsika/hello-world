#establishing  variables
widget_weight = 75
gizmos_weight = 112 


#accepting user inputs
Widget = float(input(" Enter number of widgets :  "))
Gizmos = float(input("Enter number of gizmos :   "))

#calculating
Total_Weight_of_widget =  widget_weight*Widget
Total_Weight_of_gizmos = gizmos_weight*Gizmos

#displaying
print("The total weight of wigdet consumed is:  ",Total_Weight_of_widget,"grams")
print("The total weight of Gizmos consumed is:  ",Total_Weight_of_gizmos,"grams")