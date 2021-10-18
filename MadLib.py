print("Enter two inputs for the mad lib: ")
user_input = input()
tokens = user_input.split()

while tokens[0] != "quit":
    print(f'Eating{tokens[1]} {tokens[0]} a day keeps the doctor away.')
    user_input = input()
    tokens = user_input.split()
