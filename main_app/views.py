from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    our_services = ["Bush Camps", "Balloon Tours", "Hunting", "Village Visits", "Yoga"]
    price = 10000
    date = '15-11-2024'
    return render(request, 'services.html', {'our_services': our_services, 'price': price, 'date': date})