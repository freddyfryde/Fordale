while True:
  # Объявление переменных
  print ("####################")
  expression = input ("Введите пример: ")
  firstNum = ""
  secondNum = ""
  action = ""
  check = False
  
  # Возможность выхода из цикла
  if expression == "выход":
    break
  
  # Обработка выражения, запись значений в переменные
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
  
  # Проведение математических операций
  print ("Ответ:", end = " ")
  if action == "+":
    print (firstNum + secondNum)
  if action == "-":
    print (firstNum - secondNum)
  if action == "*":
    print (firstNum * secondNum)
  if action == "/":
    print (firstNum / secondNum)
