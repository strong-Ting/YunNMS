from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, 'Backend/Permission/dashboard.html', locals())

def setup(request):
    return HttpResponse(request)
