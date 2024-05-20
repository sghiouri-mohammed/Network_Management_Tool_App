from django.shortcuts import render, redirect

from nmt.models import Account, NetworkCenter, Building, Floor, Local, Equipement


def register(request):

    message = ""

    if (request.method == "POST"):

        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        mail = request.POST["mail"]
        username = request.POST["username"]
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

        username = request.POST["username"]
        mot_de_passe = request.POST["pwd"]

        users = Account.objects.all()

        for user in users:

            if( user.username == username and user.password == mot_de_passe ):

                d = True
                request.session["fname"] = user.firstname
                request.session["lname"] = user.lastname
                request.session["mail"] = user.username

        if d:
            return redirect("home")

        else:
            message = " Login credentials are false !"

    return render(request, "login.html",context={"message":message})


def home(request):
    return render(request, "home.html")


def index(request):
    liste_users = Account.objects.all()
    nbr_users = len(liste_users)

    liste_floors = Floor.objects.all()
    nbr_floors = len(liste_floors)

    list_materials = Equipement.objects.all()
    nbr_materials = len(list_materials)

    list_build = Building.objects.all()
    nbr_build = len(list_build)

    list_nc = NetworkCenter.objects.all()
    nbr_nc = len(list_nc)

    return render(request, "Network Configuration Management/index.html",context={"number_of_nc":nbr_nc,"number_of_buildings":nbr_build,"number_of_floors":nbr_floors,"number_of_materials":nbr_materials,"number_of_users":nbr_users,"first_name":request.session["fname"], "last_name":request.session["lname"]})


def netwok_centers(request):

    message = ""
    network_centers = NetworkCenter.objects.all()

    if (request.method == "POST"):
        nom = request.POST["name"]

        nc = NetworkCenter(nom=nom)

        if nc:
            nc.save()
            message = " Network Center Added Successfully !"
        else:
            message = " Error !! "

    return render(request, "Network Configuration Management/network_centers.html",context={"list_network_centers":network_centers,"first_name":request.session["fname"], "last_name":request.session["lname"], "message":message})


def delete_network_center(request, id_center):

    center = NetworkCenter.objects.get(id=id_center)
    center.delete()

    return redirect('config')


def buildings(request, id_center):
    message = " "

    bb = Building.objects.filter(id_network_center=id_center)
    print(len(bb))

    center = NetworkCenter.objects.get(id=id_center)
    network_centers = NetworkCenter.objects.all()

    if request.method == "POST":
        network_center = request.POST["netwok_center"]
        name = request.POST["building"]
        info = request.POST["info"]

        build = Building(id_network_center=network_center, building_name=name, info=info)

        if build:
            build.save()
            message = " Building Added Successfully !"
        else:
            message = " Error !! "

    return render(request, "Network Configuration Management/network_center_buildings.html",context={"list_network_centers":network_centers,"center":center,"list_buildings":bb,"message":message,"first_name":request.session["fname"], "last_name":request.session["lname"]})


def delete_building(request, id_building):

    buil = Building.objects.get(id=id_building)
    id_center = buil.id_network_center
    buil.delete()
    return buildings(request, id_center)


def floor(request, id_center, id_building):
    message = ""

    center = NetworkCenter.objects.get(id=id_center)
    building = Building.objects.get(id=id_building)
    buildings = Building.objects.all()
    floors = Floor.objects.filter(id_network_center=id_center, id_building=building.id)
    print(len(floors))

    if request.method == "POST":

        buildingg = request.POST["building"]
        name = request.POST["floor"]
        info = request.POST["info"]
        number = request.POST["number"]

        flo = Floor(id_network_center=id_center, id_building=buildingg, nom=name, floor=number, info=info)

        if flo:
            flo.save()
            message = " Floor Added Successfully !"
        else:
            message = " Error !! "

    return render(request, "Network Configuration Management/network_center_buidling_floors.html",context={"floors":floors,"building":building, "buildings":buildings, "center":center,"message":message,"first_name":request.session["fname"], "last_name":request.session["lname"]})


def delete_floor(request, id_floor):

    flooor = Floor.objects.get(id=id_floor)
    id_center = flooor.id_network_center
    id_building = flooor.id_building
    flooor.delete()

    return floor(request, id_center, id_building)


def local(request, id_center, id_building, id_floor):

    message = ""

    center = NetworkCenter.objects.get(id=id_center)
    building = Building.objects.get(id=id_building)
    floor = Floor.objects.get(id=id_floor)
    floors = Floor.objects.all()
    buildings = Building.objects.all()

    list_local = Local.objects.filter(id_network_center=id_center, id_building=id_building, id_floor_salle=id_floor)

    if request.method == "POST":

        flooor = request.POST["floor"]
        name = request.POST["local"]
        info = request.POST["info"]

        local = Local(id_network_center=id_center, id_building=id_building, id_floor_salle=flooor, nom=name, info=info)

        if local:
            local.save()
            message = " Floor Added Successfully !"
        else:
            message = " Error !! "

    return render(request, "Network Configuration Management/locals.html",
                  context={"locals":list_local, "floor": floor,"floors": floors, "building": building, "buildings": buildings, "center": center,
                           "message": message, "first_name": request.session["fname"],
                           "last_name": request.session["lname"]})



def delete_local(request, id_local):

    localo = Local.objects.get(id=id_local)

    id_center = localo.id_network_center
    id_building = localo.id_building
    id_floor = localo.id_floor_salle
    localo.delete()

    return local(request, id_center, id_building, id_floor)



def equipement(request, id_center, id_building, id_floor, id_local):

    message = ""

    center = NetworkCenter.objects.get(id=id_center)
    building = Building.objects.get(id=id_building)
    floor = Floor.objects.get(id=id_floor)
    local = Local.objects.get(id=id_local)
    locals = Local.objects.all()

    list_materials = Equipement.objects.filter(id_network_center=id_center, id_building=building.id, id_floor_salle=floor.id, id_local=local.id)

    if request.method == "POST":

        switch = request.POST["switch"]
        addr = request.POST["addr"]
        model = request.POST["model"]
        role = request.POST["role"]
        locall = request.POST["local"]
        info = request.POST["info"]

        equi = Equipement(id_network_center=id_center, id_building=id_building, id_floor_salle=id_floor, id_local=locall, nom=switch, ip=addr, model=model, role=role, info=info)

        if equi:
            equi.save()
            message = " Material Added Successfully !"
        else:
            message = " Error !! "

    return render(request, "Network Configuration Management/equipements.html",
                  context={"locals":locals,"floor":floor, "local": local,"materials": list_materials, "building": building, "buildings": buildings, "center": center,
                           "message": message, "first_name": request.session["fname"],
                           "last_name": request.session["lname"]})



def add_network_center(request):
    message = ""

    if request.method == "POST":
        nom = request.POST["name"]

        nc = NetworkCenter(nom=nom)

        if nc:
            nc.save()
            return redirect('index')

    return render(request, "Network Configuration Management/Ajouter_network_Center.html",
                  context={"first_name": request.session["fname"],
                           "last_name": request.session["lname"]})



def add_building(request):

    list_nc = NetworkCenter.objects.all()

    if request.method == "POST":
        nom = request.POST["name"]
        network_ce = request.POST["nc"]
        info = request.POST["info"]

        building = Building(id_network_center=network_ce, building_name=nom, info=info)

        if building:
            building.save()
            return redirect('index')

    return render(request, "Network Configuration Management/Ajouter_Building.html",
                  context={"network_centers":list_nc,"first_name": request.session["fname"],
                           "last_name": request.session["lname"]})



def add_floor_room(request):

    list_nc = NetworkCenter.objects.all()
    list_bd = Building.objects.all()

    if request.method == "POST":
        nc = request.POST["nc"]
        bd = request.POST["bd"]
        name = request.POST["name"]
        number = request.POST["number"]
        info = request.POST["info"]

        floor_room = Floor(id_network_center=nc, id_building=bd, nom=name, floor=number, info=info)

        if floor_room:
            floor_room.save()
            return redirect('index')

    return render(request, "Network Configuration Management/Ajouter_floor_room.html",
                  context={"buildings":list_bd,"network_centers":list_nc,"first_name": request.session["fname"],
                           "last_name": request.session["lname"]})








def logout(request):

    request.session["fname"] = None
    request.session["lname"] = None
    request.session["mail"] = None

    return redirect("login")

def addfloor(request):

    message = ""

    if request.method == "POST":
        floor_name = request.POST["floor_name"]
        floor_level = request.POST["floor_level"]

        floor = Floor(floor_name=floor_name, floor_level=floor_level)

        if floor:
            message = "Floos seccessfully added"
            floor.save()

    return render(request, "Network Configuration Management/addfloor.html",context={"message":message,"first_name":request.session["fname"], "last_name":request.session["lname"]})










def devices(request):
    return render(request, 'Network Configuration Management/device.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})


def campus_details(request):

    return render(request, 'Network Configuration Management/campus_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def data_centre_details(request):
    return render(request, 'Network Configuration Management/data_centre_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def conference_centre_details(request):
    return render(request, 'Network Configuration Management/conference_centre_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})










def chateau_details(request):
    return render(request, 'Network Configuration Management/campus/chateau_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})


def marshall_building_details(request):
    return render(request, 'Network Configuration Management/campus/marshall_building_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def boulogne_details(request):
    return render(request, 'Network Configuration Management/campus/boulogne_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})


def franqueville_details(request):
    return render(request, 'Network Configuration Management/campus/franqueville_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def octave_feuillet_details(request):
    return render(request, 'Network Configuration Management/campus/octave_feuillet_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def monaco_details(request):
    return render(request, 'Network Configuration Management/campus/monaco_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def ch_basement_details(request):
    return render(request, 'Network Configuration Management/campus/chateau/ch_basement_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def ch_ground_floor_details(request):
    return render(request, 'Network Configuration Management/campus/chateau/ch_ground_floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def ch_third_floor_details(request):
    return render(request, 'Network Configuration Management/campus/chateau/ch_third_floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})
def mb_basement_details(request):
    return render(request, 'Network Configuration Management/campus/marshall_building/mb_basement_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def mb_ground_floor_details(request):
    return render(request, 'Network Configuration Management/campus/marshall_building/mb_ground_floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def mb_first_floor_details(request):
    return render(request, 'Network Configuration Management/campus/marshall_building/mb_first_floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def mb_second_floor_details(request):
    return render(request, 'Network Configuration Management/campus/marshall_building/mb_second_floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def mb_third_floor_details(request):
    return render(request, 'Network Configuration Management/campus/marshall_building/mb_third_floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def mb_fourth_floor_details(request):
    return render(request, 'Network Configuration Management/campus/marshall_building/mb_fourth_floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})
def mb_fifth_floor_details(request):
    return render(request, 'Network Configuration Management/campus/marshall_building/mb_fifth_floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})

def mb_sixth_floor_details(request):
    return render(request, 'Network Configuration Management/campus/marshall_building/mb_sixth_floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})


def floor_details(request):
    return render(request, 'Network Configuration Management/campus/floor_details.html', context={"first_name":request.session["fname"], "last_name":request.session["lname"]})
