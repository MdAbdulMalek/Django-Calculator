from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def submit(request):
    q = request.GET['query']
    '''jsondict = {
        "q" : q
    }
    return JsonResponse(jsondict)'''
    #return HttpResponse(q)
    try:
        ans = eval(q)
        mydictionary = {
            "q" : q,
            "ans" : ans,
            "error" : False
        }
        return render(request, "index.html", context= mydictionary)
    except:
        mydictionary ={
            "error" : True
        }
        return render(request, "index.html", context= mydictionary)