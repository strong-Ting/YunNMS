from django.shortcuts import render, HttpResponse

from User import models as userModel

# Create your views here.
def dashboard(request):
    users = userModel.find_all(None)
    return render(request, 'User/dashboard.html', locals())

def setup(request):
    return HttpResponse(request)
