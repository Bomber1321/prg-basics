# takes two numbers from keyboard
n1 = input("nr1: ")
n2 = input("nr2: ")

# define an anonymous function
mean = lambda x,y: (int(x)+int(y))/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {result}")