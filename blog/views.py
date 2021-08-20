from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Jacob Short',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 19, 2021'
    },
        {
        'author': 'Raelynn Short',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 19, 2021'
    },
        {
        'author': 'Samantha Short',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 19, 2021'
    },


]

def home_view(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about_view(request):
        return render(request, 'blog/about.html', {'title': 'About'})

