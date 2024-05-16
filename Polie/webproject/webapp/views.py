from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt #csrf errors

# HOME
def home(request):
    context = {}
    # i.e context['webname'] = "RBIS"
    return render(request, "start-page.html", context)


# check connection
def check(request):
    return HttpResponse("Server successfully connected!")

#PASSENGER Profile
def profile_view(request):
    # Your view logic goes here
    return render(request, 'snippets/02_passenger/profile.html')

def profile_view(request):
    # Your view logic goes here
    return render(request, 'snippets/02_driver/profile.html')

#SETTINGS
def settings_view(request):
    # Your view logic goes here
    return render(request, 'snippets/02_passenger/settings.html')

# def settings_view(request):
#     # Your view logic goes here
#     return render(request, 'snippets/02_driver/settings.html')


"""
def home(request):
    return render(request, r"home.html", {}) 
"""
