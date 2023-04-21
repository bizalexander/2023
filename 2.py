import random

First_initial=("K")

Last_name= ("Adam")

DGT=random.randrange(1,9)
TGB=random.randrange(1,9)
Afd=random.randrange(1,9)

user_name=(First_initial, Last_name, DGT, TGB, Afd)
print (user_name)



Upper_case_set =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', \
                 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', \
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Low_case_set=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', \
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
              't', 'u', 'v', 'w', 'x', 'y', 'z']
Number_set=["0",'1','2','3','4','5','6','7','8','9']


Special_ch =[ "_","!","$","#","@","%"]

Length_of_Password =random.randrange(5,9)
passwd1=random.choice(Upper_case_set+Low_case_set)
passwd2=random.choices(Upper_case_set+Low_case_set \
                      +Number_set+Special_ch,k=Length_of_Password-1)
passwd= passwd1+"".join(passwd2);
passwd=passwd.replace(passwd[1],random.choice(Upper_case_set+Low_case_set))
passwd=passwd.replace(passwd[2],random.choice(Upper_case_set))
passwd=passwd.replace(passwd[3],random.choice(Low_case_set))
passwd=passwd.replace(passwd[4],random.choice(Number_set))
passwd=passwd.replace(passwd[5],random.choice(Special_ch))
print("The password is: ", passwd)
