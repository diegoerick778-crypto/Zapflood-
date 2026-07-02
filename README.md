# ⚡ ZapFlood - Super Disparador de Notificações

<p align="center">
  <img src="https://shields.io" alt="Python Version">
  <img src="https://shields.io" alt="Selenium Version">
  <img src="https://shields.io" alt="Platform">
</p>

O **ZapFlood** é um script automatizado em Python utilizando **Selenium** para envio de notificações ou mensagens recorrentes no WhatsApp Web. Ele conta com uma interface colorida via terminal (ASCII Art) e sistemas de proteção humana (intervalos randômicos) para evitar o banimento da sua conta.

---

## 🚀 Funcionalidades

* 📱 **Envio Inteligente:** Digita e envia mensagens consecutivas sem precisar recarregar a página do WhatsApp Web.
* 🛡️ **Anti-Ban Avançado:** Pausas dinâmicas e randômicas entre os envios para simular o comportamento de digitação humana.
* ⏱️ **Pausa de Sanidade:** Intervalo longo de descanso automático a cada 10 mensagens disparadas.
* 🎨 **Terminal Customizado:** Visual inteiramente em verde clássico com logs detalhados de progresso em tempo real.

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:
* [Python 3](https://python.org)
* [Google Chrome](https://google.com) (Navegador oficial)

---

## 🔧 Instalação e Execução (Computador / Linux / Windows)

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd zapflood
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o script:**
   ```bash
   python zapflood.py
   ```

4. **Como usar:**
   * Digite o número com DDI e DDD (ex: `551199999999`).
   * Digite o texto da mensagem.
   * Defina a quantidade de disparos.
   * Uma janela do Chrome se abrirá. **Escaneie o QR Code** e deixe o robô trabalhar!

---

## 🤖 Uso no Android (Termux)

*Nota: Por limitações de arquitetura de processadores móveis, o Selenium padrão não abre interface gráfica no Termux.*

Para rodar em modo oculto (`headless`), siga o passo a passo:
```bash
pkg update && pkg upgrade -y
pkg install tur-repo -y
pkg install chromium-chromedriver -y
```
*Lembre-se de adaptar as opções do WebDriver no seu código para apontar para o binário do ChromeDriver instalado pelo Termux.*

---

## ⚠️ Aviso Legal (Disclaimer)

Este projeto foi desenvolvido estritamente para fins de estudos, automação de notificações e testes de estresse controlados. O uso indevido deste script para práticas de **SPAM** massivo viola os Termos de Serviço do WhatsApp. O desenvolvedor não se responsabiliza por eventuais suspensões ou banimentos de contas. Use com moderação e responsabilidade.

---
<p align="center">Desenvolvido com 💚 por mim</p>

# Zapflood-
# Zapflood-
