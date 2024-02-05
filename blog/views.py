from django.shortcuts import render

# Create your views app here.

def index(request):
    context = {
        'title': 'blog',
        'developer':'ucup',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/blog/artikel','Artikel'],
            ['/blog/berita','Berita'],
        ]
    }
    return render(request, 'blog/index.html', context)

def blog(request):
    context = {
        'title': 'blog',
        'developer':'eko',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/blog/artikel','Artikel'],
            ['/blog/berita','Berita'],
        ]
    }

    return render(request, 'blog/index.html', context)

def artikel(request):
    context = {
        'title': 'artikel',
        'developer':'agung',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/blog/artikel','Artikel'],
            ['/blog/berita','Berita'],
        ]
    }

    return render(request, 'blog/index.html', context)

def berita(request):
    context = {
        'title': 'berita',
        'developer':'budi',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/blog/artikel','Artikel'],
            ['/blog/berita','Berita'],
        ]
    }

    return render(request, 'blog/index.html', context)