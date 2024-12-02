from math import radians, cos, sin, sqrt, atan2

class ISS_Info():


    def __init__(self):
        pass
    
    def haversine(self,lat1, lon1, lat2, lon2):
        """
        Calculates the great-circle distance between two points on the Earth's surface
        given their latitude and longitude in degrees. This is known as the Haversine formula.

        lat1, lon1: Latitude and Longitude of the first point (in degrees)
        lat2, lon2: Latitude and Longitude of the second point (in degrees)

        Returns the distance between the two points in kilometers.
        """

        # The radius of the Earth in kilometers (approximate value)
        R = 6371.0  # This value can be used for calculating distance in kilometers

        # Step 2: Convert latitude and longitude from degrees to radians.
        # Why? Because trigonometric functions like sin() and cos() use radians, not degrees.
        # Radians are another way to measure angles. To use trigonometry, we need to convert degrees to radians.
        lat1_rad = radians(lat1)  # Convert latitude of the first point to radians
        lon1_rad = radians(lon1)  # Convert longitude of the first point to radians
        lat2_rad = radians(lat2)  # Convert latitude of the second point to radians
        lon2_rad = radians(lon2)  # Convert longitude of the second point to radians

        # Step 3: Calculate the difference in latitude and longitude between the two points.
        # This gives us how far apart the two points are in terms of angles.
        dlat = lat2_rad - lat1_rad  # Difference in latitude (in radians)
        dlon = lon2_rad - lon1_rad  # Difference in longitude (in radians)

        # Step 4: Apply the Haversine formula.
        # The Haversine formula uses the trigonometric functions sine (sin) and cosine (cos).
        # We are essentially calculating the shortest distance between two points on a sphere
        # (in this case, the Earth) by using the difference in latitudes and longitudes.

        # Haversine part 1:
        # sin(dlat / 2)**2 is calculating the square of the sine of half the latitude difference
        # sin(dlon / 2)**2 is calculating the square of the sine of half the longitude difference
        # cos(lat1_rad) * cos(lat2_rad) helps to adjust for the spherical shape of the Earth
        a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2

        # Step 5: Calculate the angular distance using the inverse trigonometric function atan2().
        # atan2() is a special function that calculates the angle between two points.
        # sqrt() is used to calculate the square root of a value.
        # The formula 2 * atan2(sqrt(a), sqrt(1 - a)) gives us the central angle between the points in radians.
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Step 6: Calculate the distance.
        # The distance is simply the central angle (c) multiplied by the Earth's radius (R).
        # This gives us the great-circle distance between the two points in kilometers.
        distance = R * c  # Final distance in kilometers

        # Return the calculated distance
        return distance