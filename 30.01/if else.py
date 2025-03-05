num1=int(input("enter your age"))
if (num1>=18):
    print("eligible for voting")
elif(num1>=60):
    print ("your age is not eligible for voting")
else:
    ("not eligible")
    
current bill
num1=int(input("enter current bill"))
if (num1<=50):
    print("free current bill")
elif(num1>=200):
    print("please pay current bill")
else:
    print("you have used less than 50units")

num1=int(input("enter your marks"))
if (num1>=40):
    print("pass")
elif(num1>=80):
     print("A+")
else:
    print("fail")

last_digit = int(input("Enter the last digit of your phone number: "))

discount = 0

if last_digit == 0:
    discount = 20
elif last_digit % 2 == 0:
    discount = 10
else:
    discount = 15

print(f"You get a {discount}% discount!")