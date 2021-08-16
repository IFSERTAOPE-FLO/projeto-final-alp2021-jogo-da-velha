import random

def vencedor(resultado):
    if resultado == "win":
     print("O jogador Venceu!")
    elif resultado == "lose":
     print("O jogador perdeu")
    else:
     print("Deu velha!")

def vencedor_2P(resultado):
    if resultado == "win":
     print("O jogador_1 Venceu!")
    elif resultado == "lose":
     print("O jogador_2 Venceu!")
    else:
     print("Deu velha!")

def comparar(a, b, c, d, e, f, g, h, i):
 if a == "X" and b == "X" and c == "X":
  return "win"
 elif d == "X" and e == "X" and f == "X":
  return "win"
 elif g == "X" and h == "X" and i == "X":
  return "win"

 elif a == "X" and d == "X" and g == "X":
  return "win"
 elif b == "X" and e == "X" and h == "X":
  return "win"
 elif c == "X" and f == "X" and i == "X":
  return "win"

 elif a == "X" and e == "X" and i == "X":
  return "win"
 elif c == "X" and e == "X" and g == "X":
  return "win"

 elif a == "O" and b == "O" and c == "O":
  return "lose"
 elif d == "O" and e == "O" and f == "O":
  return "lose"
 elif g == "O" and h == "O" and i == "O":
  return "lose"

 elif a == "O" and d == "O" and g == "O":
  return "lose"
 elif b == "O" and e == "O" and h == "O":
  return "lose"
 elif c == "O" and f == "O" and i == "O":
  return "lose"

 elif a == "O" and e == "O" and i == "O":
  return "lose"
 elif c == "O" and e == "O" and g == "O":
  return "lose"
 elif a != " " and b != " " and c != " " and d != " " and e != " " and f != " " and g != " " and h != " " and i != " ":
  return "empate"
 else:
  return "nada"

def inicio():
 print("=-"*30)
 print("Jogo da velha")
 print("=-"*30)
 modo()

def modo():
 condicao = "true"
 resposta = "1"
 while condicao == "true":
  print("Esolha o modo de Jogo:")
  print("1 / um jogador, 2 / dois jogadores")
  jogadores = input()
  if jogadores == "1":
   while resposta == "1":
    modo_singular()
    condicao = "false"
    resposta = input("Quer jogar denovo? 1 / sim  2 / não ")
  elif jogadores == "2":
   while resposta == "1":
    modo_mutiplayer()
    condicao = "false"
    resposta = input("Querem jogar denovo? 1 / sim  2 / não ")
  else:
   print("tente novamente")

def modo_singular():
 a = " "
 b = " "
 c = " "
 d = " "
 e = " "
 f = " "
 g = " "
 h = " "
 i = " "
 resultado = "nada"
 jogador_1 = ""
 jogador_2 = ""
 controle = 0
 controle2 = 0
 while resultado == "nada":
  print(" a | b | c    "+" "+a+" | "+b+" | "+c)
  print(" ---------    "+" ---------")
  print(" d | e | f    "+" "+d+" | "+e+" | "+f)
  print(" ---------    "+" ---------")
  print(" g | h | i    "+" "+g+" | "+h+" | "+i)
  controle = 0
  while controle != 1:
   jogador_1 = input("Qual será a sua jogada? ")
   if jogador_1 == "a":
    if a != "O" and a!= "X":
     a = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "b":
    if b != "O" and b!= "X":
     b = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "c":
    if c != "O" and c!= "X":
     c = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "d":
    if d != "O" and d!= "X":
     d = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "e":
    if e != "O" and e!= "X":
     e = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "f":
    if f != "O" and f!= "X":
     f = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "g":
    if g != "O" and g!= "X":
      g = "X"
      controle = 1
    else:
      print("essa posição já está ocupada")
   elif jogador_1 == "h":
    if h != "O" and h!= "X":
     h = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   else:
    if i != "O" and i!= "X":
     i = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   resultado = comparar(a, b, c, d, e, f, g, h, i)
  controle2 = 0
  while controle2 != 1:
    jogador_2 = random.randint(1,9)
    if jogador_2 == 1 and a != "O" and a!= "X":
      a = "O"
      print("O jogador_2 escolheu a posição a")
      controle2 = 1
    elif jogador_2 == 2 and b != "O" and b!= "X":
      b = "O"
      print("O jogador_2 escolheu a posição b")
      controle2 = 1
    elif jogador_2 == 3 and  c != "O" and c!= "X":
       c = "O"
       print("O jogador_2 escolheu a posição c")
       controle2 = 1
    elif jogador_2 == 4 and  d != "O" and d!= "X":
       d = "O"
       print("O jogador_2 escolheu a posição d")
       controle2 = 1
    elif jogador_2 == 5 and  e != "O" and e!= "X":
       e = "O"
       print("O jogador_2 escolheu a posição e")
       controle2 = 1
    elif jogador_2 == 6 and  f != "O" and f!= "X":
       f = "O"
       print("O jogador_2 escolheu a posição f")
       controle2 = 1
    elif jogador_2 == 7 and  g != "O" and g!= "X":
       g = "O"
       print("O jogador_2 escolheu a posição g")
       controle2 = 1
    elif jogador_2 == 8 and  h != "O" and h!= "X":
       h = "O"
       print("O jogador_2 escolheu a posição h")
       controle2 = 1
    elif jogador_2 == 9 and  i != "O" and i!= "X":
       i = "O"
       print("O jogador_2 escolheu a posição i")
       controle2 = 1
    resultado = comparar(a, b, c, d, e, f, g, h, i)
 print(" a | b | c    "+" "+a+" | "+b+" | "+c)
 print(" ---------    "+" ---------")
 print(" d | e | f    "+" "+d+" | "+e+" | "+f)
 print(" ---------    "+" ---------")
 print(" g | h | i    "+" "+g+" | "+h+" | "+i)
 vencedor(resultado)
 
def modo_mutiplayer():
 a = " "
 b = " "
 c = " "
 d = " "
 e = " "
 f = " "
 g = " "
 h = " "
 i = " "
 resultado = "nada"
 jogador_1 = ""
 jogador_2 = ""
 controle = 0
 controle2 = 0
 print(" a | b | c    "+" "+a+" | "+b+" | "+c)
 print(" ---------    "+" ---------")
 print(" d | e | f    "+" "+d+" | "+e+" | "+f)
 print(" ---------    "+" ---------")
 print(" g | h | i    "+" "+g+" | "+h+" | "+i)
 while resultado == "nada":
  controle = 0
  while controle != 1:
   jogador_1 = input("Qual será a sua jogada Jogador_1? ")
   if jogador_1 == "a":
    if a != "O" and a!= "X":
     a = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "b":
    if b != "O" and b!= "X":
     b = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "c":
    if c != "O" and c!= "X":
     c = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "d":
    if d != "O" and d!= "X":
     d = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "e":
    if e != "O" and e!= "X":
     e = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "f":
    if f != "O" and f!= "X":
     f = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   elif jogador_1 == "g":
    if g != "O" and g!= "X":
      g = "X"
      controle = 1
    else:
      print("essa posição já está ocupada")
   elif jogador_1 == "h":
    if h != "O" and h!= "X":
     h = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   else:
    if i != "O" and i!= "X":
     i = "X"
     controle = 1
    else:
     print("essa posição já está ocupada")
   print(" a | b | c    "+" "+a+" | "+b+" | "+c)
   print(" ---------    "+" ---------")
   print(" d | e | f    "+" "+d+" | "+e+" | "+f)
   print(" ---------    "+" ---------")
   print(" g | h | i    "+" "+g+" | "+h+" | "+i)
   resultado = comparar(a, b, c, d, e, f, g, h, i)
  controle2 = 0
  while controle2 != 1:
    jogador_2 = input("Qual será a sua jogada Jogador_2? ")
    if jogador_2 == "a":
     if a != "O" and a!= "X":
      a = "O"
      controle2 = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_2 == "b":
     if b != "O" and b!= "X":
      b = "O"
      controle2 = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_2 == "c":
     if c != "O" and c!= "X":
      c = "O"
      controle2 = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_2 == "d":
     if d != "O" and d!= "X":
      d = "O"
      controle2 = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_2 == "e":
     if e != "O" and e!= "X":
      e = "O"
      controle2 = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_2 == "f":
     if f != "O" and f!= "X":
      f = "O"
      controle2 = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_2 == "g":
     if g != "O" and g!= "X":
       g = "O"
       controle2 = 1
     else:
       print("essa posição já está ocupada")
    elif jogador_2 == "h":
     if h != "O" and h!= "X":
      h = "O"
      controle2 = 1
     else:
      print("essa posição já está ocupada")
    else:
     if i != "O" and i!= "X":
      i = "O"
      controle2 = 1
     else:
      print("essa posição já está ocupada")
    print(" a | b | c    "+" "+a+" | "+b+" | "+c)
    print(" ---------    "+" ---------")
    print(" d | e | f    "+" "+d+" | "+e+" | "+f)
    print(" ---------    "+" ---------")
    print(" g | h | i    "+" "+g+" | "+h+" | "+i)
    resultado = comparar(a, b, c, d, e, f, g, h, i)
 vencedor_2P(resultado)
  
inicio()
