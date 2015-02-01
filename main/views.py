from django.views import generic
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')



# class IndexView(generic.ListView):
#     template_name = 'main/index.html'




