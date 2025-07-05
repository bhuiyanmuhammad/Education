from django.shortcuts import render, HttpResponse



def home(request):
    #return HttpResponse("This is HomePage")
    return render(request, 'home.html')