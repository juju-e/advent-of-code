f=open("input.txt")
lines=f.readlines()
f.close()
def math(inp):
    return (inp//3)-2
def walk(inp):
 total=0
 inp=math(inp)
 total+=inp
 while(inp>0):
   if math(inp)<0:
      return total         
   inp=math(inp)
   total+=inp
 return total
total=0
for line in lines[0:len(lines)-1]:
 total+=walk(int(line))
print(total)
