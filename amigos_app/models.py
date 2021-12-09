
from django.db import models
import re
from datetime import date

class UserManager(models.Manager):

    def Validaciones_login(self,login_date):
        errores = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(login_date['first_name'])< 2:
            errores['first_name']='First Name must be longer than 1 character'
            
        
        if len(login_date['alias'])< 2:
            errores['alias']= 'alias must be longer than 1 character'
            

        if not EMAIL_REGEX.match(login_date['email']):
            errores['email'] ='Email is in an invalid format'

        
        if login_date['password'] != login_date['confirm_password']:
            errores['password'] ='Passwords do not match'
            

        if len(login_date['password']) < 8 :
            errores['password'] ='Password must be 8 or more characters long'
        
        
        fecha = login_date['register_date'].split("-")
        fecha = date(int(fecha[0]),int(fecha[1]), int(fecha[2]))
        print(fecha)
        hoy = date.today()
        if hoy.year-fecha.year<16:
            errores['register_date'] ='Debe tener al menos 16 para registrarte'
        # if fecha > hoy:
        #     errores['register_date'] ='Debe tener al menos 16'
        
        return errores

class User1(models.Model):
    first_name = models.CharField(max_length = 60)
    alias = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 150)
    register_date = models.DateField()
    objects = UserManager()# esto me da acceso a los errores de esta definicion
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return f" ({self.id})| First Name: {self.first_name}| Alias: {self.alias}| Email: {self.email} ||"

class Friends(models.Model):
    name_friend= models.ForeignKey(User1,related_name = 'name_friend', on_delete = models.CASCADE)
    amigo =  models.ManyToManyField(User1)
    

