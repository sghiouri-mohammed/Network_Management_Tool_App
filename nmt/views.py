from django.shortcuts import render, redirect

from nmt.models import Account


def register(request):

    message = ""

    if (request.method == "POST"):

        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        username = request.POST["mail"]
        mot_de_passe = request.POST["pwd"]


        new_account = Account(lastname=last_name, firstname=first_name, username=username, password=mot_de_passe)

        if new_account:

            new_account.save()
            message = " Account successfully added "

        else:
            message = " Problem accured ! Retry "


    return render(request, "register.html", context={"message":message} )

def login(request):

    d = False
    message = " "

    if (request.method == "POST" ):

        username = request.POST["mail"]
        mot_de_passe = request.POST["pwd"]

        users = Account.objects.all()

        for user in users:

            if( user.username == username and user.password == mot_de_passe ):

                d = True
                request.session["fname"] = user.firstname
                request.session["lname"] = user.lastname
                request.session["mail"] = user.username


        if d:
            return redirect("index")

        else:
            message = " Login credentials are false !"

    return render(request, "login.html",context={"message":message})



def index(request):
    return render(request, "index.html",context={"first_name":request.session["fname"], "last_name":request.session["lname"]})



def logout(request):

    request.session["fname"] = None
    request.session["lname"] = None
    request.session["mail"] = None

    return redirect("login")

def campus_details(request):

    return render(request, 'campus_details.html')

def data_centre_details(request):
    return render(request, 'data_centre_details.html')

def conference_centre_details(request):
    return render(request, 'conference_centre_details.html')

def chateau_details(request):
    return render(request, 'campus/chateau_details.html')


def marshall_building_details(request):
    return render(request, 'campus/marshall_building_details.html')

def boulogne_details(request):
    return render(request, 'campus/boulogne_details.html')


def franqueville_details(request):
    return render(request, 'campus/franqueville_details.html')


def monaco_details(request):
    return render(request, 'campus/monaco_details.html')

