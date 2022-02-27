def main():
    files=open('pruebas/web.html','rb')
    inicio='<title>'
    fin='</title>'

    for l in files.readlines():
        l = str(l)
        if inicio in l:
            x=l.find(inicio)
            x= x+ len(inicio)
            y=l.find(fin)
            print(l[x:y])


    
#ojo con la palabra main que dentro de estos coyetes simples
if __name__ =='__main__':
    main()