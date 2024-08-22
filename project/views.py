from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Hey Riya")

def home(request):
    return HttpResponse("Blog")
    