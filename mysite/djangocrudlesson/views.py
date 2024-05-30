from django.shortcuts import render, redirect
from .models import Gender, User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def index_gender(request):
    genders =Gender.objects.all()

    context = {
        'genders': genders 
    }
    return render(request, 'gender/index.html', context )

def create_gender(request):
    return render(request, 'gender/create.html')

def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender)
    messages.success(request, 'Gender successfully saved!')

    return redirect('/genders')


def show_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) 

    context = {
        'gender':  gender,
    }

    return render(request, 'gender/edit.html', context)

def edit_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) 

    context = {
        'gender':  gender,
    }

    return render(request, 'gender/edit.html', context)

def update_gender(request, gender_id):
    gender = request.POST.get('gender')
 
    Gender.objects.filter(pk=gender_id).update(gender=gender) # UPDATE GENDERS SET  GENDER = GENDER  WHERE GENDER_ID = GENDER_ID
    messages.success(request, 'Gender successfully updated')

    return redirect('/genders')


def delete_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) # SELECT * FROM GENDERS WHERE GENDER_ID = GENDER_ID

    context = {
        'gender':  gender,
    }

    return render(request, 'gender/delete.html', context)

def destroy_gender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete() #  DELETE FROM genders WHERE gender_id = gender_id
    messages.success(request, 'Gender successfully updated.')

    return redirect('/genders')

def index_user(request):
    return render(request, 'user/index.html')

def create_user(request):
    genders = Gender.objects.all()# select from genders

    context = {
        'genders': genders
    }

    return render(request, 'user/create.html', context) 

def store_user(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_Date')
    genderId = request.POST.get('gender_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirm_password')

    if password == confirmPassword:
        User.objects.create(first_name=firstName,  middle_name=middleName, last_name=lastName, age=age, birth_date=birthDate, gender_id=genderId, username=username, password=make_password(password))

        messages.success(request, 'User successfully saved.')
    else:
        messages.error(request, 'Password do not match. ')
        return render(request, 'user/create.html')