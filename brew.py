'''
BlinkBrew
Author is BlinkHub Development Team.
Copyright (C) 2017. Blinkhub Inc.
'''
import argparse #Библиотека для передачи аргументов при запуске скрипта
import os #Библиотека для взаимадействия с системой
import requests #Библиотека для отправки запросов в сеть
import wget #Библиотека для загрузки файлов
parser = argparse.ArgumentParser() #Какая-то фигня которая позваляет всему начать работать, без нее никак
parser.add_argument("-i", "--install", help="Install blink-packages for system.", type=str) #Добавляю аргумент -i либо --install с текстом помощи help и функция type которая принемает данные типа str
args = parser.parse_args() #Еще одна какая-то важная фигня
if args.install: #Если вызван аргумент install командой -i или --install
    print("Getting " + args.install + "...") #Вывод сообщения про получении данных о пакете, а args.install содержит переданный текст, в данном случае название пакета
    if os.path.exists("Homebrew/" + args.install) != True: #Проверка если папка с именим этого пакета не существует по пути Homebrew/
        if requests.head("http://dev.blinkhub.ru/homebrew/packages/" + args.install + ".bpkg").status_code == requests.codes.ok:  #Проверка на наличее требуемого пакета на сервере
            print("Downloading " + args.install + "...") #Вывод сообщения о загрузке
            wget.download("http://dev.blinkhub.ru/homebrew/packages/" + args.install + ".bpkg", "Homebrew/") #Загрузить файл через библиотеку wget в папку Homebrew/
        else: #Если такого файла не существует на сервере
            print("Package " + args.install + " not found on server.") #Вывод сообщения о том что файл не найден
    else: #Если папка с названием пакета по пути Homebrew/ уже существует
        print("Package " + args.install + " already installed.") #Вывод сообщения о том что пакет уже установлен
