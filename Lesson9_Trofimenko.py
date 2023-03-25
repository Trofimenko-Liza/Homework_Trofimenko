import re

#task 1
result = re.search('^\w.*\w$', 'This is a homework 25647_')
print(result)


#task 2
result = re.sub(r'\(|\)| ', '', '["example (.com)", "github (.com)", "stackoverflow (.com)"]')
print(result)


