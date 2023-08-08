from django.shortcuts import render
import urllib
import json

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        # source contain JSON data from API

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='
            + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "name": str(list_of_data['name']),
            "lon": str(list_of_data['coord']['lon']),
            "lan": str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "pages/home.html", data)
