import math
pembatas="-------------------"
print(pembatas)
print("BODY MASS INDEX CALCULATOR")
print("BY : NEOZA")
print(pembatas)

weight=int(input("Your Weight[KG] : "))
height=int(input("Your Height[CM] : "))
heightcm=height/100
calculatedheight=math.pow(heightcm, 2)
bmi=weight/calculatedheight
roundbmi=round(bmi, 2)
floatroundbmi=float(roundbmi)
print("BMI :", floatroundbmi)
print(pembatas)

if floatroundbmi<18.5 :
  print("YOU'RE UNDERWEIGHT")
  print(pembatas)

elif floatroundbmi<24.9 and roundbmi>18.5 :
  print("YOU'RE IDEAL")
  print(pembatas)

elif floatroundbmi<29.9 and roundbmi>25.0 :
  print("YOU'RE FAT")
  print(pembatas)

elif floatroundbmi>30.0 :
  print("YOU'RE OBESE")
  print(pembatas)

else : 
  print("YOU'RE AN ALIEN")
  print=(pembatas)
