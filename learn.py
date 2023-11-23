import re


# Function to replace && and || with "and" and "or"
def replace_symbols(match):
    symbol = match.group(0)
    if symbol == '&&':
        return 'and'
    elif symbol == '||':
        return 'or'


# Get the number of lines
n = int(input())

# Process each line and apply the substitution
for _ in range(n):
    line = input()
    modified_line = re.sub(r'(?<= )(\&\&|\|\|)(?= )', replace_symbols, line)
    print(modified_line)
