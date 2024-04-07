#import libraries here

def main():
  a=int(input("Enter the wavelength in nm: "))
  if a>=380 and a<450:
    print("The relevant color is Violet")
  elif a>=450 and a<495:
    print("The relevant color is Blue")       
  elif a>=495 and a<570:
    print("The relevant color is Green")
  elif a>=570 and a<590:
    print("The relevant color is Yellow")
  elif a>=590 and a<620:
    print("The relevant color is Orange")
  elif a>=620 and a<750:
    print("The relevant color is Red")
  else:
    print("Invalid input!")
  pass

if __name__ == "__main__":
  main()
