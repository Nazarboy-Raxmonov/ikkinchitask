from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import iphone, redmi
from .serializers import redmiSerializer, iphoneSerializer

# Create your views here.
def iphonedetailviews(request,tel_id):
    telefon = get_object_or_404(iphone, id = tel_id)

    telinfo = iphoneSerializer(telefon)

    return JsonResponse(telinfo.data, safe = False)

def iphoneallviews(request):

    alltels = iphone.objects.all()
    res = iphoneSerializer(alltels, many = True)
    return JsonResponse(res.data, safe = False)

def redmidetailviews(request, tel_model):
    redmitel = get_object_or_404(redmi, model = tel_model)

    telinfo = redmiSerializer(redmitel)

    return JsonResponse(redmitel.data, safe = False)

def redmiallviews(request):

    allredmis = redmi.objects.all()
    ans = redmiSerializer(allredmis, many = True)
    return JsonResponse(ans, safe = False)

