from django.shortcuts import render



# file viwes project
def index(request):
    context = {
        'title':'web development fullstack',
        'developer':'pudin',
    }
    return render(request, 'index.html', context)