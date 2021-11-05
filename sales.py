sales =float(input("kindly enter your sales for the month :    "))
if sales >5000.00:
    commission =0.15*sales
    print( " your total sales is  " + str (commission))
elif sales > 3000.00:
    commission = 0.10*sales
    print("your sales is  " + str(commission))
elif  sales  <= 3000.00:
    commission = 0.05*sales
    print("your total sales is " + str  (commission))