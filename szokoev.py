szam= int(input("ird be az evszamot: \n"))
def szev(n):
      if n % 4 != 0:
            return False
      elif n % 400 == 0:
            return True
      elif n % 100 == 0:
            return False
      else:
            return True
if szev(szam) is True:
      print("Szokoev")
else:
      print("nem szokoev!")
