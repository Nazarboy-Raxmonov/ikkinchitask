from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import iphone, redmi

# Create your views here.
def iphonedetailviews(request,tel_id):
    telefon = get_object_or_404(iphone, id = tel_id)

    telinfo = {
        'model' : telefon.model,
        'country' : telefon.country
    }

    return JsonResponse(telinfo, safe = False)

def iphoneallviews(request):
    res = []
    alltels = iphone.objects.all()
    for i in alltels:
        res.append({
            'model' : i.model,
            'country': i.country
        })
    
    return JsonResponse(res, safe = False)

def redmidetailviews(request, tel_model):
    redmitel = get_object_or_404(redmi, model = tel_model)

    telinfo = {
        'model' : redmitel.model,
        'year' : redmitel.year
    }

    return JsonResponse(redmitel, safe = False)

def redmiallviews(request):
    ans = []
    allredmis = redmi.objects.all()
    for i in allredmis:
        ans.append({
            'model' : i.model,
            'year' : i.year
        })
    return JsonResponse(ans, safe = False)

