import os
import requests
from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv

load_dotenv()

def error404(request, exception):
     return render(request, '404.html', status=404)

# Create your views here.
def get_my_ipaddress(request):
     # The name of the visitor
     visitor_name = "Guest" or request.GET.get('visitor_name')
     
     # The current Ip Address of the visitor using the BIGDATACLUD.net api route
     get_client_ip = requests.get(url="https://api.ipify.org?format=json")
     client_ip_address = get_client_ip.json().get('ip')
     
     # get the Requester City Location for OpenweatherAPI to get it's temperatur details
     get_client_location_by_ip_address = requests.get(url=f"https://ipinfo.io/{client_ip_address}/json?token={os.getenv('IP_INFO_TOKEN')}")

     client_location = get_client_location_by_ip_address.json().get('city')
     
     openweather_url = f'https://api.openweathermap.org/data/2.5/weather?q={client_location}&appid={os.getenv('OPEN_WEATHER_API_KEY')}'
     tempetature = requests.get(openweather_url).json()['main']['temp']
     
     return JsonResponse({
          'client_ip': client_ip_address, 
          'location': client_location, 
          'grettings': f'Hello, {visitor_name}!, the temperature is {tempetature} degrees Celcius in {client_location}'
          })