stuff=[[
    'LOAD R1 406',
    'LOAD R2 230',
    'LOAD R3 220',
    'LOAD R4 72',
    'LOAD R5 10',
    'LOAD R6 3',
    'ADD R3 R4',
    'ADD R3 R5',
    'DIV R3 R6',
    'STORE (R3,R3,R3) (R1,R2)'
],
[
    'LOAD R1 814',
    'LOAD R2 591',
    'LOAD R3 255',
    'LOAD R4 73',
    'LOAD R5 118',
    'LOAD R6 35',
    'SUB  R4 R3',
    'SUB  R5 R3',
    'SUB  R6 R3',
    'STORE (R4,R5,R6) (R1,R2)'
]]
# print(stuff[0][0])
# print(len(stuff[0]))
# print(len(stuff))
# print(stuff[0][0].split())

def writereg(loc,val):
    RegD[loc]=val

RegD={"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0}

for i in stuff:
    for t in range(len(stuff[0])):
        single=i[t].split()
        if single[0]=="LOAD":
            writereg(single[1],single[2])
        if single[0]=="ADD":
            #print(single[1])
            #print(RegD[single[1]])
            writereg(single[1],int(RegD[single[1]])+int(RegD[single[2]]))
        if single[0]=="DIV":
            writereg(single[1],int(RegD[single[1]]) // int(RegD[single[2]]))
        if single[0]=="SUB":
            writereg(single[1],abs(int(RegD[single[1]])-int(RegD[single[2]])))
        if single[0]=="MUL":
            writereg(single[1],int(RegD[single[1]])*int(RegD[single[2]]))
        if single[0]=="STORE":
            rgb=single[1]
            rgb2=rgb.replace('(','').replace(')','')
            rgb3=rgb2.split(',')
            # print("This print= ",rgb3)
            # print("this print 1= ",rgb3[0])
            # print("this print 2= ",rgb3[1])
            # print("this print 3= ",rgb3[2])
            xy=single[2]
            #print(xy)
            xy2=xy.replace('(','').replace(')','')
            xy3=xy2.split(',')
            # print("this is x ",xy3[0])
            # print("this is y ",xy3[1])
            print(f'"STORE" : [{RegD[rgb3[0]]},{RegD[rgb3[1]]},{RegD[rgb3[2]]}],"xy": [ {RegD[xy3[0]]},{RegD[xy3[1]]} ]   ')
            #print(RegD[rgb3[0]])
        
            
        
   
    print(RegD)
    print("/n") 

# Regs=[0,0,0,0,0,0]
# print(Regs)
# Regs[1]=7
# print(Regs)

#RegD={"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0}
# print(RegD)
# RegD["R1"]=4
# writereg("R2",5)

#{"STORE":[r,g,b],"xy":[x,y]} 
        
#print(RegD)


