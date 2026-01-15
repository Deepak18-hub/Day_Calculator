

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .Mainoperation_Code import calculate_days

#from .goldcal import goldrate


def App(request):
    days = None
    
    if request .method == "POST":
        sdate = request.POST.get("sdate")
        edate = request.POST.get("edate")
        
        days = calculate_days(sdate,edate)
        
    return render(request , "index.html",{"days":days})  

# def goldcal(request):
#     total_cost = None  
#     tgc = None
#     if request.method == "POST":
#         gold_weight = float(request.POST.get("gw"))
#         making_charge = float(request.POST.get("mc"))
#         gold_rate = float(request.POST.get("gr"))
#         pergp = float(gold_rate/10) 
#         tgc = (gold_weight * pergp) + (gold_weight * making_charge )
#         #print(tgc)

#         total_cost = goldrate(gold_weight,making_charge,gold_rate)

#     return render(request, "gold_price.html",{"total_cost":total_cost,"tgc":tgc})
       

# def aboutus(request):
#     return HttpResponse("Welcome to my Page") 
