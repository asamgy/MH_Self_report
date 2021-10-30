# File name: weather_mapping.py
# Author: Vicki Liu


lightrain = "light rain"
heavyrain = "heavy rain"
lightsnow = "light snow"
heavysnow = "heavy snow"
lightice = "light ice"
heavyice = "heavy ice"
lightfog = "light fog"
heavyfog = "heavy fog"
lightsmoke = "light smoke"
heavysmoke = "heavy smoke"
dust = "dust"
thunderstorm = "thunderstorm"
heavycloudy = "heavy cloudy"
lightcloudy = "light cloudy"
storm= "storm"
tornado = "tornado"
unk = "unk"
clear = "clear"

weatherMapping = {
	"Light Drizzle": lightrain,
	"Heavy Drizzle": heavyrain,
	"Light Rain": lightrain,
	"Heavy Rain": heavyrain,
	"Light Snow": lightsnow,
	"Heavy Snow": heavysnow,
	"Drizzle": lightrain,
	"Light Snow Grains": lightsnow,
	"Heavy Snow Grains": heavysnow,
	"Light Ice Crystals": lightice,
	"Heavy Ice Crystals": heavyice,
	"Light Ice Pellets": lightice,
	"Heavy Ice Pellets": heavyice,
	"Light Hail": lightice,
	"Heavy Hail": heavyice,
	"Light Mist": lightfog,
	"Heavy Mist": heavyfog,
	"Light Fog": lightfog,
	"Heavy Fog": heavyfog,
	"Mist":lightfog,
	"Fog": lightfog,
	"Rain": lightrain,
	"Light Fog Patches": lightfog,
	"Heavy Fog Patches": heavyfog,
	"Smoke": lightsmoke,
	"Light Smoke": lightsmoke,
	"Heavy Smoke": heavysmoke,
	"Light Volcanic Ash": lightsmoke,
	"Heavy Volcanic Ash": heavysmoke,
	"Light Widespread Dust": dust,
	"Heavy Widespread Dust": dust,
	"Light Sand": dust,
	"Heavy Sand": dust,
	"Light Haze": lightfog,
	"Heavy Haze": heavyfog,
	"Light Spray": lightrain,
	"Heavy Spray": heavyrain,
	"Light Dust Whirls": dust,
	"Heavy Dust Whirls": dust,
	"Light Sandstorm": dust,
	"Heavy Sandstorm": dust,
	"Light Low Drifting Snow": lightsnow,
	"Heavy Low Drifting Snow": heavysnow,
	"Light Low Drifting Widespread Dust": dust,
	"Heavy Low Drifting Widespread Dust": dust,
	"Light Low Drifting Sand": dust,
	"Heavy Low Drifting Sand": dust,
	"Light Blowing Snow": lightsnow,
	"Heavy Blowing Snow": heavysnow,
	"Snow": lightsnow,
	"Light Blowing Widespread Dust": dust,
	"Heavy Blowing Widespread Dust": dust,
	"Light Blowing Sand": dust,
	"Heavy Blowing Sand": dust,
	"Light Rain Mist": lightrain,
	"Heavy Rain Mist": heavyrain,
	"Light Rain Showers": lightrain,
	"Heavy Rain Showers": heavyrain,
	"Light Snow Showers": lightsnow,
	"Heavy Snow Showers": heavysnow,
	"Light Snow Blowing Snow Mist": lightsnow,
	"Heavy Snow Blowing Snow Mist": heavysnow,
	"Light Ice Pellet Showers": lightice,
	"Heavy Ice Pellet Showers": heavyice,
	"Light Hail Showers": lightice,
	"Heavy Hail Showers": heavyice,
	"Light Small Hail Showers": lightice,
	"Heavy Small Hail Showers": heavyice,
	"Thunderstorm": thunderstorm,
	"Light Thunderstorm": thunderstorm,
	"Heavy Thunderstorm": thunderstorm,
	"Light Thunderstorms and Rain": lightrain,
	"Heavy Thunderstorms and Rain": heavyrain,
	"Light Thunderstorms and Snow": lightsnow,
	"Heavy Thunderstorms and Snow": heavysnow,
	"Light Thunderstorms and Ice Pellets": lightice,
	"Heavy Thunderstorms and Ice Pellets": heavyice,
	"Light Thunderstorms with Hail": lightice,
	"Heavy Thunderstorms with Hail": heavyice,
	"Light Thunderstorms with Small Hail": lightice,
	"Heavy Thunderstorms with Small Hail": heavyice,
	"Light Freezing Drizzle": lightice,
	"Heavy Freezing Drizzle": heavyice,
	"Light Freezing Rain":lightice,
	"Heavy Freezing Rain": heavyice,
	"Light Freezing Fog": lightfog,
	"Heavy Freezing Fog": heavyfog,
	"Patches of Fog": lightfog,
	"Shallow Fog": lightfog,
	"Partial Fog": lightfog,
	"Overcast": heavycloudy,
	"Clear": clear,
	"Partly Cloudy": lightcloudy,
	"Mostly Cloudy": heavycloudy,
	"Scattered Clouds": lightcloudy,
	"Small Hail": lightice,
	"Squalls": storm,
	"Funnel Cloud": tornado,
	"Unknown Precipitation": unk,
	"Unknown": unk,
	"Haze": lightfog,
	"Ice Pellets": lightice

}
