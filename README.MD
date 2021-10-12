# Exemplos de uso do micropython: conexão com a rede
# Apelido do projeto: watcher spider

## Para rodar

### Configurando ESP32

  * Para instalar o micropython na ESP32, foi usado esse tutorial como base: https://youtu.be/ApOwrmX0TB0
  * Para configurar o VSCode como plataforma de desenvolvimento, foi usado este outro tutorial: https://youtu.be/hNcamK6_TcU

### Baixe este repositório

  * Após clonar esse repositório, é preciso enviá-lo para a sua esp, isso pode ser feito usando os seguintes comandos 
  '''
        ampy --port COM5 put path_to/model
        ampy --port COM5 put path_to/service
        ampy --port COM5 put path_to/view
        ampy --port COM5 put path_to/main.py /main.py
        ampy --port COM5 run main.py
  '''

  * Por via de preferência, eu executo esses comandos usando um RUN.bat (existe algo semelhante para o linux, mas no momento não me recordo como fazer), esse aruqivo .bat executa todos os comandos acima desde que esteja sendo executando à partir do caminho certo para garantir que encontre os arquivos deste projeto

  * Deixarei o meu arquiv RUN.bat como exemplo
## Referências usadas

### Micropython

  * Documentação oficial:  http://docs.micropython.org/en/latest/
  * Manual básico de micropython pela Adafruit: https://cdn-learn.adafruit.com/downloads/pdf/micropython-basics-load-files-and-run-code.pdf
  * Playlist de minicurso no YouTube: https://www.youtube.com/playlist?list=PLtcOfE9KWB64xDnedRcPJ5d35FkMB4A-g

### ESP

  * Como instalar micropython na esp32 : https://youtu.be/ApOwrmX0TB0
  * Como usar o VSCode como plataforma de desenvolvimento micropython: https://youtu.be/hNcamK6_TcU


### MVC

para este projeto tentei aplicar uma estrutura de MVC contendo apenas os diretórios model, service, utils e view, e com o arquivo main.py que chama todo o código

#### Model

 * Onde estão as declarações das classes que serão usadas como base, aqui está a parte mais paupável do projeto, tanto que fica intuitivo até mesmo pelo nome das mesmas
 
#### Service

  * Aqui que temos a classe que irá gerenciar as classes do model e que também irá responder às requisições feias pela view

#### Utils

  * Ainda vazia

#### View

  * Aqui encontra-se toda a parte visual e que o usuário final tem acesso. Nesse projeto não existe input, mas as saídas todas elas, seja por led, seja por print, são mostradas através daqui ou em alguns casos, é daqui que sai a chamada para as classes que realizarão esse output

### Outras