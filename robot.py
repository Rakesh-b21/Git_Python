from cmath import sqrt
print("""So lets find the distance of the robot from it's start position. 
For that we should need to move the robot:
Enter the values:
where direction = u for Up, d for Down, l for left, r for right
and steps = integer
To stop the robot just enter without giving any input""")
coordinates = {'u':0,'d':0,'l':0,'r':0}
while True:
    dir = input("Enter the direction: ")
    if dir=="": break
    
    steps = int(input("Enter the steps: "))
    
    coordinates[dir]+=1
x = abs(coordinates['l']-coordinates['r'])
y = abs(coordinates['u']-coordinates['d'])
if x==0 or y==0: print("Displacement of the robot from the start point is ",x+y)
else:
    print("Displacement of the robot from the start point is ",round(sqrt(x**2+y**2)))