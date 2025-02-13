terms = int(input("Enter number of terms: "))
firstTerm, secondTerm = 0, 1
if terms <= 0:
    print("Invalid number.")
else:
    print('Fibonacci series: ', end=(""))
    for i in range(terms):
        print(firstTerm, end=" ")
        firstTerm, secondTerm = secondTerm, firstTerm + secondTerm