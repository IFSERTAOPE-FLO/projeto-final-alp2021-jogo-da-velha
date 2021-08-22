import random
import os
def vencedor(resultado):
    if resultado == "win":
     print("O jogador Venceu!")
    elif resultado == "lose":
     print("O jogador perdeu")
    else:
     print("Deu velha!")
def vencedor_2P(resultado, jogador1, jogador2):
    if resultado == "win":
     print("O", jogador1, "Venceu!")
    elif resultado == "lose":
     print("O", jogador2, "Venceu!")
    else:
     print("Deu velha!")
def comparar(a, b, c, d, e, f, g, h, i, vs):
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
 elif vs == 5:
  return "empate"
 else:
  return "nada"
def inicio():
 print("*="*19)
 print("*="*19)
 print ("*=*=SEJA BEM VINDO AO JOGO DA VELHA=*=")
 print("*="*19)
 print("*="*19)
 modo()
def level():
 print("Escolha o level")
 print("1 \ fácil, 2 \ médio, 3 \ hard")
 lev = input()
 if lev == "1":
  os.system("cls")
  Level_Facil()
 if lev == "3":
  os.system("cls")
  modo_singular()
 if lev == "2":
  print("falta termina")
def s_n():
 print("Digite")
 print("1 \ para reiniciar 2 \ para sair")
 Sair_N = input()
 if Sair_N == "1":
  inicio()
  os.system("cls")
 if Sair_N == "2":
  os.system("cls")
  print("até")
def modo():
 condicao = "true"
 condicao2 = "true"
 resposta = "1"
 jogadores = ""
 while condicao == "true":
  print("Escolha o modo de Jogo:")
  print("*="*19) 
  print("1 / para campeonato, 2 / jogos avusos")
  print("*="*19) 
  jogos = input()
  if jogos == "1":
   os.system("cls")
   print("você deseja continuar?")
   print("*="*19)
   print("1 / para continuar 2 / para reiniciar")
   print("*="*19)
   SIMUM = int(input(""))
   if SIMUM == 2:
    os.system("cls")
    inicio()
   else:
	   	modo_campeonato()
  elif jogos == "2":
   print("você deseja continuar?")
   print("*="*19)
   print("1 / para continuar 2 / para reiniciar")
   print("*="*19)
   SIMUM = int(input(""))
   if SIMUM == 2:
    inicio()
   else:
    condicao = "false"
    condicao = "false"
    while condicao2 == "true":
     print("Escolha quantos jogadores são:")
     print("1 / um jogador, 2 / dois jogadores")
     jogadores = input()
     if jogadores == "1":
      condicao2 = "false"
      while resposta == "1":
       modo_singular()
       resposta = input("Quer jogar denovo? 1 / sim  2 / não ")
       if resposta == "2":
        s_n()
     elif jogadores == "2":
      condicao2 = "false"
      while resposta == "1":
       modo_mutiplayer()
       resposta = input("Querem jogar denovo? 1 / sim  2 / não ")
       if resposta == "2":
        print("até")
     else:
      print("tente novamente")
  else:
    print("tente novamente")
def Level_Facil():
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
 vitorias = 0
 derrotas = 0
 vs = 0
 while resultado == "nada":
  os.system("cls")
  print("*="*12)
  print(" a | b | c    "+" "+a+" | "+b+" | "+c)
  print(" ---------    "+" ---------")
  print(" d | e | f    "+" "+d+" | "+e+" | "+f)
  print(" ---------    "+" ---------")
  print(" g | h | i    "+" "+g+" | "+h+" | "+i)
  print("*="*12)
  controle = 0
  vs = vs + 1
  if resultado == "nada":
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
  resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
  controle2 = 0
  if resultado == "nada":
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
    resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
 os.system("cls")
 print("*="*12)
 print(" a | b | c    "+" "+a+" | "+b+" | "+c)
 print(" ---------    "+" ---------")
 print(" d | e | f    "+" "+d+" | "+e+" | "+f)
 print(" ---------    "+" ---------")
 print(" g | h | i    "+" "+g+" | "+h+" | "+i)
 print("*="*12)
 if resultado == "win":
  vitorias = vitorias + 1
 elif resultado == "lose":
  derrotas = derrotas + 1
 vencedor(resultado)
 if resultado == "win":
  return "win"
 elif resultado == "lose":
  return "lose"
def modo_campeonato():
 v = 0
 condicao3 = "true"
 partidas = ""
 derrota = 0
 vitoria = 0
 while condicao3 == "true":
    print("Escolha quantos jogadores são:")
    print("1 / um jogador, 2 / dois jogadores")
    jogadores = input()
    if jogadores == "1":
     condicao3 = "false"
     partidas = int(input("Quantas partidas serão? "))
     while v != partidas:
      result = level()	 
      v = v + 1
      if result == "win":
        vitoria = vitoria + 1 
      elif result == "lose":
        derrota = derrota + 1
      print("\n")
      print("=-"*10)
      print("|      Placar      |")
      print("=-"*10)
      print("Jogador_1:", vitoria,"/",derrota,"Jogador_2")
      print("\n")
      if vitoria > derrota:
       print("O jogador_1 venceu!")
      elif derrota > vitoria:
       print("O jogador_2 venceu!")
      else:
       print("Empate!")
       print("Ambos jogaram muito bem!")
    elif jogadores == "2":
     condicao3 = "false"
     partidas = input("Quantas partidas serão? ")
     while v != partidas:
      result = modo_mutiplayer()
      v = v + 1
      if result == "win":
        vitoria = vitoria + 1 
      elif result == "lose":
        derrota = derrota + 1
      print("\n")
      print("=-"*10)
      print("   Placar")
      print("=-"*10)
      print("Jogador_1:", vitoria,"/",derrota,":Jogador_2")
      print("\n")
      if vitoria > derrota:
       print("O jogador_1 venceu!")
      elif derrota > vitoria:
       print("O jogador_2 venceu!")
      else:
       print("Empate!")
       print("Ambos jogaram muito bem!")
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
 vitorias = 0
 derrotas = 0
 vs = 0
 while resultado == "nada":
  os.system("cls")
  print("*="*12)
  print(" a | b | c   "+" "+a+" | "+b+" | "+c)
  print(" ---------   "+" ---------")
  print(" d | e | f   "+" "+d+" | "+e+" | "+f)
  print(" ---------   "+" ---------")
  print(" g | h | i   "+" "+g+" | "+h+" | "+i)
  print("*="*12) 
  controle = 0
  vs = vs + 1
  if resultado == "nada":
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
  resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
  controle2 = 0
  if resultado == "nada":
   while controle2 != 1:
    if a == "O" and b == "O" and c != "X":
     jogador_2 = 3
     c = "O"
     print("O jogador_2 escolheu a posição c")
     controle2 = 1
    elif a == "O" and c == "O" and b != "X":
     jogador_2 = 2
     b = "O"
     print("O jogador_2 escolheu a posição b")
     controle2 = 1
    elif b == "O" and c == "O" and a != "X":
     jogador_2 = 1
     a = "O"
     print("O jogador_2 escolheu a posição a")
     controle2 = 1
    elif d == "O" and e == "O" and f != "X":
     jogador_2 = 6
     f = "O"
     print("O jogador_2 escolheu a posição f")
     controle2 = 1
    elif d == "O" and f == "O" and e != "X":
     jogador_2 = 5
     e = "O"
     print("O jogador_2 escolheu a posição e")
     controle2 = 1
    elif e == "O" and f == "O" and d != "X":
     jogador_2 = 4
     d = "O"
     print("O jogador_2 escolheu a posição d")
     controle2 = 1
    elif g == "O" and h == "O" and i != "X":
     jogador_2 = 9
     i = "O"
     print("O jogador_2 escolheu a posição i")
     controle2 = 1
    elif g == "O" and i == "O"  and h != "X":
     jogador_2 = 8
     h = "O"
     print("O jogador_2 escolheu a posição h")
     controle2 = 1
    elif h == "O" and i == "O" and g != "X":
     jogador_2 = 7
     g = "O"
     print("O jogador_2 escolheu a posição g")
     controle2 = 1
    elif a == "O" and d == "O" and g != "X":
     jogador_2 = 7
     g = "O"
     print("O jogador_2 escolheu a posição g")
     controle2 = 1
    elif a == "O" and g == "O" and d != "X":
     jogador_2 = 4
     d = "O"
     print("O jogador_2 escolheu a posição d")
     controle2 = 1
    elif d == "O" and g == "O" and a != "X":
     jogador_2 = 1
     a = "O"
     print("O jogador_2 escolheu a posição a")
     controle2 = 1
    elif b == "O" and e == "O" and h != "X":
     jogador_2 = 8
     h = "O"
     print("O jogador_2 escolheu a posição h")
     controle2 = 1
    elif b == "O" and h == "O" and e != "X":
     jogador_2 = 5
     e = "O"
     print("O jogador_2 escolheu a posição e")
     controle2 = 1
    elif e == "O" and h == "O" and b != "X":
     jogador_2 = 2
     b = "O"
     print("O jogador_2 escolheu a posição b")
     controle2 = 1
    elif c == "O" and f == "O" and i != "X":
     jogador_2 = 9
     i = "O"
     print("O jogador_2 escolheu a posição i")
     controle2 = 1
    elif c == "O" and i == "O" and f != "X":
     jogador_2 = 6
     f = "O"
     print("O jogador_2 escolheu a posição f")
     controle2 = 1
    elif f == "O" and i == "O"  and c != "X":
     jogador_2 = 3
     c = "O"
     print("O jogador_2 escolheu a posição c")
     controle2 = 1
    elif a == "O" and e == "O" and i != "X":
     jogador_2 = 9
     i = "O"
     print("O jogador_2 escolheu a posição i")
     controle2 = 1
    elif a == "O" and i == "O" and e != "X":
     jogador_2 = 5
     e = "O"
     print("O jogador_2 escolheu a posição e")
     controle2 = 1
    elif e == "O" and i == "O" and a != "X":
     jogador_2 = 1
     a = "O"
     print("O jogador_2 escolheu a posição a")
     controle2 = 1
    elif c == "O" and e == "O" and g != "X":
     jogador_2 = 7
     g = "O"
     print("O jogador_2 escolheu a posição g")
     controle2 = 1
    elif c == "O" and g == "O" and e != "X":
     jogador_2 = 1
     a = "O"
     print("O jogador_2 escolheu a posição a")
     controle2 = 1
    elif e == "O" and g == "O" and c != "X":
     jogador_2 = 3
     c = "O"
     print("O jogador_2 escolheu a posição c")
     controle2 = 1
    elif a == "X" and b == "X" and c != "O":
     jogador_2 = 3
     c = "O"
     print("O jogador_2 escolheu a posição c")
     controle2 = 1
    elif a == "X" and c == "X" and b != "O":
     jogador_2 = 2
     b = "O"
     print("O jogador_2 escolheu a posição b")
     controle2 = 1
    elif b == "X" and c == "X" and a != "O":
     jogador_2 = 1
     a = "O"
     print("O jogador_2 escolheu a posição a")
     controle2 = 1
    elif d == "X" and e == "X" and f != "O":
     jogador_2 = 6
     f = "O"
     print("O jogador_2 escolheu a posição f")
     controle2 = 1
    elif d == "X" and f == "X" and e != "O":
     jogador_2 = 5
     e = "O"
     print("O jogador_2 escolheu a posição e")
     controle2 = 1
    elif e == "X" and f == "X" and d != "O":
     jogador_2 = 4
     d = "O"
     print("O jogador_2 escolheu a posição d")
     controle2 = 1
    elif g == "X" and h == "X" and i != "O":
     jogador_2 = 9
     i = "O"
     print("O jogador_2 escolheu a posição i")
     controle2 = 1
    elif g == "X" and i == "X" and h != "O":
     jogador_2 = 8
     h = "O"
     print("O jogador_2 escolheu a posição h")
     controle2 = 1
    elif h == "X" and i == "X" and g != "O":
     jogador_2 = 7
     g = "O"
     print("O jogador_2 escolheu a posição g")
     controle2 = 1
    elif a == "X" and d == "X" and g != "O":
     jogador_2 = 7
     g = "O"
     print("O jogador_2 escolheu a posição g")
     controle2 = 1
    elif a == "X" and g == "X" and d != "O":
     jogador_2 = 4
     d = "O"
     print("O jogador_2 escolheu a posição d")
     controle2 = 1
    elif d == "X" and g == "X" and a != "O":
     jogador_2 = 1
     a = "O"
     print("O jogador_2 escolheu a posição a")
     controle2 = 1
    elif b == "X" and e == "X" and h != "O":
     jogador_2 = 8
     h = "O"
     print("O jogador_2 escolheu a posição h")
     controle2 = 1
    elif b == "X" and h == "X" and e != "O":
     jogador_2 = 5
     e = "O"
     print("O jogador_2 escolheu a posição e")
     controle2 = 1
    elif e == "X" and h == "X" and b != "O":
     jogador_2 = 2
     b = "O"
     print("O jogador_2 escolheu a posição b")
     controle2 = 1
    elif c == "X" and f == "X" and i != "O":
     jogador_2 = 9
     i = "O"
     print("O jogador_2 escolheu a posição i")
     controle2 = 1
    elif c == "X" and i == "X" and f != "O":
     jogador_2 = 6
     f = "O"
     print("O jogador_2 escolheu a posição f")
     controle2 = 1
    elif f == "X" and i == "X" and c != "O":
     jogador_2 = 3
     c = "O"
     print("O jogador_2 escolheu a posição c")
     controle2 = 1
    elif a == "X" and e == "X" and i != "O":
     jogador_2 = 9
     i = "O"
     print("O jogador_2 escolheu a posição i")
     controle2 = 1
    elif a == "X" and i == "X" and e != "O":
     jogador_2 = 5
     e = "O"
     print("O jogador_2 escolheu a posição e")
     controle2 = 1
    elif e == "X" and i == "X" and a != "O":
     jogador_2 = 1
     a = "O"
     print("O jogador_2 escolheu a posição a")
     controle2 = 1
    elif c == "X" and e == "X" and g != "O":
     jogador_2 = 7
     g = "O"
     print("O jogador_2 escolheu a posição g")
     controle2 = 1
    elif c == "X" and g == "X" and e != "O":
     jogador_2 = 1
     a = "O"
     print("O jogador_2 escolheu a posição a")
     controle2 = 1
    elif e == "X" and g == "X" and c != "O":
     jogador_2 = 3
     c = "O"
     print("O jogador_2 escolheu a posição c")
     controle2 = 1
    else:
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
    resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
 os.system("cls")
 print(" a | b | c    "+" "+a+" | "+b+" | "+c)
 print(" ---------    "+" ---------")
 print(" d | e | f    "+" "+d+" | "+e+" | "+f)
 print(" ---------    "+" ---------")
 print(" g | h | i    "+" "+g+" | "+h+" | "+i)
 if resultado == "win":
  vitorias = vitorias + 1
 elif resultado == "lose":
  derrotas = derrotas + 1
 vencedor(resultado)
 if resultado == "win":
  return "win"
 elif resultado == "lose":
  return "lose"
def Quem_comecara():
 import time
 print("iremos sorteiar quem começarar e usarar X")
 print("porfavor, espere 3 segundos")
 temp = time.localtime()
 time.sleep(1)
 os.system("cls")
 print("*=*=*=*=*=*=*=")
 print("=    *****   *")
 print("*       **   =")
 print("=    *****   *")
 print("*       **   =")
 print("=    *****   *")
 print("*=*=*=*=*=*=*=")
 time.sleep(1)
 os.system("cls")
 print("*=*=*=*=*=*=*=")
 print("=  ******    *")
 print("*      **  * =")
 print("=  ********* *")
 print("*  **  **    =")
 print("=  ******    *")
 print("*=*=*=*=*=*=*=")
 time.sleep(1)
 os.system("cls")
 print("*=*=*=*=*=*=*=")
 print("=     **     *")
 print("*   *  *     =")
 print("=      *     *")
 print("*      *     =")
 print("=    *****   *")
 print("*=*=*=*=*=*=*=")	
 time.sleep(1)
 os.system("cls")
 print("RESULTADO:")
 print("*="*15)
 sorteio = random.randint(1,2)
 if sorteio == 1:
  return "Usuario"
 else:
  return "Pc"
def modo_mutiplayer():
 J1vsJ2 = str(input("informe o nome do jogador "))
 J2vsJ1 = str(input("informe o nome do segundo jogador "))
 sorteidej = Quem_comecara()
 if sorteidej == "Usuario":
  J1 = print(J1vsJ2, "começarar e usarar X!")
  jogador1 = J1vsJ2
  jogador2 = J2vsJ1
 else:
  J2 = print(J2vsJ1,"começarar e usarar X!")
  jogador1 = J2vsJ1
  jogador2 = J1vsJ2
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
 vitorias = 0
 derrotas = 0
 vs = 0
 print(" a | b | c    "+" "+a+" | "+b+" | "+c)
 print(" ---------    "+" ---------")
 print(" d | e | f    "+" "+d+" | "+e+" | "+f)
 print(" ---------    "+" ---------")
 print(" g | h | i    "+" "+g+" | "+h+" | "+i)
 print("*="*12)
 while resultado == "nada":
  vs = vs + 1
  controle = 0
  if resultado == "nada":
   while controle != 1:
    print(f"Qual será a sua jogada", jogador1+"?",end="")
    jogador_1 = input()
    if jogador_1 == "a":
     if a != "O" and a!= "X":
      a = "X"
      controle = 1
      resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "b":
     if b != "O" and b!= "X":
      b = "X"
      controle = 1
      resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "c":
     if c != "O" and c!= "X":
      c = "X"
      controle = 1
      resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "d":
     if d != "O" and d!= "X":
      d = "X"
      controle = 1
      resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "e":
     if e != "O" and e!= "X":
      e = "X"
      controle = 1
      resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "f":
     if f != "O" and f!= "X":
      f = "X"
      controle = 1
      resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "g":
     if g != "O" and g!= "X":
       g = "X"
       controle = 1
       resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
     else:
       print("essa posição já está ocupada")
    elif jogador_1 == "h":
     if h != "O" and h!= "X":
      h = "X"
      controle = 1
      resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
     else:
      print("essa posição já está ocupada")
    else:
     if i != "O" and i!= "X":
      i = "X"
      controle = 1
      resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
     else:
      print("essa posição já está ocupada")
    print(" a | b | c    "+" "+a+" | "+b+" | "+c)
    print(" ---------    "+" ---------")
    print(" d | e | f    "+" "+d+" | "+e+" | "+f)
    print(" ---------    "+" ---------")
    print(" g | h | i    "+" "+g+" | "+h+" | "+i)
  if resultado == "nada": 
   controle2 = 0
   while controle2 != 1:
     print("Qual será a sua jogada", jogador2+"?",end="")
     jogador_2 = input()
     if jogador_2 == "a":
      if a != "O" and a!= "X":
       a = "O"
       controle2 = 1
       resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "b":
      if b != "O" and b!= "X":
       b = "O"
       controle2 = 1
       resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "c":
      if c != "O" and c!= "X":
       c = "O"
       controle2 = 1
       resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "d":
      if d != "O" and d!= "X":
       d = "O"
       controle2 = 1
       resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "e":
      if e != "O" and e!= "X":
       e = "O"
       controle2 = 1
       resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "f":
      if f != "O" and f!= "X":
       f = "O"
       controle2 = 1
       resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "g":
      if g != "O" and g!= "X":
        g = "O"
        controle2 = 1
        resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
      else:
        print("essa posição já está ocupada")
     elif jogador_2 == "h":
      if h != "O" and h!= "X":
       h = "O"
       controle2 = 1
       resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
      else:
       print("essa posição já está ocupada")
     else:
      if i != "O" and i!= "X":
       i = "O"
       controle2 = 1
       resultado = comparar(a, b, c, d, e, f, g, h, i, vs)
      else:
       print("essa posição já está ocupada")
     print(" a | b | c    "+" "+a+" | "+b+" | "+c)
     print(" ---------    "+" ---------")
     print(" d | e | f    "+" "+d+" | "+e+" | "+f)
     print(" ---------    "+" ---------")
     print(" g | h | i    "+" "+g+" | "+h+" | "+i)
 vencedor_2P(resultado, jogador1, jogador2)
 if resultado == "win":
  return "win"
 elif resultado == "lose":
  return "lose"
inicio()