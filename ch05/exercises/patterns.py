#Part 1

def star_pyramid():
  print = ("Please enter the number of rows:")
  num_rows = int(input(":")) 
  for i in range(1, num_rows + 1):
    print(i * "*")


#Part 2
def rstar_pyramid():
  print = ("Please enter the number of rows:")
  num_rows = int(input(":"))
  for i in range(num_rows + 1, 1):
    print(i * "*")
  