import urllib.request
#abrimos un archivo 
web=open('pruebas/Funcionario.html','wb')
#luego realizamos una consulta
consulta=urllib.request.urlopen('https://map.gob.do/DirectorioFuncionarios/consulta/index')
#luego leer la consulta 
consulta= consulta.read()
#luego lo que hemos lo leido lo guardamos en web
web.write(consulta)
web.close()