import logging
from geopy.geocoders import Nominatim
from geopy import distance

# Get coordinates of place name
# If cannot founf, return None
def get_place_coordinate(place_name):
    geolocator = Nominatim(user_agent="promoinsta")
    location = geolocator.geocode(place_name)

    if location:
        # No error, return coordinates
        return (location.latitude, location.longitude)
    else:
        # Can't found coordinates, return None
        return None

# Get distance from two points coordinates
# if one of coordinate is None, return None
def get_coordinates_distance(coords_1, coords_2, units='km'):
    # If coordinates exist calc distance, else return None
    if coords_1 and coords_2:
        if units == 'km':
            return distance.distance(coords_1, coords_2).km
        elif units == 'miles':
            return distance.distance(coords_1, coords_2).miles
        else:
            logging.error("Unknown units selected.")
            return None
    else:
        # logging.warning("some coordinates does not exist.")
        return None

# Get distance between places names
# If cannont found, return None
def get_places_distance(place_1, place_2, units='km'):
    # Get distance between place 2 and place 2
    return get_coordinates_distance(get_place_coordinate(place_1), get_place_coordinate(place_2), units)

# print(get_places_distance("Москва", "ЖК Зиларт"))