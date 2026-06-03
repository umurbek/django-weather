<h1 align="center">🌦️ Django Weather App</h1>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <a href="#english">English</a> •
  <a href="#русский">Русский</a> •
  <a href="#o'zbekcha">O'zbekcha</a>
</p>

---

<a id="english"></a>
## 🌐 English Version

### 📖 About the Project
**Django Weather App** is a simple, fast, and user-friendly web application built with Django. It provides real-time weather information for any city around the world by integrating with the **OpenWeatherMap API**. 

### ✨ Key Features
- **🔍 City-based Search:** Get current weather conditions by simply typing a city name.
- **🌡️ Detailed Weather Data:** Displays temperature, humidity, wind speed, and weather description.
- **☁️ Visual Icons:** Shows dynamic weather icons based on current conditions.
- **🛡️ Robust Error Handling:** Gracefully handles 404 errors, invalid city names, and API connection issues.
- **🔐 Secure Configuration:** Uses `.env` for safe storage of API keys and secret configurations.

### 🛠️ Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-EB6E4B?style=for-the-badge&logo=openweathermap&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

---

<a id="русский"></a>
## 🇷🇺 Русская Версия

### 📖 О проекте
**Django Weather App** — это простое и быстрое веб-приложение, созданное на Django. Оно позволяет получать актуальные данные о погоде в любом городе мира благодаря интеграции с **OpenWeatherMap API**.

### ✨ Основные возможности
- **🔍 Поиск по городам:** Узнайте погоду, просто введя название города.
- **🌡️ Детальные данные:** Отображение температуры, влажности, скорости ветра и описания погоды.
- **☁️ Иконки погоды:** Визуализация погодных условий с помощью динамических иконок.
- **🛡️ Обработка ошибок:** Корректная обработка неверных названий городов, ошибок 404 и сбоев API.
- **🔐 Безопасность:** Использование `.env` для защиты API-ключей.

---

<a id="o'zbekcha"></a>
## 🇺🇿 O'zbekcha Versiyasi

### 📖 Loyiha haqida
**Django Weather App** — bu Django yordamida qurilgan oddiy, sodda va tezkor ob-havo tekshirish web-ilovasi. Tizim **OpenWeatherMap API** orqali dunyoning istalgan shahridagi joriy ob-havo ma'lumotlarini real vaqt rejimida taqdim etadi.

### ✨ Asosiy Imkoniyatlar
- **🔍 Shahar bo'yicha qidirish:** Shahar nomini kiritish orqali ob-havoni aniqlash.
- **🌡️ To'liq ma'lumot:** Harorat, namlik, shamol tezligi va holat (weather description) ko'rsatkichlari.
- **☁️ Ob-havo ikonkalari:** Holatga mos keluvchi vizual ikonkalarni ko'rsatish.
- **🛡️ Xatoliklarni ushlash:** Noto'g'ri shahar nomi, 404 xatoliklar va API muammolarini to'g'ri qaytarish.
- **🔐 Maxfiylik:** API kalitlarni `.env` orqali xavfsiz saqlash.

---

## 🚀 Installation / O'rnatish

```bash
# 1. Clone the repository / Loyihani yuklab oling
git clone [https://github.com/umurbek/django-weather.git](https://github.com/umurbek/django-weather.git)
cd django-weather

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up Environment Variables
# Create a .env file in the root directory and add:
# SECRET_KEY=your_django_secret_key
# OPENWEATHER_API_KEY=your_api_key_here

# 5. Run database migrations
python manage.py migrate

# 6. Start the server
python manage.py runserver
.