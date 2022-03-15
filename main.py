
import paises #Cris
import interfaz #Nico
import verificación #Daniel
import Findeljuego #Caro
import usuario #Pablo





def juego():

    print("Adivina una letra:")

    guess = usuario.input_usuario(input(),aciertos,errores) #(PABLO)

    ver = verificación.verificacion_jugada(guess,pais,aciertos,errores) #(DANIEL)


    if ver == 1:
        Findeljuego.findeljuegobueno()
        Findeljuego.contador(aciertos,errores)
        return (1)

    if ver == -1:
        Findeljuego.findeljuegomalo(pais)
        Findeljuego.contador(aciertos,errores)
        return (-1)

    print(interfaz.guiones(pais,aciertos))

    print(interfaz.fallado(errores))

    print("\n")
    print("\n")

while True:
    pais = paises.pais()
    largo = len(pais)
    aciertos = [" "]
    errores = []
    print(interfaz.guiones(pais,aciertos))
    while True:
        numero = juego()
        if (numero == -1) or (numero == 1):
            Findeljuego.volverajugar()
            break
        
