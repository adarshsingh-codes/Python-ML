marks=int(input("Enter the marks: "))
if marks>100 or marks<0:
    print("invalid marks")
elif marks>=90:
    print("S grade")
elif marks>=80:
    print("A grade")
elif marks>=70:
    print("B grade")
elif marks>=60:
    print("C grade")
else:
    print("F grade")
