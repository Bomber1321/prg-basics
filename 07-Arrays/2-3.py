# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food=0
trans=0
util=0
week_sum=[0,0,0,0]
total=0
week_nr=0
total=0
for week in monthly_expenses:
    food += week[0]
    trans += week[1]
    util += week[2]
    for expense in week:
        week_sum[week_nr] +=expense
    total+=week_sum[week_nr]
    week_nr+=1
    
        

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',trans)
print('Utilities:',util)
print('Week 1:',week_sum[0])
print('Week 2:',week_sum[1])
print('Week 3:',week_sum[2])
print('Week 4:',week_sum[3])
print('---------------')
print('TOTAL:',total)