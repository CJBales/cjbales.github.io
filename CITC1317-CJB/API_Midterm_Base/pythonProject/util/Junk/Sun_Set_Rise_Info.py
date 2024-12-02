from datetime import datetime


class Sun_Set_Rise_Info():

    def __init__(self):
        pass

    def is_nighttime(self,current_time, sunrise, sunset):
        current_time = datetime.fromisoformat(current_time)
        sunrise = datetime.fromisoformat(sunrise)
        sunset = datetime.fromisoformat(sunset)

        # Nighttime is either before sunrise or after sunset
        return current_time <= sunrise or current_time >= sunset

