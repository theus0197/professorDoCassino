from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import controller

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        auth = {
            'user': request.user.username
        }
        return render(request, 'home/indexLogged.html', {
            'auth': auth,
            'manager': [],
        })
    else:
        return render(request, 'home/index.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.signin(data, request)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
def logout(request):
    if request.user.is_authenticated:
        response = controller.signout(request)
        print(response)
        if response['status']:
            return redirect('/')
    else:
        return redirect('/')

@csrf_exempt
def get_group(request):
    if request.method == 'POST':
        response = controller.get_groups()
        return render(request, 'home/manager/groups.html', {
            'groups': response
        })
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def add_group(request):
    if request.method == 'POST':
        return render(request, 'home/manager/add.html')
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def add_new_group(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.add_new_group(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def view_group(request):
    data = request.body.decode('utf-8')

    response = controller.view_group(data)
    return render(request, 'home/manager/edit.html', {
        'group': response
    })

@csrf_exempt
def update_group(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.update_group(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
    return JsonResponse(response)

@csrf_exempt
def delete_group(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.delete_group(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
    return JsonResponse(response)

@csrf_exempt
def api_get_groups(request):
    if request.method == 'POST':
        response = controller.api_get_groups()
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
    return JsonResponse(response)
