#WeatherForecast
#It was designed with the help of the tkinter library and the openweathermap api.

import tkinter as tk
import requests 


api_url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "#your api key"

MainWindow = tk.Tk()
MainWindow.title("Weather Forecast Program")
MainWindow.geometry("800x200")

MainText = tk.Label(MainWindow, text="Click on the city where you want to find out the weather forecast.", font="Times 21", bg="white")
MainText.pack()

LanguageText = tk.Label(MainWindow, text="Select the language.", font="Times 21", bg="white")
LanguageText.pack(pady=60, anchor="center")
LanguageText.pack()

#Language Settings
LangTr = "tr"
LangEng = "eng"
x = 0


def TurkishLanguage():
    global x
    x = 1
    MainText.config(text="Hava durumu tahminini öğrenmek istediğiniz şehre tıklayın.")
    LanguageText.config(text="Dil seçiniz.")
    LangTrButton.config(state="disabled")
    LangEngButton.config(state="normal")

def EnglishLanguage():
    global x
    x = 0
    MainText.config(text="Click on the city where you want to find out the weather forecast.")
    LanguageText.config(text="Select the language.")
    LangEngButton.config(state="disabled")
    LangTrButton.config(state="normal")

    
LangTrButton = tk.Button(MainWindow, text="Türkçe", command=TurkishLanguage)
LangTrButton.config(width=15, height=2)
LangTrButton.place(x=274, y= 150)


LangEngButton = tk.Button(MainWindow, text="English", command=EnglishLanguage)
LangEngButton.config(width=15, height=2)
LangEngButton.place(x=411, y= 150)



def IstanbulFunction():
    city = "Istanbul"
    params = {
            'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'eng' if x == 0 else 'tr'  # 'x' durumuna göre dil seçimi
    }

    response = requests.get(api_url, params=params)
    weather_data = response.json()

    NewWindow = tk.Toplevel(MainWindow)
    NewWindow.title("Istanbul")
    NewWindow.geometry("300x100")
    if x == 0:
    
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"Weather forecast for {city} : {description}").pack()
            tk.Label(NewWindow, text=f"Temprature: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Data could not be retrieved. Error: {response.status_code}").pack()

    else:
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"{city} için hava durumu: {description}").pack()
            tk.Label(NewWindow, text=f"Sıcaklık: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Veriler alınamadı. Hata: {response.status_code}").pack()


def AnkaraFunction():
    city = "Ankara"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'eng' if x == 0 else 'tr'
    }

    response = requests.get(api_url, params=params)
    weather_data = response.json()

    NewWindow = tk.Toplevel(MainWindow)
    NewWindow.title("Ankara")
    NewWindow.geometry("300x100")
    if x == 0:
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"Weather forecast for {city} : {description}").pack()
            tk.Label(NewWindow, text=f"Temprature: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Data could not be retrieved. Error: {response.status_code}").pack()

    else:        
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"{city} için hava durumu: {description}").pack()
            tk.Label(NewWindow, text=f"Sıcaklık: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Veriler alınamadı. Hata: {response.status_code}").pack()


def IzmirFunction():
    city = "Izmir"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'eng' if x == 0 else 'tr'
    }


    response = requests.get(api_url, params=params)
    weather_data = response.json()

    NewWindow = tk.Toplevel(MainWindow)
    NewWindow.title("Izmir")
    NewWindow.geometry("300x100")
    if x == 0:
    
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"Weather forecast for {city} : {description}").pack()
            tk.Label(NewWindow, text=f"Temprature: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Data could not be retrieved. Error: {response.status_code}").pack()

    else:
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"{city} için hava durumu: {description}").pack()
            tk.Label(NewWindow, text=f"Sıcaklık: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Veriler alınamadı. Hata: {response.status_code}").pack()


def TokatFunction():
    city = "Tokat"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'eng' if x == 0 else 'tr'
    }


    response = requests.get(api_url, params=params)
    weather_data = response.json()

    NewWindow = tk.Toplevel(MainWindow)
    NewWindow.title("Tokat")
    NewWindow.geometry("300x100")
    if x == 0:
    
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"Weather forecast for {city} : {description}").pack()
            tk.Label(NewWindow, text=f"Temprature: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Data could not be retrieved. Error: {response.status_code}").pack()

    else:
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"{city} için hava durumu: {description}").pack()
            tk.Label(NewWindow, text=f"Sıcaklık: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Veriler alınamadı. Hata: {response.status_code}").pack()


def MuglaFunction():
    city = "Mugla"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'eng' if x == 0 else 'tr'
    }

    response = requests.get(api_url, params=params)
    weather_data = response.json()

    NewWindow = tk.Toplevel(MainWindow)
    NewWindow.title("Mugla")
    NewWindow.geometry("300x100")
    if x == 0:
    
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"Weather forecast for {city} : {description}").pack()
            tk.Label(NewWindow, text=f"Temprature: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Data could not be retrieved. Error: {response.status_code}").pack()

    else:
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"{city} için hava durumu: {description}").pack()
            tk.Label(NewWindow, text=f"Sıcaklık: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Veriler alınamadı. Hata: {response.status_code}").pack()


def SamsunFunction():
    city = "Samsun"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'eng' if x == 0 else 'tr'
    }

    response = requests.get(api_url, params=params)
    weather_data = response.json()

    NewWindow = tk.Toplevel(MainWindow)
    NewWindow.title("Samsun")
    NewWindow.geometry("300x100")

    if x == 0:
    
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"Weather forecast for {city} : {description}").pack()
            tk.Label(NewWindow, text=f"Temprature: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Data could not be retrieved. Error: {response.status_code}").pack()

    else:
        if response.status_code == 200:
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            tk.Label(NewWindow, text=f"{city} için hava durumu: {description}").pack()
            tk.Label(NewWindow, text=f"Sıcaklık: {temp} °C").pack()
        else:
            tk.Label(NewWindow, text=f"Veriler alınamadı. Hata: {response.status_code}").pack()


#Istanbul
Istanbul = tk.Button(MainWindow, text="Istanbul", command=IstanbulFunction)
Istanbul.config(width=15, height=2)
Istanbul.place(x=0, y= 50)

#Ankara
Ankara = tk.Button(MainWindow, text="Ankara", command=AnkaraFunction)
Ankara.config(width=15, height=2)
Ankara.place(x=137, y= 50)

#Izmir
Izmir = tk.Button(MainWindow, text="Izmir", command=IzmirFunction)
Izmir.config(width=15, height=2)
Izmir.place(x=274, y= 50)

#Tokat
Tokat = tk.Button(MainWindow, text="Tokat", command=TokatFunction)
Tokat.config(width=15, height=2)
Tokat.place(x=411, y= 50)

#Mugla
Mugla = tk.Button(MainWindow, text="Mugla", command=MuglaFunction)
Mugla.config(width=15, height=2)
Mugla.place(x=548, y= 50)

#Samsun
Samsun = tk.Button(MainWindow, text="Samsun", command=SamsunFunction)
Samsun.config(width=15, height=2)
Samsun.place(x=685, y= 50)

MainWindow.mainloop()
