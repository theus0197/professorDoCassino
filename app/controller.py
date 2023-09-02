from django.contrib.auth import authenticate, login as loginProcess, logout
from django.conf import settings
import json
import os
import datetime
import ftplib
import requests
from . import models

if settings.DEBUG:
    host = '127.0.0.1:8000'
    url = 'http://{}/media/json'.format(host)
else:
    host = ''
    url = 'http://{}/BotMilionario'.format(host)

def ftp(file, name):
    if settings.DEBUG is False:
        server = ftplib.FTP()
        server.connect('31.170.160.95', 21)

        server.login('u403612333', 'Hz;gMM&0')
        #server.dir()

        #save file in path Frogti in server
        server.cwd('/domains/engenbot.com/public_html/VictoryTips')
        server.storbinary('STOR {}.json'.format(name), file)
        file.close()

def load_json(data):
    try:
        data = json.loads(data)
    except:
        data = []

    return data

def method_not_allowed():
    return {
        'status': False,
        'message': 'Método não autorizado!',
        'containers': {}
    }

def signin(data, request):
    data = load_json(data)
    username = data['username']
    password = data['password']
    print(data)
    user = authenticate(username=username, password=password)
    if user is not None:
        loginProcess(request, user)
        status = True
        message = 'Login realizado com sucesso!'
    else:
        status = False
        message = 'Autenticação inválida!'

    return {
        'status': status,
        'message': message,
        'containers': {}
    }

def signout(request):
    logout(request)
    return {
        'status': True,
        'message': 'Logout realizado com sucesso!',
        'containers': {}
    }

def get_clients():
    clients = models.Clients.objects.all()
    status = True
    message = 'Clientes carregados com sucesso!'
    containers = {
        'clients': clients
    }

    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def add_new_client(data):
    data = load_json(data)
    id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    name = data['name']
    cpf = data['cpf'].replace(' ', '')
    email = data['email']
    roleta_evo = True if data['roleta-evo'] == 'true' else False
    roleta_playtech = True if data['roleta-playtech'] == 'true' else False
    dados = True if data['dados'] == 'true' else False
    football_studio = True if data['football-studio'] == 'true' else False
    football_dice = True if data['football-dice'] == 'true' else False

    if name != '':
        if cpf != '':
            if models.Clients.objects.filter(cpf=cpf).exists():
                status = False
                message = 'Esse usuário já está cadastrado!'
            else:
                new_client = models.Clients(
                    id=id,
                    name=name,
                    cpf=cpf,
                    email=email,
                    roleta_evo=roleta_evo,
                    roleta_playtech=roleta_playtech,
                    dados=dados,
                    football_studio=football_studio,
                    football_dice=football_dice
                )
                new_client.save()
                status = True
                message = 'Grupo adicionado com sucesso!'
        else:
            status = False
            message = 'CPF do client não pode estar vazio!'
    else:
        status = False
        message = 'Nome do cliente não pode estar vazio!'
            

    return{
        'status': status,
        'message': message,
        'containers': {}
    }
    
def view_client(data):
    data = load_json(data)
    id_ = data['id']
    if models.Clients.objects.filter(id=id_).exists():
        status = True
        message = 'Usuário encontrado com sucesso!'
        user = models.Clients.objects.get(id=id_)
        containers = {
            'client': {
                'id': user.id,
                'name': user.name,
                'cpf': user.cpf,
                'email': user.email,
                'roleta_evo': 'true' if user.roleta_evo is True else 'false',
                'dados': 'true' if user.dados is True else 'false',
                'roleta_playtech': 'true' if user.roleta_playtech is True else 'false',
                'football_dice': 'true' if user.football_dice is True else 'false',
                'football_studio': 'true' if user.football_studio is True else 'false',
                'blaze': 'true' if user.bet_blaze is True else 'false',
                'estrelabet': 'true' if user.bet_estrelabet is True else 'false',
                'brxbet': 'true' if user.bet_brxbet is True else 'false',
                'betano': 'true' if user.bet_betano is True else 'false',
                'saurobet': 'true' if user.bet_saurobet is True else 'false'
            }
        }
    else:
        status = False
        message = 'Esse não está cadastrado'
        containers = {}
        

    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def update_client(data):
    data = load_json(data)
    id_ = data['id']
    name = data['name']
    cpf = data['cpf']
    email = data['email']
    roleta_evo = True if data['roleta-evo'] == 'true' else False
    roleta_playtech = True if data['roleta-playtech'] == 'true' else False
    dados = True if data['dados'] == 'true' else False
    football_studio = True if data['football-studio'] == 'true' else False
    football_dice = True if data['football-dice'] == 'true' else False
    bet_blaze = True if data['blaze'] == 'true' else False
    bet_estrelabet = True if data['estrelabet'] == 'true' else False
    bet_brxbet = True if data['brxbet'] == 'true' else False
    bet_betano = True if data['betano'] == 'true' else False
    bet_saurobet = True if data['saurobet'] == 'true' else False

    if models.Clients.objects.filter(id=id_).exists():
        status = True
        message = 'Usuário encontrado com sucesso!'
        user = models.Clients.objects.get(id=id_)
        user.name = name
        user.cpf = cpf
        user.email = email
        user.roleta_evo = roleta_evo
        user.roleta_playtech = roleta_playtech
        user.dados = dados
        user.football_studio = football_studio
        user.football_dice = football_dice
        user.bet_blaze = bet_blaze
        user.bet_estrelabet = bet_estrelabet
        user.bet_brxbet = bet_brxbet
        user.bet_betano = bet_betano
        user.bet_saurobet = bet_saurobet

        user.save()
    else:
        status = False
        message = 'Usuário não encontrado'


    return{
        'status': status,
        'message': message,
        'containers': {}
    }

def delete_client(data):
    data = load_json(data)
    id_ = data['id']

    if models.Clients.objects.filter(id=id_).exists():
        user = models.Clients.objects.get(id=id_)
        user.delete()
        status = True
        message = 'Usuário removido com sucesso!'
    else:
        status = False
        message = 'Usuário não encontrado'
    
    return{
        'status': status,
        'message': message,
        'containers': {}
    }

def api_get_clients(data):
    data = load_json(data)
    print(data)
    cpf = data['cpf']
    if cpf != '':
        if models.Clients.objects.filter(cpf=cpf).exists():
            user = models.Clients.objects.get(cpf=cpf)
            status = True
            message = 'Olá {}, seu acesso foi liberado ;)'
            containers = {
                'name': user.name,
                'email': user.email,
                'dados': user.dados,
                'roleta_evo': user.roleta_evo,
                'roleta_playtech': user.roleta_playtech,
                'football_dice': user.football_dice,
                'football_studio': user.football_studio,
                'blaze': user.bet_blaze,
                'estrelabet': user.bet_estrelabet,
                'brxbet': user.bet_brxbet,
                'betano': user.bet_betano,
                'saurobet': user.bet_saurobet
            }
        else:
            status = False
            message = 'Infelizmente seu acesso ainda não está liberado, contate o suporte!'
            containers = {}
    else:
        status = False
        message = 'Preencha o campo CPF para verificar se você possui acesso!'
        containers = {} 
    
    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def authorized_app(data):
    data = load_json(data)
    cpf = data['cpf']
    game = data['game']
    if cpf != '':
        if models.Clients.objects.filter(cpf=cpf).exists():
            user = models.Clients.objects.get(cpf=cpf)
            if game == 'roleta':
                status_game = True if user.roleta else False
            elif game == 'dados':
                status_game = True if user.dados else False
            elif game == 'football-studio':
                status_game = True if user.football_studio else False
            elif game == 'football-dice':
                status_game = True if user.football_dice else False
            elif game == 'roleta-evo':
                status_game = True if user.roleta_evo else False
            elif game == 'roleta-playtech':
                status_game = True if user.roleta_playtech else False
            else:
                status_game = False
            status = True
            message = 'Condição do game foi coletada com sucesso!'
            containers = {
                'status_game': status_game, 
                'blaze': user.bet_blaze,
                'estrelabet': user.bet_estrelabet,
                'brxbet': user.bet_brxbet,
                'betano': user.bet_betano,
                'saurobet': user.bet_saurobet

            }
        else:
            status = False
            message = 'Infelizmente seu acesso ainda não está liberado, contate o suporte!'
            containers = {}
    else:
        status = False
        message = 'Preencha o campo CPF para verificar se você possui acesso!'
        containers = {} 

    return {
        'status': status,
        'message': message,
        'containers': containers
    }


