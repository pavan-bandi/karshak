from django.shortcuts import render
from .models import bacterialdiseases,fungaldiseases,crops,farmer,pesticides

from django.contrib import messages

def home(request):
    bacs=bacterialdiseases.objects.all()
    fungs=fungaldiseases.objects.all()

    return render(request,'index.html',{'bacs':bacs,'fungs':fungs})
def farmerscorner(request):
    if request.method=='GET':
        farmer_id = request.GET.get('f_id')
        crop_id = request.GET.get('crop_id')
        farmers = farmer.objects.filter(farmerid=farmer_id)
        cropps = crops.objects.filter(crop_id=crop_id)
        pests = pesticides.objects.filter(crop_id=crop_id)



        return render(request,'farmer.html',{'farmers':farmers,'crops':cropps,'pests':pests} )
    else:
        return render(request, 'farmer.html')

def addf(request):
    return render(request,'addfarmer.html')
def addc(request):
    return render(request,'addcrops.html')
def addp(request):
    return render(request,'addpest.html')
def addfarmers(request):
    farmer_id = request.GET.get('fid')
    farmer_name = request.GET.get('fname')
    farm_land = request.GET.get('fland')
    phone_No = request.GET.get('phone')
    if not (farmer_id and  farmer_name and farm_land and phone_No):
        messages.error(request, 'Please provide all the details!!')
        return render(request, 'addfarmer.html')
    is_user_exists = farmer.objects.filter(farmerid=farmer_id).exists()

    if is_user_exists:
        messages.error(request, 'User with this  id already exists. U can add ur crops' )
        return render(request, 'addfarmer.html')
    f=farmer()
    f.farmerid=farmer_id
    f.Name=farmer_name
    f.farmland=farm_land
    f.phone_no=phone_No
    f.save()

    return render (request,'addfarmer.html')
    
def addcrops(request):
    farmer_id=request.GET.get('farm_id')
    cropid=request.GET.get('c_id')
    crop_name=request.GET.get('cname')
    crop_ex=request.GET.get('c_ex')
    crop_season=request.GET.get('c_season')
    if not (farmer_id and cropid and  crop_name and crop_ex and crop_season):
        messages.error(request, 'Please provide all the details!!')
        return render(request, 'addcrops.html')
    is_farmer_exists = farmer.objects.filter(farmerid=farmer_id).exists()
    if not is_farmer_exists :
        messages.error(request, 'user with this id does not exist create new farmer')
        return render(request, 'addcrops.html')
    is_user_exists = crops.objects.filter(crop_id=cropid).exists()

    if is_user_exists:
        messages.error(request, 'User with this  id already exists. U can add ur crops' )
        return render(request, 'addcrops.html')
    c=crops()
    c.crop_id=cropid
    c.crop_name=crop_name
    c.cr_ex=crop_ex
    c.crop_season=crop_season
    c.crop_year=2022
    c.save()

    return render(request, 'farmer.html')
def addpests(request):
    cropid=request.GET.get('c_id')
    fertilizer_for=request.GET.get('pfor')
    fname=request.GET.get('pname')
    price=request.GET.get('price')

    if not (cropid and  fertilizer_for and fname and price):
        messages.error(request, 'Please provide all the details!!')
        return render(request, 'addpest.html')
    is_user_exists = crops.objects.filter(crop_id=cropid).exists()
    if not is_user_exists:
        messages.error(request, 'crop id  does not exist. ')
        return render(request, 'addpest.html')
    p=pesticides()
    p.crop_id=cropid
    p.fert_or_pest=fname
    p.price=price
    p.fertizer_for=fertilizer_for
    p.save()

    return render(request,'addpest.html')


