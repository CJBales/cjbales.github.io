from API.util.Runescape_HiScores_URL_Templates import REVERSED_API_ENDPOINTS_NEEDING_JSON_PARSE

DUSK_DAWN_URL = "https://api.sunrise-sunset.org/json?lat={1}&lng={2}&date={3}&tzid={0}"

ISS_LOCATION_URL = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps={0}&units=miles"

DAILY_WEATHER_URL = "https://api.open-meteo.com/v1/forecast?latitude=36.5484&longitude=-82.5618&hourly=cloud_cover_high&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York"