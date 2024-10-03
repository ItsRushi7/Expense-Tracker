from django.shortcuts import render, redirect
from Myapp.models import MyExpense
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


def Login(request):

    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        user = authenticate(username=user_name, password=pass_word)

        if user is not None:
            login(request, user)
            print("hello")
            messages.success(request, "Login Successfully ")
            return redirect('Home')

        else:
            pass

    return render(request, 'index.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST.get('Name')
        mobile = request.POST.get('Number')
        email = request.POST.get('Email')
        password = request.POST.get('Password')

        if (username != '' and mobile != '' and email != '' and password != ''):

            Sign_up = User.objects.create_user(
                username=username, email=email, password=password)
            Sign_up.save()
            messages.success(request, "Signup Successfully ")
            return redirect('Login')

    return render(request, 'Signup.html')


def Home(request):

    if request.method == 'POST':

        Category = request.POST.get('Category')
        Amount = request.POST.get('Amount')
        Created = request.POST.get('Created')
        Updated = request.POST.get('Update')
        Comments = request.POST.get('Comments')

        Add = MyExpense()

        Add.Category = Category
        Add.Amount = Amount
        Add.Created_At = Created
        Add.Updated_At = Updated
        Add.Comments = Comments

        Add.save()

    Exp = MyExpense.objects.all()

    return render(request, 'Home.html', {'Exp': Exp})


def Delete(request, id):

    Res = MyExpense.objects.get(id=id)
    Res.delete()

    return redirect('Home')


def Edit(request, id):

    obj = MyExpense.objects.get(id=id)

    return redirect('Update', {"obj": obj})
