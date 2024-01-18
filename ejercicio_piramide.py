'''
Primero defino una variable que defina la altura de la pirámide y su valor va a ser la entrda del usiario'''
altura_piramide = input("Escriba cuántos niveles quiere que tenga su pirámide " )

'''
Esta función evalúa si la altura de dicha pirámide es válida.'''
def altura_valida(altura_piramide):
     
     while True: 
        entrada = input(altura_piramide) 
        try: 
            entrada  = int(entrada) 
        except: 
            altura_piramide = input("Escriba cuántos niveles quiere que tenga su pirámide " )
            pass 
        else: 
            if 1 <= entrada: 
                break 
    

altura_piramide = altura_valida(altura_piramide)

altura_piramide = int(altura_piramide) 
altura_piramide = altura_piramide + 1 # le añadimos un uno a la altura para wue entre en el rango.
'''
Creo un buvlea que se va a repetir tantas veces el usuario haya indicado'''
for nivel in range(1, altura_piramide):
    nivel = int(nivel) # El nivel que se esté evaluando que son desde el 1 hasta la altura indicada
    asteriscos = nivel*2 - 1 # Como cada nivel debe tener dos estrellas mas que el anteriorr, esta es su fórmula
    repeticion = "*"*asteriscos # Se repetira una cadena de asteriscos las veces indicadas anteriormente
    print (repeticion.center(50, " ")) # Método para que se imprima centraloizado