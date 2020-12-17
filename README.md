# MensagensWpp
Teste de envio de mensagens no whatsapp utilizando o Selenium

## ATENÇÃO: o WebDriver varia de acordo com o SO e o browser utilizado. Este projeto está utilizando o Chrome.

Para download compatível com a versão do seu Chrome, acesse https://chromedriver.chromium.org/downloads e extraia o chromedriver na mesma pasta do projeto.

Adeque o atributo 'self.driver' colocando o nome correto do chromedriver.

### O nome da classe do 'chat_box' pode variar. Saiba qual o correto Inspecionando o elemento (F12).

### O xPath do elemento 'botao_enviar' pode variar. Saiba qual o correto Inspecionando o elemento (F12) -> Botão direito -> Copy -> Full xPath.

## Execução

No arquivo 'main.py':

1) Insira a mensagem a ser enviada no atributo 'self.mmensagem'.

2) Insira o(s) grupo/pessoa no atributo 'self.grupos_ou_pessoas'. Exemplo: ['eu', 'mae', 'pai'] .

3) Execute o script. O navegador irá abrir na tela do WhatsApp Web, onde você terá que scannear o QR code.

Os métodos 'time.sleep(x)' indicam o atraso em segundos que será aguardado.

4) Aguarde a execução automatizada terminar.
