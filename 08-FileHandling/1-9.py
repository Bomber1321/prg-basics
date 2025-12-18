###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'
i=0
with open(file_name) as file:
   for line in file:
      if job_title in line:
         i+=1
         print(f"{i}. {line}")