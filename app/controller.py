from django.contrib.auth import authenticate, login as loginProcess, logout
from django.conf import settings
import json
import os
import datetime

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
    path = os.path.join(settings.MEDIA_ROOT, 'json')
    name = 'group.json'

    if os.path.exists(os.path.join(path, name)):
        with open(os.path.join(path, name), 'r') as f:
            data = json.load(f)
            status = True
            message = 'Grupos carregados com sucesso!'
            containers = {
                'groups': data
            }
    else:
        status = False
        message = 'Nenhum grupo encontrado!'
        containers= {}

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

        if os.path.exists(os.path.join(path, name)):
            with open(os.path.join(path, name), 'r') as f:
                data = json.load(f)
                data.append(dict)
                with open(os.path.join(path, name), 'w') as f:
                    json.dump(data, f, indent=4)

        else:
            with open(os.path.join(path, name), 'w') as f:
                json.dump([dict], f, indent=4)
        
        status = True
        message = 'Grupo adicionado com sucesso!'

    else:
        status = False
        message = 'Nome do grupo não pode ser vazio!'
        if not os.path.exists(os.path.join(path, 'change.json')):
            with open(os.path.join(path, 'change.json'), 'w') as f:
                json.dump({}, f, indent=4)

        with open('change.json', 'r') as f:
            now = datetime.datetime.now()
            data = json.load(f)
            data['changed'] = now
            with open('change.json', 'w') as f:
                json.dump(data, f, indent=4)

    return{
        'status': status,
        'message': message,
        'containers': {}
    }
    
def view_group(data):
    data = load_json(data)
    id = data['id']
    path = os.path.join(settings.MEDIA_ROOT, 'json')
    name = 'group.json'

    if os.path.exists(os.path.join(path, name)):
        with open(os.path.join(path, name), 'r') as f:
            data = json.load(f)
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
    else:
        status = False
        message = 'Nenhum grupo encontrado!'
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

    if os.path.exists(os.path.join(path, name)):
        with open(os.path.join(path, name), 'r') as f:
            dt = json.load(f)
            for i in range(len(dt)):
                if dt[i]['id'] == id:
                    dt[i]['status'] = gstatus
                    dt[i]['name'] = gname
                    dt[i]['type'] = type
                    dt[i]['start'] = start
                    dt[i]['limit'] = limit
                    with open(os.path.join(path, name), 'w') as f:
                        json.dump(dt, f, indent=4)
                    status = True
                    message = 'Grupo atualizado com sucesso!'
                    containers = {
                        'group': dt[i]
                    }
                    break
                else:
                    status = False
                    message = 'Grupo não encontrado!'
                    containers = {}
    else:
        status = False
        message = 'Nenhum grupo encontrado!'
        containers = {}

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

    if os.path.exists(os.path.join(path, name)):
        with open(os.path.join(path, name), 'r') as f:
            dt = json.load(f)
            for group in dt:
                if group['id'] == id:
                    dt.remove(group)
                    with open(os.path.join(path, name), 'w') as f:
                        json.dump(dt, f, indent=4)
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
    else:
        status = False
        message = 'Nenhum grupo encontrado!'
        containers = {}
    
    return{
        'status': status,
        'message': message,
        'containers': containers
    }

def api_get_groups():
    path = os.path.join(settings.MEDIA_ROOT, 'json')
    name = 'group.json'
    with open(os.path.join(path, name), 'r') as f:
        data = json.load(f)
        status = True
        message = 'Grupos carregados com sucesso!'
        containers = {
            'groups': data
        }

    if not os.path.exists(os.path.join(path, 'change.json')):
        with open(os.path.join(path, 'change.json'), 'w') as f:
            json.dump({}, f, indent=4)

            with open(os.path.join(path, 'change.json'), 'r') as f:
                now = datetime.datetime.now()
                data = f
                data['changed'] = now
                with open('change.json', 'w') as f:
                    json.dump(data, f, indent=4)
    else:
        with open(os.path.join(path, 'change.json'), 'r') as f:   
            now = containers['changed']            
    
    containers['changed'] = now
    
    return{
        'status': status,
        'message': message,
        'containers': containers
    }