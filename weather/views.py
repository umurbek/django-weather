from django.shortcuts import render
import requests
import os

def get_weather_for_city(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        raise RuntimeError("OPENWEATHER_API_KEY is missing in .env file")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "en"
    }

    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()

    return resp.json()


def index(request):
    context = {"weather": None, "error": None}

    if request.method == "POST":
        city = request.POST.get("city", "").strip()

        if city:
            try:
                data = get_weather_for_city(city)

                context["weather"] = {
                    "city": f"{data['name']}, {data['sys'].get('country', '')}",
                    "temp": data['main']['temp'],
                    "desc": data['weather'][0]['description'].title(),
                    "humidity": data['main']['humidity'],
                    "wind": data['wind']['speed'],
                    "icon": data['weather'][0]['icon'],
                }

            except requests.HTTPError as e:
                if e.response.status_code == 404:
                    context["error"] = "Shahar topilmadi. Iltimos, to‘g‘ri nom kiriting."
                else:
                    context["error"] = f"API xatosi: {e.response.status_code}"
            except Exception as e:
                context["error"] = f"Xatolik: {e}"

        else:
            context["error"] = "Iltimos, shahar nomini kiriting."

    return render(request, 'weather/index.html', context)
