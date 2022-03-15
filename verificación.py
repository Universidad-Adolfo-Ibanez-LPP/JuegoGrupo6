def verificacion_jugada (input_usuario, pais, aciertos, errores):

  if input_usuario in pais: #acierto
      print("Esta letra pertenece al pais")
      aciertos.append(input_usuario)

      if len(aciertos) > len(set(pais)): #victoria
        return 1

  else: #fallo
      print("Esta letra NO pertenece al pais")
      errores.append(input_usuario)

      if len(errores)>=5: #derrota, el 5 es arbitrario
        return -1
