import imp
from bs4 import BeautifulSoup
# inicio mi clase como main 
def main():
    web=open('web.html','rb')
    #crearemos dos variables para almacenar los parametros del html
    inicio='<li>'

