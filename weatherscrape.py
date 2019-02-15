##API Weather Parser##
##KoinuKoji##
##Thanks to Michael Dereszynski and Peter Tucker for helping me learn!##
# This pulls back date, zipcode, lat/lon, weather (based on icon), temperature high and low. More can be added!
# You will need an API Key from DarkSky at https://darksky.net/dev - Free for 1000 pings

import json
import requests
import csv
import datetime as dt

# API INFO
key = YOURKEYHERE  
base_url = 'https://api.darksky.net/forecast/' + key

#File Setup 
outputfile = open('weatherdata.csv','a', newline='')
outputwriter = csv.writer(outputfile)

###Zip/Lat/Lon file - Using a CSV pulled from census.gov for zip codes to convert to Latitude/Longitude###
def loopLocations():
    file = open(GEORESULTSFILE,'r')
    with file:
        reader = csv.DictReader(file)
        for row in reader:
            getWeather(row['Zip'],row['Lat'],row['Lon'])

###Get info out of JSON###
def parseWeather(zipcode, obj):
    today = dt.date.today()
    lat = obj['latitude']
    lon = obj['longitude']
    weather = obj['daily']['icon']
    tempHigh = obj['daily']['data'][0]['temperatureHigh']
    tempLow = obj['daily']['data'][0]['temperatureLow']
    outputwriter.writerow([today, zipcode, lat, lon, weather, tempHigh, tempLow])

###Ping API for JSON Data###
def getWeather(zipcode, lat, lon):
    resp = requests.get(base_url + lat +','+ lon)
    obj = resp.json()
    parseWeather(zipcode, obj)

loopLocations()
