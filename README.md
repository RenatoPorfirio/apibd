# apibd

Autor: Renato Porfirio Santos Xavier

#Dependencias:

A aplicação trabalha com servidores postgresql, portanto, é necessário que haja um servidor para conectar-se.
Módulos python necessários:
  
=> pyscopg2 (módulo para trabalhar com o postgresql - ver documentação em https://www.psycopg.org/docs/)
comando de instalação: pip install psycopg2
                          ou
                       pip install psycopg2-binary

=> flask (módulo responsável pelo servidor http - ver documentação em https://flask.palletsprojects.com/en/2.2.x/0)
comando de instalação: pip install flask
 
#Funcionamento
A aplicação contém três arquivos auxiliares: dbconfig.txt, help.txt, index.html
=>dbconfig.txt: Responsável pelas configurações de conexão com o banco de dados.
                - HOST: representa o endereço do host que hospeda o banco de dados;
                - USER: nome de usuário do banco de dados (padrão: postgres);
                - PSWD: senha para conectar-se ao banco de dados;
                - NAME: nome do banco de dados que deseja conectar-se;
=>help.txt    : Texto do menu de ajuda da ferramenta;
=>index.html  : Homepage do servidor da API, onde é possível testar o seu funcionamento;
 ######################################################################################
 O arquivo principal da aplicação é o apistart.py. Este, importa todos os módulos e arquivos necessários para o correto funcionamento.
 Para saber como utilizar a ferramenta, abra o arquivo help.txt ou execute o comando:
 python3 apistart.py --help
 
 NOTA:As requisições são processadas no link: http://ec2-34-203-132-2.compute-1.amazonaws.com:5000/req.
      Em http://ec2-34-203-132-2.compute-1.amazonaws.com:5000, é possível acessar a homepage (index.html) para consultar ou adicionar dados.
