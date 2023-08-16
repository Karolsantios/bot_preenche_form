# passo a passo do projeto
    #https://dlp.hashtagtreinamentos.com/pyton/intensivo/login
# passo 1: Entrar no sistema da empresa
# passo 2: fazer login
# passo 3: importar a base de produtos pra cadastrar
# passo 4: cadastrar um produto
# passo 5: repetir o processo de cadastro até o fim
# pyautogui
#pyautogui.write -> escrever um texto
#pyautogui.press -> apertar uma tecla
#pyautogui.click -> clicar em algum lugar da tela
import pyautogui
import time

pyautogui.PAUSE = 0.3

# Abrindo o navegaor (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# fazer login
    #selecionar o campo de email
pyautogui.click(x=570, y=392)
# escrever email
pyautogui.write("pythonimpressionador@gmail.com")
# passa para o próximo campo
pyautogui.press("tab")
pyautogui.write("sua senha")
# clicar no botão login
pyautogui.click(x=681, y=542)
time.sleep(3)

# importando a baase de produtos para cadastrar
import pandas as pd

tabela = pd.read_csv("produtos2.csv")
print(tabela)

for linha in tabela.index:
    print(linha)
    pyautogui.click(x=891, y=274)
    #pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    #preencher o campo
    pyautogui.write(str(codigo))
    #passar para o próximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna("obs"):
        pyautogui.write(srt(tabela.loc[linha, 'obs']))
    # pyautogui.press("tab")
    pyautogui.press("enter")
    # scroll para voltar e repetir o procedimento
    pyautogui.scroll(5000)
    # repetir o processo de cadastro até o fim
