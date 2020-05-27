import math


class Sq():
    square_list=list()

    def __init__(self,a):
        self.w=a
        self.square_list.append(self)

    def __repr__(self):
        return "{}by{}by{}by{}".format(self.w,self.w,self.w,self.w)
        
def Jud_type(parm1,parm2):
    if type(parm1) == type(parm2):
        return True
    else:
        return False


Sq1=Sq(100)
Sq2=Sq(101)


print(Jud_type(Sq1,Sq2))
print(Jud_type(Sq1,1))

print(Sq1)
print(Sq.square_list)

