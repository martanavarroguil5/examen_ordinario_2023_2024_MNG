'''
Defino las variables'''
tiempo_carslen = 180
tiempo_nakamura = 180

'''
Cuando juega Carslen le quitan tiempo'''
def jugada_carslen(tiempo_carslen):
    tiempo_carslen = tiempo_carslen - 10
    
def jugada_nakamura(tiempo_nakamura):
    tiempo_nakamura = tiempo_nakamura -10

    
turno = input("De quién quieres que sea el turno? C/N ")


if turno == "C":
    def jugada_carslen():
elif turno == "N":
    def jugada_nakamura():
else:



