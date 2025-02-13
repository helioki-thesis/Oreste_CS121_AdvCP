
num = int(input("Enter a number: "))
divs = 0
for i in range(1, num):
    if num % i == 0:
        divs += i
if num == divs:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")