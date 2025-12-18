###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, "r", encoding="utf-8") as email_content:
    email = email_content.read()

# regular expression pattern
# for amounts
pattern = '€(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
x=0
for amount in amounts:
   x+=int(amount)

# print result
print(x)