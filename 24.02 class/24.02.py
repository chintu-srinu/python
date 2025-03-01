for i in range(1,101):
    print(i)

sum=0
for i in range (1,101):
    print(sum)
    sum = sum + i
    print(sum)

num1 =2
if num1%2 ==0:
    while i in range (1,50):
        print(i)
        print(odd)
        print(even)



num1 = int (input("enter"))
for i in range(1,21):
    print (num1*i)


for num in range(1,101):
    if num % 3 == 0, num % 5 == 0:
            print(i)


q=56723 : 32765
q=5672 r=3 =3
q=567 r=2 = 3*10+2=32
q=56 r=7
q=5 r=6
q=0 r=5


num1=56723
digit_sum = 0
rev_num = 0
count = 0
while num1 != 0:
    rem = num1 % 10
    digit_sum += rem
    rev_num = rev_num * 10 + rem
    num1 = num1
    count += 1
print (rev_num)
print(digit_sum)
print(count)

#check the given number is panloderm or not

if rev_num == num1:
    print("panindorome")
else:
    print("not")


db_username = "chintu"
db_password = "1234"

total_rem_chancs = 3


while total_rem_chancs > 0:
    input_username = input("enter name")
    input_password = input("enter password")

    if input_username == db_username and input_password == db_password:
        print("login")
        break
    # total_rem_chancs= 0
    else:
        total_rem_chancs -=1
        print("failed")
        print("still have ", total_rem_chancs, "chances")