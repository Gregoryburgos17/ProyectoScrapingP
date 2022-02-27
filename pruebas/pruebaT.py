

# inicio mi clase como main 
def main():
    web=open('pruebas/web.html','rb')
    #crearemos dos variables para almacenar los parametros del html

    inicio='<li>' # si sustituyo td puedo encontra la informacion necesaria
    fin ='</li>' 

    # vamos a leerlo por lineas para buscar la lista

    for linea in web.readlines():
        linea=str(linea)

        #filtramos de la siguiente manera 
        #con esto lograremos traer el contenido de las paginas web

        if inicio in linea:
            #colocaremos una condicion para seguir filtrando
            #if not elimina aquellas letras inecesarias,

            if  not '<a href' in linea:
                 # ahora vamos a buscar la etiqueta que empieza con li de lista

                 x=linea.find(inicio)
                 x= x + len(inicio)
                 y=linea.find(fin)
                #le estamo diciendo que imprima desde x a y 
                
                 print(linea[x:y])
        


if __name__=='__main__':
    main()
