import statistics as sts

class clas ():
    def __init__(self,member) :
       self.member = member

    def get_info(self , name) :
        age = input("Enter the age list of class %s students : " %name)
        height = input("Enter the height list of class %s students : " %name)
        weight = input("Enter the weight list of class %s students : "%name)
        age= age.split(" ")
        height= height.split(" ")
        weight= weight.split(" ")
        age= [int(x) for x in age]
        height= [int(x) for x in height]
        weight= [int(x) for x in weight]
        return age,height,weight

    def cal_mean (self,age,height,weight) :
        age_mean    = sts.mean(age)
        height_mean = sts.mean(height)
        weight_mean = sts.mean(weight)
        print(age_mean)
        print(height_mean)
        print(weight_mean)
        return age_mean,height_mean,weight_mean



num_a = int(input("How many student are there in class A :"))
num_b = int(input("How many student are there in class B :"))
a= clas(num_a)
b= clas(num_b)
age_a,height_a,weight_a = a.get_info("A")
age_b,height_b,weight_b = b.get_info("B")

am_a,hm_a,wm_a= a.cal_mean(age_a,height_a,weight_a)
am_b,hm_b,wm_b= b.cal_mean(age_b,height_b,weight_b)
if am_a >am_b :
    print ("A")
elif am_a == am_b :
    print ("Same")
else :
    print ("B")