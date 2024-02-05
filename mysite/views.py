from django.shortcuts import render



# file viwes project
def index(request):
    return render(request, 'index.html')