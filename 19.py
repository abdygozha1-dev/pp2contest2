n=int(input())
my_dict={} #creating empty dictionary

for i in range(n):
    s,t=input().split() #Amina Kamila, inputing strings in one line
    if s not in my_dict: #егер кілт болмаса, жасаймын
        my_dict[s]=int(t)
    else:
        my_dict[s]+=int(t) #болса value ларын қосамын
a=dict(sorted(my_dict.items())) #dictionary sorting with dict(), sorted(), items() function

for key, value in a.items(): #outputing dictionary element with items() and format
    print(f"{key} {value}") 

'''
my first code:
n=int(input())
dictionary={}
for i in range(n):
    s,t=map(input().split())
    if s not in dictionary:
        dictionary[s]=int(t)
    else:
        dictionary[s]+=int(t)

input: 5
HundredMillionStarsFromTheSky 10
WhereStarsLand 14
WhereStarsLand 4
TheThirdCharm 100
HusbandForHundredDays 1
output: HundredMillionStarsFromTheSky 10
HusbandForHundredDays 1
TheThirdCharm 100
WhereStarsLand 18
'''