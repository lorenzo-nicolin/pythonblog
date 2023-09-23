from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'tite':'Welcome',
        'content':'this is a test'
    },
    {
        'tite':'Welcome 2',
        'content':'this is a test 2'
    }
]

def home(request):

    content = {
        'posts':posts
    }
    return render(request,'blog/home.html',content)

def about(request):
    return render(request,'blog/about.html')
