from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random

#--------------     FUNCIONES

def solicitudHastags():
    diccionario = dict()
    hastag = ""
    veces = 0

    bucle = True

    while (bucle):
        hastag = input("Introduce hastag a recorrer o introduce -1 para terminar de introducir valores: ")

        if hastag == "-1":
            bucle = False
        else:
            while veces <= 0:
                veces = int(input("Introduce el numero de publicaciones de este hastag que quieres recorrer: "))
            diccionario[hastag] = veces
            veces = 0
    
    return diccionario


def solicitaMensajes():
    mensajes = ["Qué guay!", "Muy interesante", "Buen contenido", "Buena publicación"]
    eleccion = 0
    mensajeEleccionPersonalizada = ""

    print("Tienes una lista con los siguientes mensajes predeterminados: ")
    print(mensajes)

    while (eleccion != 1) and (eleccion != 2):
        print("Qué prefieres?:\n1. Utilizar los mensajes predeterminados.\n2. Crear tus propios mensajes automáticos [RECOMENDADO].")
        eleccion = int(input("OPCION: "))
    
    if eleccion == 2:
        mensajes = []

        while mensajeEleccionPersonalizada != "-1":
            mensajeEleccionPersonalizada = input("Introduce mensaje (o -1 para terminar de introducir): ")

            if (mensajeEleccionPersonalizada != "-1"):
                mensajes.append(mensajeEleccionPersonalizada)
    
    return mensajes


def recorreUnHastag(hastag, veces, mensajes):
    driver.get("https://www.instagram.com/explore/tags/" + hastag)
    sleep(4)

    primeraPubli = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]')
    primeraPubli.click()
    sleep(2)

    for i in range(veces):
        try:
            corazon = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]')
            corazon.click()
            sleep(random.randint(1,2))
        except:
            pass
        
        try:
            botonDialogo = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button/div[2]')
            botonDialogo.click()
            sleep(1)

            texto = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
            texto.send_keys(mensajes[random.randint(0, len(mensajes)-1)])

            enviar = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button/div')
            enviar.click()
        except:
            pass

        sleep(random.randint(4,8))

        pestana = driver.find_element_by_xpath('/html/body')
        if i != veces-1:    pestana.send_keys(Keys.RIGHT)

        sleep(random.randint(1,4))


#--------------------------------------------------- MAIN -----------------------------------------
#-------------- CREDENCIALES


user = input("Introduce tu email o nombre de cuenta: ")
contrasena = input("Introduce tu contraseña: ")
print("\n\n")
diccionario = solicitudHastags()
print("\n")
mensajes = solicitaMensajes()
print("\n")

#--------------

#-------------- ACCESO
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.instagram.com")
sleep(2)

cookies_button = driver.find_element_by_xpath("/html/body/div[4]/div/div/button[2]")
cookies_button.click()
sleep(1)

username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(user)
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(contrasena)
login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()

sleep(7)

boton_seguro = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
boton_seguro.click()

sleep(2)

boton_notificaciones = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
boton_notificaciones.click()

sleep(2)

# ---- FUNCION DE RECORRIDO DE HASTAGS

for i in diccionario.keys():
    recorreUnHastag(i, diccionario[i], mensajes)

driver.close()