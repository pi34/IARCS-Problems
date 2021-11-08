     
# The problem for this can be found here: https://www.codechef.com/ZCOPRAC/problems/ZCO14001.
  
dimensions = input().split()
initial = input().split()
commands = input().split()

current = 0
occupied = False

for command in commands:
    if int(command) is 0:
        print (' '.join(initial))
        break
    elif int(command) is 1:
        if current != 0:
            current = current - 1
    elif int(command) is 2:
        if current != int(dimensions[0])-1 :
            current = current + 1
    elif int(command) is 3:
        if not occupied:
            if int(initial[current]) is not 0:
                occupied = True
                initial[current] = str(int(initial[current]) - 1)
    elif int(command) is 4:
        if occupied:
            if int(initial[current]) is not int(dimensions[1]):
                occupied = False
                initial[current] = str(int(initial[current]) + 1)
   
