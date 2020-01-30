
VentaDolar = 6350
CompraDolar = 6310 #Factores de conversion
verificador = True #booleano para que funcione el programa
#Por comodidad hice los dos programas en un codigo

while(verificador == True ):
    key = input("Digite 0 si desea cambiar de USD a PYG, caso contrario digite 1 \n") #El usuario decide que tipo de conversion quiere hacer
    if (key.isnumeric() == True and int(key) == 0): #de USD a PYG con validacion de que se ingresa un numero
        dinero = input("Ingrese el monto en USD a cambiar: \n") #Monto a cambiar
        if (dinero.isnumeric() == True): #validacion de que se ingresa un int
            resultado = int(dinero) * CompraDolar #Convertido
            print("El monto equivale a", resultado, "PYG, que tenga un lindo dia") #Resultado en terminal
            verificador = False #se termina el programa ya que se realizo la conversion
        else: #mensaje de error
            print('No se ha ingresado un monto correcto, caracter invalido')    

    elif (key.isnumeric() == True and int(key) == 1): #de PYG a USD con validacion de que se ingresa un numero
        dinero = input("Ingrese el monto en PYG a cambiar \n") #Monto a cambiar
        if (dinero.isnumeric() == True): #validacion de que se ingresa int
            resultado = int(dinero) / VentaDolar #convertido
            print( "El monto equivale a ", resultado, "USD, que tenga un lindo dia") #resultado
            verificador = False #se termina el programa ya que se realizo la conversion
        else:
            print('No se ha ingresado un monto correcto, caracter invalido') #mensaje de error   

    else:
        print("Opcion incorrecta debe ingresar 0 o 1 \n") #mensaje de error           
