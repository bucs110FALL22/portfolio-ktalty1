#Part 1

def star_pyramid():
  levels = int(input("Please enter the number of rows:"))
  
  for i in range(1, levels + 1):
    print(i * "*")


#Part 2
def rstar_pyramid():
  levels = int(input("Please enter the number of rows:"))
  
  for i in range(levels, 0, -1):
    print(i * "*")

star_pyramid()
rstar_pyramid()
  