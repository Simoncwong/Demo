#TempConvert.py   10-17-2019

TempStr = input("Enter temperature:")
if TempStr[-1] in ['F', 'f']:
  C = (eval(TempStr[0:-1]) - 32)/1.8
  print("Temp is {:.2f}C".format(C))
elif TempStr [-1] in ['C', 'c']:
  F = 1.8 * eval(TempStr[0:-1]) + 32
  print("Temp is {:.2f}F".format(F))
else:
    print("Invalid input")
