from django.shortcuts import render,redirect

# from pwn.forms import CuisineForm
from pwn.models import AdminLoginModel,StateModel,CityModel,CuisineModel
from django.contrib import messages

def showIndex(request):
    return render(request,"pwn/login.html")


def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),
                                                password=request.POST.get("pwn_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "pwn/login.html", {"error": "Admin Logout Success"})



def welcome(request):
    return render(request,"pwn/home.html")


def openState(request):
    return render(request,"pwn/openstate.html",{"state_data":StateModel.objects.all()})


def openCity(request):
    return render(request,"pwn/opencity.html",{"state":StateModel.objects.all(),"city_data":CityModel.objects.all()})


def openCusine(request):
    return render(request,"pwn/opencuisine.html",{"cuisine_data":CuisineModel.objects.all()})

def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")

def saveState(request):
    if request.POST.get("upd_idno"):
        sm=StateModel.objects.get(id=request.POST.get("upd_idno"))
        sm.name=request.POST.get("state")
        if not request.FILES.get("photo"):
            pass
        else:
            sm.photo=request.FILES.get("photo")
        sm.save()
        return render(request,"pwn/openstate.html",{"success":"Updated Successfully","state_data": StateModel.objects.all()})
    else:
        try:
            StateModel.objects.get(name=request.POST.get("state"))
            return render(request, "pwn/openstate.html",
                          {"error": "State Already Exist", "state_data": StateModel.objects.all()})
        except:
            StateModel(name=request.POST.get("state"), photo=request.FILES.get("photo")).save()
            messages.success(request, "State Added")
            return redirect('state')


def updateState(request):
    idno=request.GET.get("idno")
    sm=StateModel.objects.get(id=idno)
    return render(request,"pwn/openstate.html",{"idno":sm.id,"state":sm.name,"photo":sm.photo,"state_data":StateModel.objects.all()})


def deleteState(request):
    print(request.GET.get("idno"))
    print(type(request.GET.get("idno")))
    StateModel.objects.get(id=request.GET.get("idno")).delete()
    return redirect('state')


def saveCity(request):
    if request.POST.get("upd_idno"):
        cm=CityModel.objects.get(id=request.POST.get("upd_idno"))
        cm.name=request.POST.get("city")
        if not request.FILES.get("photo"):
            pass
        else:
            cm.photo=request.FILES.get("photo")
        cm.save()
        updateCityId(request,request.POST.get("upd_idno"),request.POST.get("state"))
        return render(request,"pwn/opencity.html",{"success":"Updated Successfully","city_data": CityModel.objects.all(),"state":StateModel.objects.only('name')})
    else:
        try:
            CityModel.objects.get(name=request.POST.get("city"))
            return render(request, "pwn/opencity.html",
                          {"error": "City Already Exist", "city_data": CityModel.objects.all()})
        except:
            CityModel(name=request.POST.get("city"), photo=request.FILES.get("photo"),city_state_id=request.POST.get("state")).save()
            messages.success(request, "City Added")
            return redirect('city')

def updateCityId(request,upd_id,fkid):
    sm=StateModel.objects.get(id=fkid)
    CityModel.objects.filter(id=upd_id).update(city_state_id=sm.id)

def updateCity(request):
    idno = request.GET.get("idno")
    print(idno)
    cm = CityModel.objects.get(id=idno)
    return render(request, "pwn/opencity.html",
                  {"idno": cm.id, "city_state":cm.city_state.id, "state_name":cm.city_state.name , "city": cm.name, "photo": cm.photo, "city_data": CityModel.objects.all(),"state":StateModel.objects.only('name')})


def deleteCity(request):
    print(request.GET.get("idno"))
    print(type(request.GET.get("idno")))
    CityModel.objects.get(id=request.GET.get("idno")).delete()
    return redirect('city')

def saveCuisine(request):
    if request.POST.get("upd_idno"):
        cm=CuisineModel.objects.get(id=request.POST.get("upd_idno"))
        cm.type=request.POST.get("cuisine")
        if not request.FILES.get("photo"):
            pass
        else:
            cm.photo=request.FILES.get("photo")
        cm.save()
        return render(request,"pwn/opencuisine.html",{"success":"Updated Successfully","cuisine_data": CuisineModel.objects.all()})
    else:
        try:
            CuisineModel.objects.get(type=request.POST.get("cuisine"))
            return render(request, "pwn/opencuisine.html",
                          {"error": "Cuisine Already Exist", "cuisine_data": CuisineModel.objects.all()})
        except:
            CuisineModel(type=request.POST.get("cuisine"), photo=request.FILES.get("photo")).save()
            messages.success(request, "Cuisine Added")
            return redirect('cuisine')


def updateCuisine(request):
    idno=request.GET.get("idno")
    cm=CuisineModel.objects.get(id=idno)
    return render(request,"pwn/opencuisine.html",{"idno":cm.id,"cuisine":cm.type,"photo":cm.photo,"cuisine_data":CuisineModel.objects.all()})

def deleteCuisine(request):
    print(request.GET.get("idno"))
    print(type(request.GET.get("idno")))
    CuisineModel.objects.get(id=request.GET.get("idno")).delete()
    return redirect('cuisine')




