print("enter a palindrome: ")
user_input = input()

normal_str = user_input.replace(" ", "")
reverse_str = normal_str[::-1]

if normal_str == reverse_str:
    print("{} is a palindrome".format(user_input))
else:
    print("{} is not a palindrome".format(user_input))
