from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'out.html')


def factorial(request):
    # val1 = request.GET['num1']
    y = 1
    for i in range(1,int(request.GET['num'])+1):
        y = y*i
    return render(request, "result.html",{'result':y})