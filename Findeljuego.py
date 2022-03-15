def findeljuegobueno(): 
   print('¡Ganaste! Encontraste el país oculto, felicitaciones')
        
def findeljuegomalo(): 
  print(f'¡Perdiste! El país que debías encontrar era {país}')

def volverajugar():
return input ('Si deseas jugar de nuevo presiona ENTER: ')

def contador(aciertos,errores):
  return print(f"Te demoraste {len(aciertos) + len(errores) - 1} intentos")
