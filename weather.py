import requests
#(requests.__version__)
import json
def get_weather(city):
    API_KEY = "15c86aab3a1660794c777a18af8c635e"
    params = {"q": city ,"appid": API_KEY,"units": "metric"}
    try:
       response = requests.get("https://api.openweathermap.org/data/2.5/weather",params = params,timeout = 5)
       if response.status_code == 200:
          data = response.json()
          return({"city": city ,"temperature": data["main"]["temp"],"feels_like": data["main"]["feels_like"]})
          return weather
       elif response.status_code == 404:
          print("Enter a validd city")
          return None
       else:
          print("status code:" , response.status_code)
          return None 
    except requests.RequestException:
       print("network error")
       return None
#calling the function
try:
   while True:
      print("1.Add more cities: ")
      print("2.Exit")
      choice = int(input("Enter the choice "))
      if choice ==1:
          weather = get_weather(input("Enter the city:"))
          if weather is not None:
             try:
                with open("weather.json","r") as file:
                   saved_cities = json.load(file)
             except FileNotFoundError:
                saved_cities = []     
             saved_cities.append(weather)
             with open("weather.json","w")as file:
                 write = json.dump(saved_cities,file,indent = 4)
             with open("weather.json","r") as file:
                print(json.load(file))
      elif choice == 2:
          break
      else:
         print("please enter 1 or 2")
except ValueError:
   print("Invalid!")    