import random

#colores
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[39m'

print(CYAN + "Hola!")
print("Bienvenido a mi trivia! \n" + RESET)
name = input(BLUE + "Escribe tu nombre: " + RESET).capitalize()
print(CYAN + "Pondremos a prueba tus conocimientos sobre cultura general. \n" +
      RESET)
print(
    GREEN + name,
    ", te asignaremos un puntaje inicial aleatorio y conforme vayas acertando subirás tu puntaje!\n \nPero si te equivocas se te restarán puntos :/"
)
ask = input("Por favor, presiona 'enter' para asignar tu puntaje inicial: ")
score = random.randint(0, 5)
print("\n Genial, iniciarás con", score, "puntos :) \n")
print(
    BLUE + name,
    ", responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
    + RESET)

#preguntas
p1 = MAGENTA + "1)¿Cuál es el verdadero nombre de spiderman? \n" + RESET
p2 = MAGENTA + "2)¿Quien fue Atena? \n" + RESET
p3 = MAGENTA + "3)¿Que grupo terrorista ataca aún a todo el mundo? \n" + RESET
p4 = MAGENTA + "4)¿En que región está ubicado la 'LAGUNA 69'? \n" + RESET
p5 = MAGENTA + "5)Resuelve la siguiente operación: 3x4-2+13 \n" + RESET

print(p1)
print("a)Peter Parker")
print("b)Tom Holland")
print("c)Andrew Garfield")
ans1 = input("\nTu respuesta: ")
while ans1 not in ("a", "b", "c"):
    ans1 = input(
        RED + "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
        RESET)

if ans1 == "b":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
elif ans1 == "c":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
else:
    print(YELLOW + "\n Muy bien ⭐" + RESET)
    score += 10
    print("Tienes", score, "puntos.\n")

print(p2)
print("a)Diosa de la guerra")
print("b)Hija de Apolo")
print("c)Diosa de la sabiduría")
ans2 = input("\n Tu respuesta: ")
while ans2 not in ("a", "b", "c"):
    ans2 = input(
        RED + "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
        RESET)

if ans2 == "a":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
elif ans2 == "b":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
else:
    print(YELLOW + "\n Muy bien ⭐" + RESET)
    score += 10
    print("Tienes", score, "puntos.\n")

print(p3)
print("a)Klu klux klan")
print("b)Tifon")
print("c)Isis")
ans3 = input("\n Tu respuesta: ")
while ans3 not in ("a", "b", "c"):
    ans3 = input(
        RED + "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
        RESET)

if ans3 == "b":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
elif ans3 == "a":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
else:
    print(YELLOW + "\n Muy bien ⭐" + RESET)
    score += 10
    print("Tienes", score, "puntos.\n")

print(p4)
print("a)Lima")
print("b)Ancash")
print("c)Arequipa")
ans4 = input("\n Tu respuesta: ")
while ans4 not in ("a", "b", "c"):
    ans4 = input(
        RED + "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
        RESET)

if ans4 == "a":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
elif ans4 == "c":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
else:
    print(YELLOW + "\n Muy bien ⭐" + RESET)
    score += 10
    print("Tienes", score, "puntos.\n")

print(p5)
print("a)37")
print("b)23")
print("c)32)")
ans5 = input("\n Tu respuesta: ")
while ans5 not in ("a", "b", "c"):
    ans5 = input(
        RED + "Debes responder a, b o c. Ingresa nuevamente tu respuesta: " +
        RESET)

if ans5 == "a":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
elif ans5 == "c":
    print(RED + "\n Incorrecto!" + RESET)
    score -= 5
    print("Tienes", score, "puntos.\n")
else:
    print(YELLOW + "\n Muy bien ⭐" + RESET)
    score += 10
    print("Tienes", score, "puntos.\n")

print(GREEN + name, ", tienes en total", score, "puntos!" + RESET)