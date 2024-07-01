import os
import requests
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

load_dotenv()

def error404(request, exception):
     return render(request, '404.html', status=404)

# Create your views here.
def get_my_ipaddress(request):
     # The name of the visitor
     visitor_names = request.GET.get('visitor_name')

     # The current Ip Address of the visitor using the BIGDATACLUD.net api route
     get_client_ip = requests.get(url="https://api.bigdatacloud.net/data/client-info")
     client_ip_address = get_client_ip.json().get('ipString')
     
     # get the Requester City Location for OpenweatherAPI to get it's temperatur details
     get_client_location_by_ip_address = requests.get(url=f"https://ipinfo.io/41.184.49.67/json?token=673a8868f320dd")
     client_location = get_client_location_by_ip_address.json().get('city')
     
     openweather_url = f'https://api.openweathermap.org/data/2.5/weather?q={client_location}&appid=4e2f3cff62ac3b0aa61f9ab1f840cf46'
     tempetature = requests.get(openweather_url).json()['main']['temp']
     
     return JsonResponse({
          'client_ip': client_ip_address, 
          'location': client_location, 
          'grettings': f'Hello, {visitor_names}!, the temperature is {tempetature} degrees Celcius in {client_location}'
          })