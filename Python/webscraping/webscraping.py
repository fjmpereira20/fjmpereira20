from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#inicia o navegador
navegador = webdriver.Chrome()

#entra no site imdb.com
navegador.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')

navegador.minimize_window()


for i in range(1, 255):
    #find elements xpath
    filmes = navegador.find_elements('xpath','//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[1]/a/h3')
    
    #printa o nome dos filmes
    for filme in filmes:
        print(filme.text)

    ano_filme = navegador.find_elements('xpath','//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li['+str(i)+']/div[2]/div/div/div[2]/span[1]')

    #printa o ano dos filmes
    for ano in ano_filme:
        print(ano.text)


time.sleep(2)
