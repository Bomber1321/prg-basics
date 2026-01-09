class C:
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
    def __str__(self):
        if self.age>=18:
            return (self.name[0]+self.lastname[0]+str(self.age))
        else:
            return (self.name[0].lower()+self.lastname[0].lower()+str(self.age))




print(C("John","May",18))
    