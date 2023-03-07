import hashlib

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        contact = request.POST['contact']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        np = hashlib.md5(password.encode('utf')).hexdigest()
        np_cnfirm = hashlib.md5(confirm_password.encode('utf')).hexdigest()

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Taken')
                return redirect('/register/')
            else:
                user = User.objects.create(username=username, password=np, email=email, contact=contact,
                                           firstname=first_name,lastname=last_name, confirm_password=np_cnfirm )
                user.save()
                print('user created')
                return redirect('/login/')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/register/')


    else:
        return render(request, 'sign-up.html')


def login(request):
    if request.method == 'POST':
        e = request.POST.get('username')
        p = request.POST.get('password')

        val = User.objects.filter(username=e, password=p).count()

        if val == 1:
            data = User.objects.filter(username=e, password=p)
            for items in data:
                request.session['username'] = items.username
                request.session['id'] = items.id
                return redirect('/index/')

        else:
           messages.error(request, 'Invalid username and password')
        return render(request, 'sign-in.html')
    else:

        return render(request, 'sign-in.html')


def logout(request):
    try:
        del request.session['id']

    except:
        pass

    return redirect('/index/')

# add files for product

#ajax with crud
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# def create_user(request):
#     # if request.method == "POST":
#     #     form = UserForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #     else:
#     #         pass
#     form = UserForm()
#     user = User.objects.all()
#     return render(request, 'index.html', {'form': form, 'user': user})
#
#
# @csrf_exempt
# def add_user(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             uid = request.POST.get('stuid')
#             username = request.POST['username']
#             lastname = request.POST['lastname']
#             email = request.POST['email']
#             contact = request.POST['contact']
#             if (uid ==  ""):
#                 user = User(username=username, lastname=lastname, email=email, contact=contact)
#             else:
#                 user = User(id=uid ,username=username, lastname=lastname, email=email, contact=contact)
#
#             user.save()
#             user_data = User.objects.values()
#             print("===>user_data", user_data)
#             list_data = list(user_data)
#             return JsonResponse({'status': 'success', 'list_data': list_data})
#         else:
#             return JsonResponse({'status':"failed"})
#
#
# @csrf_exempt
# def delete_user(request):
#
#     if request.method == "POST":
#         id = request.POST.get('sid')
#         print("===id", id)
#         user = User.objects.get(pk=id)
#         user.delete()
#         return JsonResponse({'status': 1})
#     else:
#         return JsonResponse({'status': 0})
#
# @csrf_exempt
# def edit_user(request):
#     if request.method == "POST":
#         id = request.POST.get('sid')
#         user = User.objects.get(pk=id)
#         user_data = {'id':user.id, "username": user.username, "lastname":user.lastname, "email": user.email, "contact": user.contact}
#         return JsonResponse(user_data)
#     else:
#         return JsonResponse({"status": "user data not found"})
# token based authentication in django login example code for ecemmerce
#
# #import the necessary packages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth import login
# from django.http import HttpResponse
#
# #token based authentication view
# def token_auth_view(request):
#     token = request.POST.get('token')
#     user = authenticate(token=token)
#     if user is not None:
#         login(request, user)
#         return HttpResponse('Authentication successful')
#     else:
#         return HttpResponse('Authentication failed')
#
# #ecommerce view
# def ecommerce_view(request):
#     if request.user.is_authenticated:
#         #Your eCommerce code
#         return HttpResponse('Ecommerce view')
#     else:
#         return HttpResponse('User not authenticated')