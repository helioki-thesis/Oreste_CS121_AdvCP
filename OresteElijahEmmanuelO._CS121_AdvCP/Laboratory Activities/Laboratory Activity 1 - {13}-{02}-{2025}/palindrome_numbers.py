num = int(input("Enter a number: "))

string_num = str(num)
if string_num == string_num[::-1]:
    print("Palindrome.")
else:
    print("Not palindrome.")
