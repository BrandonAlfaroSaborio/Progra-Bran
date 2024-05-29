"""
programe un controlador que reciba del usuario un username (desde la consola)
y revise si dicho usuario exite en una lista de usuarios permitidos 
(que usted debe de crear y llenar). Si el usuario existe en la lista, debe de 
imprimir, que el usuario si tiene permiso de acceder al archivo, si no, debe imprimir
que no tiene permiso.

"""
lista=['Brandon','Agustin','Josue']
pregunta= input('Digite su usuario: \n')

if pregunta in lista :
    print('ud tiene permiso')

else:
    print('ud no tiene permiso')
