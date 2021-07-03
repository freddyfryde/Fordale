while True:
  print ("####################")
  expression = input ("Введите пример: ")
  firstNum = ""
  secondNum = ""
  action = ""
  check = False

  if expression == "выход":
    break

  for i in expression:
    try:  
      i = int (i)
      i = str (i)
      if (check):
        secondNum += i
      else:
        firstNum += i
    except ValueError:
      action += i
      check = True

  firstNum = float (firstNum)
  secondNum = float (secondNum)

  print ("Ответ:", end = " ")

  try:
    if action == "+":
      print (firstNum + secondNum)
    elif action == "-":
      print (firstNum - secondNum)
    elif action == "*":
      print (firstNum * secondNum)
    elif action == "/":
      print (firstNum / secondNum)
    elif action == "**":
      print (firstNum ** secondNum)
    elif action == "%":
      print (firstNum % secondNum)
    elif action == "//":
      print (firstNum // secondNum)
    else:
      print ("не правильно выбрано действие")
  except ZeroDivisionError:
    print ("на 0 делить нельзя")
