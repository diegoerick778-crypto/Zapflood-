from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse

# Códigos de cor ANSI para o terminal (Verde, Vermelho e Reset)
VERDE = "\033[92m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

# Logo ASCII do WhatsApp em verde
logo_ascii = f"""{VERDE}
               .---.        
              /     \\       

             |  {RESET}WA{VERDE}   |      
  .---.       \\     /       
 /     \\       '---'        

|  {RESET}ZAP{VERDE}  |                   
 \\     /                    
  '---'                     
{RESET}"""

print(logo_ascii)
print(f"{VERDE}[SISTEMA] Inicializando o super disparador de notificações...{RESET}\n")

# Recebe os dados de entrada do usuário
numero_alvo = input(f"{VERDE}Digite o número com DDD e DDI (ex: 5511999999999): {RESET}")
mensagem = input(f"{VERDE}Digite a mensagem de notificação: {RESET}")
qtd_mensagens = int(input(f"{VERDE}Quantas vezes quer enviar essa mensagem?: {RESET}"))

# Codifica a mensagem para o formato de URL
mensagem_codificada = urllib.parse.quote(mensagem)

# Inicializa o navegador
driver = webdriver.Chrome()

# Link oficial do WhatsApp Web com os parâmetros corretos
url = f"https://whatsapp.com{numero_alvo}&text={mensagem_codificada}"
driver.get(url)

print(f"\n{VERDE}[ALERTA] Por favor, escaneie o QR Code e aguarde a primeira conversa carregar...{RESET}")

try:
    # XPATH estrutural da caixa de texto do WhatsApp Web
    xpath_caixa_texto = '//div[@contenteditable="true"][@data-tab="10"]'
    
    # Aguarda dinamicamente o campo aparecer na tela pela primeira vez (até 45s por causa do QR Code)
    barra_de_envio = WebDriverWait(driver, 45).until(
        EC.presence_of_element_located((By.XPATH, xpath_caixa_texto))
    )
    
    # Envia a primeira mensagem que já veio preenchida pela URL
    barra_de_envio.send_keys(Keys.ENTER)
    print(f"{VERDE}[ENVIO] 1/{qtd_mensagens} enviado com sucesso!{RESET}")
    time.sleep(2)  # Pausa de segurança
    
    # Loop para enviar o restante das mensagens digitando direto na barra
    for i in range(2, qtd_mensagens + 1):
        # Digita o texto e aperta ENTER
        barra_de_envio.send_keys(mensagem)
        barra_de_envio.send_keys(Keys.ENTER)
        
        print(f"{VERDE}[ENVIO] {i}/{qtd_mensagens} enviado com sucesso!{RESET}")
        time.sleep(2)  # Evita o bloqueio por disparo muito rápido
        
    print(f"\n{VERDE}[SUCESSO] Todas as {qtd_mensagens} mensagens foram enviadas!{RESET}")
    
except Exception as e:
    print(f"\n{VERMELHO}[ERRO] Falha no disparo. O QR Code expirou ou a página perdeu a conexão.{RESET}")

# Tempo de respiro para garantir o processamento na rede antes de fechar
time.sleep(5)
driver.quit()
print(f"\n{VERDE}[SISTEMA] Processo encerrado. Navegador fechado.{RESET}")

