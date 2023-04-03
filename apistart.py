import sys
import json
import psycopg2
from flask import Flask, request, make_response

#DEF=====================================================================================

def db_get(cpf):
    con.commit()
    cur = con.cursor()
    cur.execute('select * from usuario where cpf = \''+ cpf +'\';')
    con.commit()
    usuario = cur.fetchall()
    if usuario:
        [(nome, cpf, data_nascimento)] = usuario
        dic = {
            'nome': nome,
            'cpf': cpf,
            'data_nascimento': data_nascimento.strftime('%d/%m/%Y')
        }
        response = make_response(json.dumps(dic, indent=4).encode('utf-8'))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200
    else:
        response = make_response('Usuário não encontrado na base de dados!')
        response.headers['Content-Type'] = 'text/plain'
        response.status_code = 204
    
    cur.close()
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

def db_insert(nome, cpf, data_nascimento):
    con.commit()
    cur = con.cursor()
    try:
        cur.execute("insert into usuario (nome,cpf,data_nascimento) values ('{n:s}','{c:s}','{d:s}');".format(n=nome, c=cpf, d=data_nascimento))
    except:
        cur.close()
        return 'USUARIO JÁ EXISTENTE', 204
    con.commit()
    cur.close()
    return 'SUCESSO', 200

HTMLHOME = ''
with open('index.html', 'r') as f:
    HTMLHOME += f.read()

#ROUTES====================================================================================

app = Flask(__name__)
con = None

@app.after_request
def add_header(response):
    response.headers['Acess-Control-Allow-Origin'] = '*'
    return response

@app.route('/')
def homepage():
	return HTMLHOME

@app.route('/req', methods=['GET','POST'])
def req():
    if request.method == 'GET':
        return db_get(request.args.get('cpf'))
    else:
        dic = request.form
        return db_insert(dic['nome'], dic['cpf'], dic['data_nascimento'])

#RUN======================================================================================

if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    with open('help.txt','r') as h:
        print(h.read())
    exit()
else:
    try:
        INFO = {}
        with open('dbconfig.txt', 'r') as conf:
            tmp = conf.readline().split()
            INFO[tmp[0]] = tmp[1]
            tmp = conf.readline().split()
            INFO[tmp[0]] = tmp[1]
            tmp = conf.readline().split()
            INFO[tmp[0]] = tmp[1]
            tmp = conf.readline().split()
            INFO[tmp[0]] = tmp[1]
        con = psycopg2.connect(user=INFO['USER'], password=INFO['PSWD'], database=INFO['NAME'], host=INFO['HOST'])
        app.run(sys.argv[1], sys.argv[2])
        con.close()
    except Exception as e:
        print('Problema na execução! Digite python3 apistart.py --help para informações sobre o uso correto.')
