import random
import os
def comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs):
 if a == "X" and b == "X" and c == "X" and d == "X" and e == "X":
  return "win"
 elif f == "X" and g == "X" and h == "X" and i == "X" and j == "X":
  return "win"
 elif k == "X" and l == "X" and m == "X" and n == "X" and o == "X":
  return "win"
 elif p == "X" and q == "X" and r == "X" and s == "X" and t == "X":
  return "win"
 elif u == "X" and v == "X" and w == "X" and x == "X" and y == "X":
  return "win"
 elif a == "X" and f == "X" and k == "X" and p == "X" and u == "X":
  return "win"
 elif b == "X" and g == "X" and l == "X" and q == "X" and v == "X":
  return "win"
 elif c == "X" and h == "X" and m == "X" and r == "X" and w == "X":
  return "win"
 elif d == "X" and i == "X" and n == "X" and s == "X" and x == "X":
  return "win"
 elif e == "X" and j == "X" and o == "X" and t == "X" and y == "X":
  return "win"
 elif a == "X" and g == "X" and m == "X" and s == "X" and y == "X":
  return "win"
 elif e == "X" and i == "X" and m == "X" and q == "X" and u == "X":
  return "win"
 elif a == "O" and b == "O" and c == "O" and d == "O" and e == "O":
  return "lose"
 elif f == "O" and g == "O" and h == "O" and i == "O" and j == "O":
  return "lose"
 elif k == "O" and l == "O" and m == "O" and n == "O" and o == "O":
  return "lose"
 elif p == "O" and q == "O" and r == "O" and s == "O" and t == "O":
  return "lose"
 elif u == "O" and v == "O" and w == "O" and x == "O" and y == "O":
  return "lose"
 elif a == "O" and f == "O" and k == "O" and p == "O" and u == "O":
  return "lose"
 elif b == "O" and g == "O" and l == "O" and q == "O" and v == "O":
  return "lose"
 elif c == "O" and h == "O" and m == "O" and r == "O" and w == "O":
  return "lose"
 elif d == "O" and i == "O" and n == "O" and s == "O" and x == "O":
  return "lose"
 elif e == "O" and j == "O" and o == "O" and t == "O" and y == "O":
  return "lose"
 elif a == "O" and g == "O" and m == "O" and s == "O" and y == "O":
  return "lose"
 elif e == "O" and i == "O" and m == "O" and q == "O" and u == "O":
  return "lose"
 elif vs == 13:
  return "empate"
 else:
  return "nada"

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
def level(lev):
 if lev == "1":
  os.system("cls")
  Level_Facil()
 if lev == "2":
  os.system("cls")
  modo_singular()
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
 resposta2 = "1"
 tabela = ""
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
    while resposta2 == "1":
     modo_campeonato()
     resposta = input("Quer jogar denovo? 1 / sim  2 / não ")
     if resposta == "2":
      s_n()
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
    while condicao2 == "true":
     print("Escolha quantos jogadores são:")
     print("1 / um jogador, 2 / dois jogadores")
     jogadores = input()
     if jogadores == "1":
      condicao2 = "false"
      print("Qual será a tabela:")
      tabela = input("1 \ (3 por 3),    2 \ (5 por 5) ")
      if tabela == "1":
       while resposta == "1":
        modo_singular()
        resposta = input("Quer jogar denovo? 1 / sim  2 / não ")
        if resposta == "2":
         s_n()
      else:
       while resposta == "1":
        modo_singular_5_por_5()
        resposta = input("Quer jogar denovo? 1 / sim  2 / não ")
        if resposta == "2":
         s_n()
     elif jogadores == "2":
      condicao2 = "false"
      J1vsJ2 = str(input("informe o nome do jogador "))
      J2vsJ1 = str(input("informe o nome do segundo jogador "))
      print("Qual será a tabela:")
      tabela = input("1 \ (3 por 3),    2 \ (5 por 5) ")
      if tabela == "1":
       while resposta == "1":
        modo_mutiplayer(J1vsJ2, J2vsJ1)
        resposta = input("Querem jogar denovo? 1 / sim  2 / não ")
        if resposta == "2":
         print("até")
      else:
       while resposta == "1":
        modo_mutiplayer_5_por_5(J1vsJ2, J2vsJ1)
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
 tabela = [[" a | b | c    "+" "+a+" | "+b+" | "+c],
           [" ---------    "+" ---------"],
           [" d | e | f    "+" "+d+" | "+e+" | "+f],
           [" ---------    "+" ---------"],
           [" g | h | i    "+" "+g+" | "+h+" | "+i]]
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
  print(tabela[0][0])
  print(tabela[1][0])
  print(tabela[2][0])
  print(tabela[3][0])
  print(tabela[4][0])
  print("*="*12)
  tabela[0][0] = " a | b | c    "+" "+a+" | "+b+" | "+c
  tabela[2][0] = " d | e | f    "+" "+d+" | "+e+" | "+f
  tabela[4][0] = " g | h | i    "+" "+g+" | "+h+" | "+i
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
 tabela[0][0] = " a | b | c    "+" "+a+" | "+b+" | "+c
 tabela[2][0] = " d | e | f    "+" "+d+" | "+e+" | "+f
 tabela[4][0] = " g | h | i    "+" "+g+" | "+h+" | "+i
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
 nivel = ""
 while condicao3 == "true":
    print("Escolha quantos jogadores são:")
    print("1 / um jogador, 2 / dois jogadores")
    jogadores = input()
    if jogadores == "1":
     condicao3 = "false"
     partidas = int(input("Quantas partidas serão? "))
     print("Escolha o level")
     print("1 \ Fácil, 2 \ Médio, 3 \ Difícil")
     lev = input()
     if lev == "1":
      os.system("cls")
      nivel = "Level_Facil"
     elif lev == "2":
      os.system("cls")
      nivel = "modo_singular"
     elif lev == "3":
      os.system("cls")
      nivel = "modo_singular_5_por_5"
     while v != partidas:
      if nivel == "Level_Facil":
       result = Level_Facil()	 
       v = v + 1
      elif nivel == "modo_singular":
       result = modo_singular()
       v = v + 1
      else:
       result = modo_singular_5_por_5()
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
     print("Qual será a tabela:")
     tabela = input("1 \ (3 por 3),    2 \ (5 por 5) ")
     if tabela == "1":
      while v != partidas:
       result = modo_mutiplayer(J1vsJ2, J2vsJ1)
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
      while v != partidas:
       result = modo_mutiplayer_5_por_5(J1vsJ2, J2vsJ1)
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
 tabela = [[" a | b | c    "+" "+a+" | "+b+" | "+c],
          [" ---------    "+" ---------"],
          [" d | e | f    "+" "+d+" | "+e+" | "+f],
          [" ---------    "+" ---------"],
          [" g | h | i    "+" "+g+" | "+h+" | "+i]]
 resultado = "nada"
 jogador_1 = ""
 jogador_2 = ""
 controle = 0
 controle2 = 0
 vitorias = 0
 derrotas = 0
 vs = 0
 while resultado == "nada":
  tabela[0][0] = " a | b | c    "+" "+a+" | "+b+" | "+c
  tabela[2][0] = " d | e | f    "+" "+d+" | "+e+" | "+f
  tabela[4][0] = " g | h | i    "+" "+g+" | "+h+" | "+i
  os.system("cls")
  print("*="*12)
  print(tabela[0][0])
  print(tabela[1][0])
  print(tabela[2][0])
  print(tabela[3][0])
  print(tabela[4][0])
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
 tabela[0][0] = " a | b | c    "+" "+a+" | "+b+" | "+c
 tabela[2][0] = " d | e | f    "+" "+d+" | "+e+" | "+f
 tabela[4][0] = " g | h | i    "+" "+g+" | "+h+" | "+i
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
 print("*      **    =")
 print("=  ******    *")
 print("*  **        =")
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
def modo_mutiplayer(J1vsJ2, J2vsJ1):
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
 tabela = [[" a | b | c    "+" "+a+" | "+b+" | "+c],
          [" ---------    "+" ---------"],
          [" d | e | f    "+" "+d+" | "+e+" | "+f],
          [" ---------    "+" ---------"],
          [" g | h | i    "+" "+g+" | "+h+" | "+i]]
 resultado = "nada"
 jogador_1 = ""
 jogador_2 = ""
 controle = 0
 controle2 = 0
 vitorias = 0
 derrotas = 0
 vs = 0
 time = 1
 tabela[0][0] = " a | b | c    "+" "+a+" | "+b+" | "+c
 tabela[2][0] = " d | e | f    "+" "+d+" | "+e+" | "+f
 tabela[4][0] = " g | h | i    "+" "+g+" | "+h+" | "+i
 print("*="*12)
 print(tabela[0][0])
 print(tabela[1][0])
 print(tabela[2][0])
 print(tabela[3][0])
 print(tabela[4][0])
 print("*="*12)
 while resultado == "nada":
  vs = vs + 1
  controle = 0
  if resultado == "nada":
   while controle != 1:
    time = time + 1
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
    tabela[0][0] = " a | b | c    "+" "+a+" | "+b+" | "+c
    tabela[2][0] = " d | e | f    "+" "+d+" | "+e+" | "+f
    tabela[4][0] = " g | h | i    "+" "+g+" | "+h+" | "+i
    print(tabela[0][0])
    print(tabela[1][0])
    print(tabela[2][0])
    print(tabela[3][0])
    print(tabela[4][0])
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
     tabela[0][0] = " a | b | c    "+" "+a+" | "+b+" | "+c
     tabela[2][0] = " d | e | f    "+" "+d+" | "+e+" | "+f
     tabela[4][0] = " g | h | i    "+" "+g+" | "+h+" | "+i
     print(tabela[0][0])
     print(tabela[1][0])
     print(tabela[2][0])
     print(tabela[3][0])
     print(tabela[4][0])
 vencedor_2P(resultado, jogador1, jogador2)
 if resultado == "win":
  return "win"
 elif resultado == "lose":
  return "lose"

def modo_singular_5_por_5():
 a = " "
 b = " "
 c = " "
 d = " "
 e = " "
 f = " "
 g = " "
 h = " "
 i = " "
 j = " "
 k = " "
 l = " "
 m = " "
 n = " "
 o = " "
 p = " "
 q = " "
 r = " "
 s = " "
 t = " "
 u = " "
 v = " "
 w = " "
 x = " "
 y = " "
 tabela = [[" a | b | c | d | e    "+" "+a+" | "+b+" | "+c+" | "+d+" | "+e],
          [" -----------------    "+" ------------------"],
          [" f | g | h | i | j    "+" "+f+" | "+g+" | "+h+" | "+i+" | "+j],
          [" -----------------    "+" ------------------"],
          [" k | l | m | n | o    "+" "+k+" | "+l+" | "+m+" | "+n+" | "+o],
          [" -----------------    "+" ------------------"],
          [" p | q | r | s | t    "+" "+p+" | "+q+" | "+r+" | "+s+" | "+t],
          [" -----------------    "+" ------------------"],
          [" u | v | w | x | y    "+" "+u+" | "+v+" | "+w+" | "+x+" | "+y]]
 resultado = "nada"
 jogador_1 = ""
 jogador_2 = ""
 controle = 0
 controle2 = 0
 vitorias = 0
 derrotas = 0
 vs = 0
 while resultado == "nada":
  tabela[0][0] = " a | b | c | d | e    "+" "+a+" | "+b+" | "+c+" | "+d+" | "+e
  tabela[2][0] = " f | g | h | i | j    "+" "+f+" | "+g+" | "+h+" | "+i+" | "+j
  tabela[4][0] = " k | l | m | n | o    "+" "+k+" | "+l+" | "+m+" | "+n+" | "+o
  tabela[6][0] = " p | q | r | s | t    "+" "+p+" | "+q+" | "+r+" | "+s+" | "+t
  tabela[8][0] = " u | v | w | x | y    "+" "+u+" | "+v+" | "+w+" | "+x+" | "+y
  os.system("cls")
  print("*="*12)
  print(tabela[0][0])
  print(tabela[1][0])
  print(tabela[2][0])
  print(tabela[3][0])
  print(tabela[4][0])
  print(tabela[5][0])
  print(tabela[6][0])
  print(tabela[7][0])
  print(tabela[8][0])
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
    elif jogador_1 == "i":
     if i != "O" and i!= "X":
      i = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "j":
     if j != "O" and j!= "X":
      j = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "k":
     if k != "O" and k!= "X":
      k = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "l":
     if l != "O" and l!= "X":
      l = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "m":
     if m != "O" and m!= "X":
      m = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "n":
     if n != "O" and n!= "X":
      n = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "o":
     if o != "O" and o!= "X":
      o = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "p":
     if p != "O" and p!= "X":
      p = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "q":
     if q != "O" and q!= "X":
      q = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "r":
     if r != "O" and r!= "X":
      r = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "s":
     if s != "O" and s!= "X":
      s = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "t":
     if t != "O" and t!= "X":
      t = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "u":
     if u != "O" and u!= "X":
      u = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "v":
     if v != "O" and v!= "X":
      v = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "w":
     if w != "O" and w!= "X":
      w = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "x":
     if x != "O" and x!= "X":
      x = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "y":
     if y != "O" and y!= "X":
      y = "X"
      controle = 1
     else:
      print("essa posição já está ocupada")
    else:
      print("Tente novamente")
      print("\n")

  resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
  controle2 = 0
  if resultado == "nada":
   while controle2 != 1:
     jogador_2 = random.randint(1,25)
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
     elif jogador_2 == 10 and  j != "O" and j!= "X":
       j = "O"
       print("O jogador_2 escolheu a posição j")
       controle2 = 1
     elif jogador_2 == 11 and  k != "O" and k!= "X":
       k = "O"
       print("O jogador_2 escolheu a posição k")
       controle2 = 1
     elif jogador_2 == 12 and  l != "O" and l!= "X":
       l = "O"
       print("O jogador_2 escolheu a posição l")
       controle2 = 1
     elif jogador_2 == 13 and  m != "O" and m!= "X":
       m = "O"
       print("O jogador_2 escolheu a posição m")
       controle2 = 1
     elif jogador_2 == 14 and  n != "O" and n!= "X":
       n = "O"
       print("O jogador_2 escolheu a posição n")
       controle2 = 1
     elif jogador_2 == 15 and  o != "O" and o!= "X":
       o = "O"
       print("O jogador_2 escolheu a posição o")
       controle2 = 1
     elif jogador_2 == 16 and  p != "O" and p!= "X":
       p = "O"
       print("O jogador_2 escolheu a posição p")
       controle2 = 1
     elif jogador_2 == 17 and  q != "O" and q!= "X":
       q = "O"
       print("O jogador_2 escolheu a posição q")
       controle2 = 1
     elif jogador_2 == 18 and  r != "O" and r!= "X":
       r = "O"
       print("O jogador_2 escolheu a posição r")
       controle2 = 1
     elif jogador_2 == 19 and  s != "O" and s!= "X":
       s = "O"
       print("O jogador_2 escolheu a posição s")
       controle2 = 1
     elif jogador_2 == 20 and  t != "O" and t!= "X":
       t = "O"
       print("O jogador_2 escolheu a posição t")
       controle2 = 1
     elif jogador_2 == 21 and  u != "O" and u!= "X":
       u = "O"
       print("O jogador_2 escolheu a posição u")
       controle2 = 1
     elif jogador_2 == 22 and  v != "O" and v!= "X":
       v = "O"
       print("O jogador_2 escolheu a posição v")
       controle2 = 1
     elif jogador_2 == 23 and  w != "O" and w!= "X":
       w = "O"
       print("O jogador_2 escolheu a posição w")
       controle2 = 1
     elif jogador_2 == 24 and  x != "O" and x!= "X":
       x = "O"
       print("O jogador_2 escolheu a posição x")
       controle2 = 1
     elif jogador_2 == 25 and  y != "O" and y!= "X":
       y = "O"
       print("O jogador_2 escolheu a posição y")
       controle2 = 1
     resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
 os.system("cls")
 tabela[0][0] = " a | b | c | d | e    "+" "+a+" | "+b+" | "+c+" | "+d+" | "+e
 tabela[2][0] = " f | g | h | i | j    "+" "+f+" | "+g+" | "+h+" | "+i+" | "+j
 tabela[4][0] = " k | l | m | n | o    "+" "+k+" | "+l+" | "+m+" | "+n+" | "+o
 tabela[6][0] = " p | q | r | s | t    "+" "+p+" | "+q+" | "+r+" | "+s+" | "+t
 tabela[8][0] = " u | v | w | x | y    "+" "+u+" | "+v+" | "+w+" | "+x+" | "+y
 os.system("cls")
 print("*="*12)
 print(tabela[0][0])
 print(tabela[1][0])
 print(tabela[2][0])
 print(tabela[3][0])
 print(tabela[4][0])
 print(tabela[5][0])
 print(tabela[6][0])
 print(tabela[7][0])
 print(tabela[8][0])
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

def modo_mutiplayer_5_por_5(J1vsJ2, J2vsJ1):
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
 j = " "
 k = " "
 l = " "
 m = " "
 n = " "
 o = " "
 p = " "
 q = " "
 r = " "
 s = " "
 t = " "
 u = " "
 v = " "
 w = " "
 x = " "
 y = " "
 tabela = [[" a | b | c | d | e    "+" "+a+" | "+b+" | "+c+" | "+d+" | "+e],
          [" -----------------    "+" ------------------"],
          [" f | g | h | i | j    "+" "+f+" | "+g+" | "+h+" | "+i+" | "+j],
          [" -----------------    "+" ------------------"],
          [" k | l | m | n | o    "+" "+k+" | "+l+" | "+m+" | "+n+" | "+o],
          [" -----------------    "+" ------------------"],
          [" p | q | r | s | t    "+" "+p+" | "+q+" | "+r+" | "+s+" | "+t],
          [" -----------------    "+" ------------------"],
          [" u | v | w | x | y    "+" "+u+" | "+v+" | "+w+" | "+x+" | "+y]]
 resultado = "nada"
 jogador_1 = ""
 jogador_2 = ""
 controle = 0
 controle2 = 0
 vitorias = 0
 derrotas = 0
 vs = 0
 time = 1
 tabela[0][0] = " a | b | c | d | e    "+" "+a+" | "+b+" | "+c+" | "+d+" | "+e
 tabela[2][0] = " f | g | h | i | j    "+" "+f+" | "+g+" | "+h+" | "+i+" | "+j
 tabela[4][0] = " k | l | m | n | o    "+" "+k+" | "+l+" | "+m+" | "+n+" | "+o
 tabela[6][0] = " p | q | r | s | t    "+" "+p+" | "+q+" | "+r+" | "+s+" | "+t
 tabela[8][0] = " u | v | w | x | y    "+" "+u+" | "+v+" | "+w+" | "+x+" | "+y
 os.system("cls")
 print("*="*12)
 print(tabela[0][0])
 print(tabela[1][0])
 print(tabela[2][0])
 print(tabela[3][0])
 print(tabela[4][0])
 print(tabela[5][0])
 print(tabela[6][0])
 print(tabela[7][0])
 print(tabela[8][0])
 print("*="*12)
 while resultado == "nada":
  vs = vs + 1
  controle = 0
  if resultado == "nada":
   while controle != 1:
    time = time + 1
    print(f"Qual será a sua jogada", jogador1+"?",end="")
    jogador_1 = input()
    if jogador_1 == "a":
     if a != "O" and a!= "X":
      a = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "b":
     if b != "O" and b!= "X":
      b = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "c":
     if c != "O" and c!= "X":
      c = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "d":
     if d != "O" and d!= "X":
      d = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "e":
     if e != "O" and e!= "X":
      e = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "f":
     if f != "O" and f!= "X":
      f = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "g":
     if g != "O" and g!= "X":
       g = "X"
       controle = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
       print("essa posição já está ocupada")
    elif jogador_1 == "h":
     if h != "O" and h!= "X":
      h = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "i":
     if i != "O" and i!= "X":
      i = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "j":
     if j != "O" and j!= "X":
      j = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "k":
     if k != "O" and k!= "X":
      k = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "l":
     if l != "O" and l!= "X":
      l = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "m":
     if m != "O" and m!= "X":
      m = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "n":
     if n != "O" and n!= "X":
      n = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "o":
     if o != "O" and o!= "X":
      o = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "p":
     if p != "O" and p!= "X":
      p = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "q":
     if q != "O" and q!= "X":
      q = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "r":
     if r != "O" and r!= "X":
      r = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "s":
     if s != "O" and s!= "X":
      s = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "t":
     if t != "O" and t!= "X":
      t = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "u":
     if u != "O" and u!= "X":
      u = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "v":
     if v != "O" and v!= "X":
      v = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "w":
     if w != "O" and w!= "X":
      w = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "x":
     if x != "O" and x!= "X":
      x = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    elif jogador_1 == "y":
     if y != "O" and y!= "X":
      y = "X"
      controle = 1
      resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
     else:
      print("essa posição já está ocupada")
    else:
      print("Tente novamente")
      print("\n")
    tabela[0][0] = " a | b | c | d | e    "+" "+a+" | "+b+" | "+c+" | "+d+" | "+e
    tabela[2][0] = " f | g | h | i | j    "+" "+f+" | "+g+" | "+h+" | "+i+" | "+j
    tabela[4][0] = " k | l | m | n | o    "+" "+k+" | "+l+" | "+m+" | "+n+" | "+o
    tabela[6][0] = " p | q | r | s | t    "+" "+p+" | "+q+" | "+r+" | "+s+" | "+t
    tabela[8][0] = " u | v | w | x | y    "+" "+u+" | "+v+" | "+w+" | "+x+" | "+y
    os.system("cls")
    print("*="*12)
    print(tabela[0][0])
    print(tabela[1][0])
    print(tabela[2][0])
    print(tabela[3][0])
    print(tabela[4][0])
    print(tabela[5][0])
    print(tabela[6][0])
    print(tabela[7][0])
    print(tabela[8][0])
    print("*="*12)
  if resultado == "nada": 
   controle2 = 0
   while controle2 != 1:
     print("Qual será a sua jogada", jogador2+"?",end="")
     jogador_2 = input()
     if jogador_2 == "a":
      if a != "O" and a!= "X":
       a = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "b":
      if b != "O" and b!= "X":
       b = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "c":
      if c != "O" and c!= "X":
       c = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "d":
      if d != "O" and d!= "X":
       d = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "e":
      if e != "O" and e!= "X":
       e = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "f":
      if f != "O" and f!= "X":
       f = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "g":
      if g != "O" and g!= "X":
        g = "O"
        controle2 = 1
        resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
        print("essa posição já está ocupada")
     elif jogador_2 == "h":
      if h != "O" and h!= "X":
       h = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "i":
      if i != "O" and i!= "X":
       i = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "j":
      if j != "O" and j!= "X":
       j = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "k":
      if k != "O" and k!= "X":
       k = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "l":
      if l != "O" and l!= "X":
       l = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "m":
      if m != "O" and m!= "X":
       m = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
        print("essa posição já está ocupada")
     elif jogador_2 == "n":
       if n != "O" and n!= "X":
        n = "O"
        controle2 = 1
        resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
       else:
        print("essa posição já está ocupada")
     elif jogador_2 == "o":
      if o != "O" and o!= "X":
       o = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "p":
      if p != "O" and p!= "X":
       p = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "q":
      if q != "O" and q!= "X":
        q = "O"
        controle2 = 1
        resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "r":
      if r != "O" and r!= "X":
       r = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "s":
      if s != "O" and s!= "X":
       s = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "t":
      if t != "O" and t!= "X":
       t = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "u":
       if u != "O" and u!= "X":
        u = "O"
        controle2 = 1
        resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
       else:
        print("essa posição já está ocupada")
     elif jogador_2 == "v":
      if v != "O" and v!= "X":
       v = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "w":
      if w != "O" and w!= "X":
       w = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "x":
      if x != "O" and x!= "X":
       x = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     elif jogador_2 == "y":
      if y != "O" and y!= "X":
       y = "O"
       controle2 = 1
       resultado = comparar_5_por_5(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, vs)
      else:
       print("essa posição já está ocupada")
     else:
       print("Tente novamente")
       print("\n")
     tabela[0][0] = " a | b | c | d | e    "+" "+a+" | "+b+" | "+c+" | "+d+" | "+e
     tabela[2][0] = " f | g | h | i | j    "+" "+f+" | "+g+" | "+h+" | "+i+" | "+j
     tabela[4][0] = " k | l | m | n | o    "+" "+k+" | "+l+" | "+m+" | "+n+" | "+o
     tabela[6][0] = " p | q | r | s | t    "+" "+p+" | "+q+" | "+r+" | "+s+" | "+t
     tabela[8][0] = " u | v | w | x | y    "+" "+u+" | "+v+" | "+w+" | "+x+" | "+y
     os.system("cls")
     print("*="*12)
     print(tabela[0][0])
     print(tabela[1][0])
     print(tabela[2][0])
     print(tabela[3][0])
     print(tabela[4][0])
     print(tabela[5][0])
     print(tabela[6][0])
     print(tabela[7][0])
     print(tabela[8][0])
     print("*="*12)
 vencedor_2P(resultado, jogador1, jogador2)
 if resultado == "win":
  return "win"
 elif resultado == "lose":
  return "lose"

inicio()
