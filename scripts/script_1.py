#imagina que quieres desempacar una lista en variables 
lista=['hola', ' como', 'estas']
#case 1
var_1=lista[0]
#case 2
var_2 = ""
for i in lista:
    var_2 = i
    break
#case 3
var_2, *_= lista
#case 4
_, var_2, _ = lista