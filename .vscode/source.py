# Input files are  [a.in, b.in, c.in, d.in, e.in]
import os
f=open("input/c.in",'r') 
outter=open("output/c.out.txt",'a')
firstl=f.readline().split()
combo=int(firstl[0])    #number of pizzas

two=int(firstl[1])  # number of 2 person teams

three=int(firstl[2])     #number of 3 person teams

four=int(firstl[3])      # number of 4 person teams

all_combo={}   # dictionary to store pizza combos

score=0        #score at the end

deduct=0       # to check if all the person teams can get pizza

for i in range(0,combo):  #loop to store the pizza ingredient combination in dictionary

    h=f.readline().split()
    h[0]=int(h[0])
    all_combo[i]=[ele for ele in h]

pizzas=0      #number of pizzas delivered

counter=0        #counter for each delivery

pizza_assign=[0,0,0]
for_four=[]
for_three=[]
for_two=[]

def pizzagiven():
    global pizzas
    global pizza_assign
    
    separate=combo
    teams=0
    if(separate==4 or separate>5):              #for 4 person team

        cut=separate

        if(separate >=4*four):       # if there are enough pizzas for all 4-person team
            
            pizzas=pizzas+four*4
            teams=teams+four
            separate=separate- 4*four
            pizza_assign[0]=four
            
        else:                      # if there arent

            separate=0
            while cut%4!=0:
                cut=cut-1
                separate=separate+1

            teams=teams+cut//4
            pizzas=pizzas+cut
            pizza_assign[0]=cut//4

    if(separate>=3):               #for three person team
        if(separate >= 3*three):        # if there are enough pizzas for all 3 person teams
            pizzas=pizzas + three*3
            pizza_assign[1]=three
            separate=separate-three*3
            teams=teams+three

        else:                             # if there isn't enough pizzas for all 3 person teams
            cut=separate
            separate=0
            while cut%3 != 0:
                cut=cut-1
                separate=separate+1
            teams=teams+cut//3
            pizzas=pizzas+cut
            pizza_assign[1]=cut//3

    if(separate>=2):               #for 2 person team

        if(separate >= 2*two):        # if there are enough pizzas for all 2 person teams
            pizzas=pizzas + two*2
            pizza_assign[2]=two
            separate=separate-two*2
            teams=teams+two

        else:                             # if there isn't enough pizzas for all 2 person teams
            cut=separate
            separate=0
            while cut%2 != 0:
                cut=cut-1
                separate=separate+1
            teams=teams+cut//2
            pizzas=pizzas+cut
            pizza_assign[2]=cut//2
    test=str(teams)
    outter.write(test)




def separator(count,diff):              # function to deliver pizza
    global score
    global counter
    global all_combo
    global for_four
    global for_three
    global for_two
    li=[]          #stores the details of the ingredients added
    
    popper=[]       #stores the keys to pop

    check=0            #to check if all_combo has been completely traversed and increase diff along with it

    key=[]

    for i in range(count):       #for the range in a group

        for j in all_combo:        #to traverse through every pizza
            breaks=0         #stores the difference
            
            key.append(all_combo[j][0])
            for l in range(1,len(all_combo[j])):       #to traverse through the ingredients of each pizza
                p=all_combo[j][l]                 #a particular ingredient
                for piz in li:                 #checks if the ingredient is present in li(stores the ingredients selected)
                    if piz==p:
                        breaks=breaks+1
            
            if breaks <= diff:     #to check if the pizza can be added
                li.extend(all_combo[j][1::])
                popper.append(j)
                check=check+1
                break

    if check<count and diff<max(all_combo):          #if the pizza couldn't be added, then it increases the diff pointer
        
        separator(count,(diff+1))

    else:                                

        for i in popper:                        #loop to pop out the pizzas that have been delivered
            all_combo.pop(i)
            counter=counter+1
            if(count==2):
                for_two.append(i) 
            elif count==3:
                for_three.append(i)
            elif count==4:
                for_four.append(i)
        p=set(li)                 
        score=score+len(p)**2                   #score


def fours(foured):                #to assign pizzas to 4 person team
    while foured>0:
        separator(4,0)
        foured=foured-1




def threes(threed):
    while threed>0:
        separator(3,0)
        threed=threed-1





def twos(twoed):
    while twoed>0:
        separator(2,0)
        twoed=twoed-1

    


pizzagiven()
fours(pizza_assign[0])
threes(pizza_assign[1])
twos(pizza_assign[2])

if len(for_two)>0:
    k=0
    for i in for_two:
        if(k%2==0):
            outter.write("\n2 ")
        test=str(i)+" "
        outter.write(test)
        k=k+1

if len(for_three)>0:
    k=0
    for i in for_three:
        if(k%3==0):
            outter.write("\n3 ")
        test=str(i)+" "
        outter.write(test)
        k=k+1
if len(for_four)>0:
    k=0
    for i in for_four:
        if(k%4==0):
            outter.write("\n4 ")
        test=str(i)+" "
        outter.write(test)
        k=k+1
outter.close()