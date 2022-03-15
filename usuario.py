def input_usuario(letra_adivinada,aciertos,errores):
    x = 0
    while x == 0:
        if(len(letra_adivinada)!=1 or letra_adivinada.isnumeric()):
            print("Eso no es una letra intenta con una sola letra")
            letra_adivinada = input()

        else:
            if letra_adivinada.lower() in aciertos:
                print("Ya habias intentado con esa letra intenta con otra por favor")
                letra_adivinada = input()

            elif letra_adivinada.lower() in errores:
                print("Ya habias intentado con esa letra intenta con otra por favor")
                letra_adivinada = input()

            else:
                x = 1
    return letra_adivinada
