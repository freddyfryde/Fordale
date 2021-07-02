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
    if check == False:
      if i == "+":
        check = True
        action = "+"
      elif i == "-":
        check = True
        action = "-"
      elif i == "*":
        check = True
        action = "*"
      elif i == "/":
        check = True
        action = "/"
      elif i == " ":
        None
      else:
        if i == " ":
          None
        else:
          firstNum += i
    else:
      secondNum += i

  firstNum = float (firstNum)
  secondNum = float (secondNum)

  print ("Ответ:", end = " ")
  if action == "+":
    print (firstNum + secondNum)
  if action == "-":
    print (firstNum - secondNum)
  if action == "*":
    print (firstNum * secondNum)
  if action == "/":
    print (firstNum / secondNum)