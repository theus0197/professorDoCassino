from django.contrib.auth import authenticate, login as loginProcess, logout
from django.conf import settings
import json
import os
import datetime
import ftplib
import requests

def ftp(file, name):
    server = ftplib.FTP()
    server.connect('31.170.160.95', 21)

    server.login('u403612333', 'Hz;gMM&0')
    #server.dir()

    #save file in path Frogti in server
    server.cwd('/domains/engenbot.com/public_html/VictoryTips')
    server.storbinary('STOR {}.json'.format(name), file)
    file.close()

def load_json(data):
    return json.loads(data)

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

def get_groups():
    response = requests.get('http://engenbot.com/VictoryTips/group.json')
    data = response.json()
    status = True
    message = 'Grupos carregados com sucesso!'
    containers = {
        'groups': data
    }

    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def add_new_group(data):
    data = load_json(data)

    #generate id with datetime
    now = datetime.datetime.now()
    id = now.strftime("%Y%m%d%H%M%S")
    status = data['status']
    name = data['name']
    type = data['type']
    start = data['start']
    limit = data['limite']

    if name != '':
        dict = {
            'id': id,
            'status': status,
            'name': name,
            'type': type,
            'start': start,
            'limit': limit
        }

        path = os.path.join(settings.MEDIA_ROOT, 'json')
        name = 'group.json'

        response = requests.get('http://engenbot.com/VictoryTips/group.json')
        data = response.json()
        data.append(dict)
        with open(os.path.join(path, name), 'w') as f:
                json.dump(data, f, indent=4)

        file = open(os.path.join(path, name), 'rb')
        ftp(file, name.replace('.json', ''))
        
        status = True
        message = 'Grupo adicionado com sucesso!'
    else:
        status = False
        message = 'Nome do grupo não pode ser vazio!'
            

    return{
        'status': status,
        'message': message,
        'containers': {}
    }
    
def view_group(data):
    response = requests.get('http://engenbot.com/VictoryTips/group.json')
    data = json.loads(data)
    id = data['id']
    data = response.json()
    for group in data:
        if group['id'] == id:
            status = True
            message = 'Grupo carregado com sucesso!'
            containers = {
                'group': group
            }
            break
        else:
            status = False
            message = 'Grupo não encontrado!'
            containers = {}

    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def update_group(data):
    data = load_json(data)
    id = data['id']
    gstatus = data['status']
    gname = data['name']
    type = data['type']
    start = data['start']
    limit = data['limite']

    path = os.path.join(settings.MEDIA_ROOT, 'json')
    name = 'group.json'

    response = requests.get('http://engenbot.com/VictoryTips/group.json')
    dt = response.json()
    for i in range(len(dt)):
        if dt[i]['id'] == id:
            dt[i]['status'] = gstatus
            dt[i]['name'] = gname
            dt[i]['type'] = type
            dt[i]['start'] = start
            dt[i]['limit'] = limit
            with open(os.path.join(path, name), 'w') as f:
                json.dump(dt, f, indent=4)
            file = open(os.path.join(path, name), 'rb')
            ftp(file, name.replace('.json', ''))
            status = True
            message = 'Grupo atualizado com sucesso!'
            containers = {
                'group': dt[i]
            }
            break
        else:
            status = False
            message = 'Grupo não encontrado!'

    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def delete_group(data):
    data = load_json(data)
    id = data['id']
    path = os.path.join(settings.MEDIA_ROOT, 'json')
    name = 'group.json'

    '''if os.path.exists(os.path.join(path, name)):
        with open(os.path.join(path, name), 'r') as f:'''
    response = requests.get('http://engenbot.com/VictoryTips/group.json')
    dt = response.json()
    for group in dt:
        if group['id'] == id:
            dt.remove(group)
            with open(os.path.join(path, name), 'w') as f:
                json.dump(dt, f, indent=4)

            file = open(os.path.join(path, name), 'rb')
            ftp(file, name.replace('.json', ''))
            status = True
            message = 'Grupo removido com sucesso!'
            containers = {
                'group': group
            }
            break
        else:
            status = False
            message = 'Grupo não encontrado!'
            containers = {}
    
    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def api_get_groups():
    response = requests.get('http://engenbot.com/VictoryTips/group.json')
    data = response.json()
    status = True
    message = 'Grupos carregados com sucesso!'
    containers = {
        'groups': data
    }
    
    return{
        'status': status,
        'message': message,
        'containers': containers
    }
