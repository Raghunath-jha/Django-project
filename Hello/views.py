from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")
    return render(request,'index.html')
def about(request):
    # return HttpResponse("this is homepage")
    return render(request,'about.html')
def contact(request):
    # return HttpResponse("this is homepage")
    return render(request,'contact.html')
def shopping(request):
    # return HttpResponse("this is homepage")
    return render(request,'shopping.html')
def login(request):
    # return HttpResponse("this is homepage")
    return render(request,'login.html')
