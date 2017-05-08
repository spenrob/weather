from django.shortcuts import get_object_or_404, render

from .models import Temp, WeatherDates, Precip, Severe
import datetime

def index(request):
    date = datetime.date.today()
    month = date.month
    day = date.day
    context = {
        'current_month': month,
        'current_day': day,
    }
    return render(request, 'weatherapp/index.html', context)


def result(request):
    form_month = request.POST['month'] #retrieving form results
    form_day = request.POST['day']
    form_year = request.POST['year']

    temperatureResults = temperatureCalculate(form_month, form_day, form_year, False)
    precipResults = precipCalculate(form_month, form_day, form_year, False)
    severeResults = severeCalculate(form_month, form_day, form_year, False)
    severeNames = ("Blowing Snow", "Drizzle", "Dush/Ash","Fog","Freezing Drizzle","Freezing Rain","Glaze/Rime","Ground Fog","Hail","Heavy Fog","High Winds","Ice Fog","Sleet","Mist","Rain","Smoke/Haze","Snow","Thunder","Tornado")

    context = {
        'minimum_temperature': temperatureResults[0],
        'average_temperature': temperatureResults[1],
        'maximum_temperature': temperatureResults[2],
        'precipitation': precipResults[0],
        'snow_depth': precipResults[1],
        'snow_fall': precipResults[2],
        'month': form_month,
        'day': form_day,
        'year': form_year,
        'severe' : severeResults,
        'severeNames' : severeNames,
        'single_bool' : False
    }
    return render(request, 'weatherapp/result.html', context)


def weatherTypeResponse(request):
    form_type = request.POST['select_type']
    form_year = request.POST['year']

    weather_set = Severe.objects.filter(**{form_type: 1})  # get every record where the weather type of interest was detected
    id_set = WeatherDates.objects.filter(id__in=weather_set, year__gte=form_year)

    context={
        'weather_type': form_type,
        'start_year': form_year,
        'id_list': id_set
    }

    return render(request, 'weatherapp/searchByWeatherTypeResult.html', context)


def searchByWeatherType(request):
    return render(request, 'weatherapp/searchByWeatherType.html')


def singleResult(request):
    form_month = request.POST['month']  # retrieving form results
    form_day = request.POST['day']
    form_year = request.POST['year']

    temperatureResults = temperatureCalculate(form_month, form_day, form_year, True)
    precipResults = precipCalculate(form_month, form_day, form_year, True)
    severeResults = severeCalculate(form_month, form_day, form_year, True)
    severeNames = ("Blowing Snow", "Drizzle", "Dush/Ash", "Fog", "Freezing Drizzle", "Freezing Rain", "Glaze/Rime", "Ground Fog", "Hail", "Heavy Fog", "High Winds", "Ice Fog", "Sleet", "Mist", "Rain", "Smoke/Haze", "Snow", "Thunder", "Tornado")


    context={
        'minimum_temperature': temperatureResults[0],
        'average_temperature': temperatureResults[1],
        'maximum_temperature': temperatureResults[2],
        'precipitation': precipResults[0],
        'snow_depth': precipResults[1],
        'snow_fall': precipResults[2],
        'month': form_month,
        'day': form_day,
        'year': form_year,
        'severe' : severeResults,
        'severeNames' : severeNames,
        'single_bool' : True
    }
    for key, value in context.items():
        print(str(key) + "->" + str(value))
    return render(request, 'weatherapp/result.html', context)


def arrestDisplay(request):
    from bs4 import BeautifulSoup
    import urllib.request

    url = "http://mugshots.com/US-Counties/Georgia/Fulton-County-GA/"
    r = urllib.request.urlopen(url)
    soup = BeautifulSoup(r, "html.parser")

    names = soup.find_all("div", class_="label")

    names_list = []

    for name in names:
        names_list.append(name.get_text())

    context = {
        'names_list': names_list,
    }

    return render(request, 'weatherapp/arrestDisplay.html', context)


def temperatureCalculate(inputMonth, inputDay, inputYear, single_bool):

    # single_bool = true if searching for a single date
    if single_bool:
        idSet = WeatherDates.objects.filter(month=inputMonth,
                                            day=inputDay,
                                            year=inputYear)
    else:
        idSet = WeatherDates.objects.filter(month=inputMonth,
                                        day=inputDay,
                                        year__gte=inputYear)  # QuerySet containing pk value of every entry on month/day

    tempSet = Temp.objects.filter(id__in=idSet)  # using idSet to retrieve every Temp object entry for month/day

    minTemp = 0  # running totals of the temperature values
    averageTemp = 0
    maxTemp = 0

    minTempCount = 0  # counts to keep track of how many non-null entries
    averageTempCount = 0
    maxTempCount = 0

    for entry in tempSet:
        if entry.tmin > -1000:  # database uses -9999 as null value.. -1000 is arbitrary number higher than -9999, lower than feasible temp value
            minTemp += entry.tmin
            minTempCount += 1
        if entry.tavg > -1000:
            averageTemp += entry.tavg
            averageTempCount += 1
        if entry.tmax > -1000:
            maxTemp += entry.tmax
            maxTempCount += 1

    if minTempCount == 0:    #preventing division by 0 error, providing more accurate results
        minTemp = "No data"
    else:
        minTemp = round(minTemp/minTempCount, 1)  # average will be equal to the final total, divided by the count

    if averageTempCount ==0:
        averageTemp = "No data"
    else:
        averageTemp = round(averageTemp/averageTempCount, 1)

    if maxTempCount == 0:
        maxTemp = "No data"
    else:
        maxTemp = round(maxTemp/maxTempCount,1)

    return minTemp, averageTemp, maxTemp


def precipCalculate(input_month, input_day, input_year, single_bool):
    if single_bool:
        id_set = WeatherDates.objects.filter(month=input_month,
                                            day=input_day,
                                            year=input_year)
    else:
        id_set = WeatherDates.objects.filter(month=input_month,
                                            day=input_day,
                                            year__gte=input_year)

    precip_set = Precip.objects.filter(id__in=id_set)

    precipitation = 0
    snow_depth = 0
    snow_fall = 0

    precipitation_count = 0
    snow_depth_count = 0
    snow_fall_count = 0

    for entry in precip_set:
        if entry.precipitation > -1000:  # database uses -9999 as null value.. -1000 is arbitrary number higher than -9999, lower than feasible temp value
            precipitation += entry.precipitation
            precipitation_count += 1
        if entry.snowdepth > -1000:
            snow_depth += entry.snowdepth
            snow_depth_count += 1
        if entry.snowfall > -1000:
            snow_fall += entry.snowfall
            snow_fall_count += 1

    if precipitation_count == 0: # preventing division by 0 error, providing more accurate results
        precipitation = "No data"
    else:
        precipitation = round(precipitation/precipitation_count,1)

    if snow_depth_count == 0:
        snow_depth = "No data"
    else:
        snow_depth = round(snow_depth/snow_depth_count,1)

    if snow_fall_count == 0:
        snow_fall = "No data"
    else:
        snow_fall = round(snow_fall/snow_fall_count,1)

    return precipitation, snow_depth, snow_fall


def severeCalculate(inputMonth, inputDay, inputYear, single_bool):
    if single_bool:
        idSet = WeatherDates.objects.filter(month=inputMonth,
                                            day=inputDay,
                                            year=inputYear)
    else:
        idSet = WeatherDates.objects.filter(month=inputMonth,
                                            day=inputDay,
                                            year__gte=inputYear)
    severeSet = Severe.objects.filter(id__in=idSet)

    blowingsnow_count = 0
    drizzle_count = 0
    dust_ash_count = 0
    fog_count = 0
    freezingdrizzle_count = 0
    freezingrain_count = 0
    glaze_rime_count = 0
    groundfog_count = 0
    hail_count = 0
    heavyfog_count = 0
    highwinds_count = 0
    icefog_count = 0
    sleet_count = 0
    mist_count = 0
    rain_count = 0
    smokehaze_count = 0
    snow_count = 0
    thunder_count = 0
    tornado_count = 0

    for entry in severeSet:
        if entry.blowingsnow == 1:
            blowingsnow_count += 1

        if entry.drizzle == 1:
            drizzle_count += 1

        if entry.dust_ash == 1:
            dust_ash_count += 1

        if entry.fog == 1:
            fog_count += 1

        if entry.freezingdrizzle== 1:
            freezingdrizzle_count += 1

        if entry.freezingrain == 1:
            freezingrain_count += 1

        if entry.glaze_rime == 1:
            glaze_rime_count += 1

        if entry.groundfog == 1:
            groundfog_count += 1

        if entry.hail == 1:
            hail_count += 1
        if entry.heavyfog== 1:
            heavyfog_count += 1

        if entry.highwinds == 1:
            highwinds_count += 1

        if entry.icefog == 1:
            icefog_count += 1

        if entry.sleet== 1:
            sleet_count += 1

        if entry.mist== 1:
            mist_count += 1

        if entry.rain == 1:
            rain_count += 1

        if entry.smokehaze == 1:
            smokehaze_count += 1

        if entry.snow == 1:
            snow_count += 1

        if entry.thunder == 1:
            thunder_count += 1

        if entry.tornado == 1:
            tornado_count += 1

    return blowingsnow_count, drizzle_count,dust_ash_count,fog_count,freezingdrizzle_count,freezingrain_count, glaze_rime_count,groundfog_count,hail_count,heavyfog_count,highwinds_count,icefog_count,sleet_count,mist_count,rain_count,smokehaze_count,snow_count,thunder_count,tornado_count


