def f(d):
    all=d
    sum=0
    num_of_flights=0
    count=0
    for flight in all.values():
        sum=sum+flight
        num_of_flights=num_of_flights+1
    avg=sum/num_of_flights
    for flight in all.values():
        if flight > avg:
            count=count+1


    return sum, num_of_flights,avg,count





print(f({"LO231":150,"BA787":120,"NZ15":30}))
print(f({"LO231":150,"BA787":20,"NZ15":30}))