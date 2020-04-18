import datetime

#Funcion encabezado

def encabezadoHtml(html,nombreF):
    html.write("<!DOCTYPE html >\n"
               "<html>\n"
               "<head>\n"
               "\t<title> Titulo <title>\n"
               "\t<link href=\"" + nomFile + ".css\" rel=\"stylesheet\">\n"
               "<head>\n"
               "<body>\n"
               "\t<table>\n")

def cuerpoHtml(html):
    html.write("\t</table>\n"
               "</body>\n"
               "</html>")

#info en html
def infoCeldas(html, info, i, numCeldas):
    html.write("\t\t\t<td>")
    if i == numCeldas -1:
        info = info[:-1]
        html.write(info)
    else:
        html.write(info)
    html.write("</td>\n")

#Crear estructura tabla
def tabla(fi, html):
    line = fi.readline()

    if line == "":
        return False

    celdas = line.split("\t")
    numCeldas = len(celdas)

    html.write("\t\t<tr>\n")
    for i in range(numCeldas):
        infoCeldas(html,celdas[i], i, numCeldas)
    html.write("\t\t</tr>\n")

    return True

check = True
nombreF = input("Introduce el nombre del fichero sin extensión\n")
rutaF = open ("/home/maitechu/PycharmProjects/MNFicheros1")
datetime.datetime.now()

try:
    log = open(rutaF + "log.txt", 'a')
    log.write(str(datetime.datetime.now())+"Fichero log abierto ok.\n")
except:
    print("Error creando fichero Log")
    check = False