from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'factorial.html')


def factorial(request):
    y = 1
    for i in range(1,int(request.GET['num'])+1):
        y = y*i
    return render(request, "result.html",{'result':y})