from django.shortcuts import render, redirect


# 指向對應的 html 檔案
def home(request):
    return render(request, 'home.html') 

def serivce(request):
    return render(request, 'serivce.html')

def news(request):
    return render(request, 'news.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dialogflow(request):
    return render(request, 'dialogflow.html')

def clinic_address(request):
    return render(request, 'clinic_address.html')
