from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import re
import bcrypt
from amigos_app.models import *
from datetime import datetime, time, timezone
from time import gmtime, strftime


def index(request):
    if 'login' not in request.session:
        request.session['login'] = False
    
    if 'u_id' not in request.session:
        request.session['u_id'] = 0

    return render(request, 'index.html')


def logout(request):
    request.session.clear()
    return redirect('/main')

def home(request):
    if request.session['login'] == True:
        user = User1.objects.filter(id = request.session['u_id'])
        user_info = {
            'user':user[0]
        }
        return redirect('/friends', user_info)

    else:
        return redirect('/main')

def reg_validate(request):
    if request.method == 'POST':
        errorescome= User1.objects.Validaciones_login(request.POST)
        if errorescome :
            print(errorescome)
            for error_key, error_value in errorescome.items():
                messages.error(request, error_value, extra_tags= error_key) 
            return render(request, 'index.html')
        else:
            user= User1.objects.filter(email=request.POST['email'])
            if user:
                print('email are ok')
                messages.error(request,'error de login')
                return render(request, 'index.html')
            else:
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                new_user = User1.objects.create(first_name = request.POST['first_name'], alias = request.POST['alias'], email = request.POST['email'], register_date = request.POST['register_date'], password = pw_hash)
                print(new_user)
                request.session['u_id'] = new_user.id
                #save User._id in session
                messages.success(request, 'You have registered succesfully. You may now login', extra_tags = 'registered')
                return redirect('/friends')

    return redirect('/main')

def login_validate(request):
        email = request.POST["email"]
        password = request.POST["password"]
        print(f"{email} {password}")
        echeck = User1.objects.filter(email=email) 
        print (echeck)
        if echeck:
            print('existe')
            #if echeck[0].password == password:
            if bcrypt.checkpw(request.POST['password'].encode(), echeck[0].password.encode()):
                print(echeck[0].password)
                request.session['login'] = True
                request.session['u_id'] = echeck[0].id
                return redirect('/friends')
            else:
                print('passwor bad')
                messages.error(request,'Password invalido', extra_tags = 'badpas')
                return redirect('/main')

        else: 
            messages.error(request,'Email No registrado', extra_tags = 'malem')
            return redirect('/main')
            


def friends(request):
    user = User1.objects.get(id=request.session['u_id'])
    usuario = User1.objects.all()
    amigos= Friends.objects.all()
    context ={
        'user':user,
        'friend':amigos,
        'usuario':usuario,
    }
    return render (request,'friends.html',context)


def user(request,id):
    usuario = User1.objects.all()
    friends = Friends.objects.get(id=id)
    user=User1.objects.get(id=request.session['u_id'])
    friends.amigo.add(user)
    friends.save()
    context ={
        'user':user,
        'usuario':usuario,
    }
    print(friends)
    print(user)
    print(usuario)
    return render(request,'user.html',context)

def add(request,id):
    
    user=User1.objects.get(id=request.session['u_id'])
    friends = Friends.objects.get(id=id)
    amig= Friends.objects.create(name_friend=user)
    amig.amigo.add(user)
    amig.save()
    friends.amigo.add(user)
    friends.save()
    print(amig)
    print(friends)
    return redirect('/friends')
    
    
def remove(request,id):
    friends = Friends.objects.get(id=id)
    user=User1.objects.get(id=request.session['u_id'])
    friends.amigo.add(user)
    friends.save()
    return redirect('/friends')



