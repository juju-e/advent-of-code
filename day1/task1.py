f=open("input.txt")
r=f.readlines()
f.close()
def math(inp):
  return (inp//3)-2
total=0
for line in r[0:len(r)-1]:
   total+=math(int(line))
print(total)
