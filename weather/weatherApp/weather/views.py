import requests
from django.shortcuts import render, redirect

from .forms import CityForm
from .models import City

#def fetch_data (request):


def index(request):
    API_KEY = '78de6a7fc9f3d64b8af6cc331977a4dc'

    if request.method == 'POST':
        print('req',request)
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []
    for city in cities:
        # url = 'http://api.openweathermap.org/data/2.5/weather?{}&units=metric&appid=' + API_KEY
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY
        req = requests.get(url.format(city.name)).json()
        print(req)

        city_weather = {
            'id': city.id,
            'city': req['name'],
            'temperature': req['main']['temp'],
            'description': req['weather'][0]['description'],
            'wind': req['wind']['speed'],
            'pressure': req['main']['pressure'],
            'icon': req['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/index.html', context)


def delete(request, id):
    if request.method == 'POST':
        City.objects.filter(id=id).delete()

    return redirect('/')
