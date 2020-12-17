from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "TESTE SELENIUM"
        self.grupos_ou_pessoas = ["Lucas Pimenta"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(8)
        for grupo in self.grupos_ou_pessoas:
            # Seleciona o grupo
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(2)
            grupo.click()

            # Seleciona o campo para enviar mensagem
            chat_box = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(2)
            chat_box.click()
            chat_box.send_keys(self.mensagem)

            # Seleciona o botão enviar
            botao_enviar = self.driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")

            time.sleep(2)
            botao_enviar.click()
            time.sleep(1)


bot = WhatsappBot()
bot.EnviarMensagens()
