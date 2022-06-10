from flask import jsonify
import numpy as np


# Constants
max_range = 1000 # in meters

def distance(coordinate_1:tuple[float,float], coordinate_2:tuple[float, float]) -> float:
    """Measure haversine distance between two coordinate.
    
    Note:
    - coordinate : tuple of latitude and longitude, ex. (3.10326051, 91.23206407)
    Reference: https://en.wikipedia.org/wiki/Haversine_formula
    """
    # constants
    earth_radius = 6371000 # in meters
    
    # unpack and convert params to radian
    lat_1, long_1 = np.radians(coordinate_1)
    lat_2, long_2 = np.radians(coordinate_2)
    
    d_lat = lat_2 - lat_1
    d_long = long_2 - long_1
    
    # calculate and return distance
    return 2 * earth_radius * np.arcsin (np.sqrt(
        np.sin(d_lat/2) ** 2
        + np.cos(lat_1) * np.cos(lat_2) * np.sin(d_long/2) ** 2))

# Trigger function
def calculate_trigger(
        coordinate_1:tuple[float,float],
        coordinate_2:tuple[float,float],
        max_range:float) -> bool:
    """Calculate if distance between two coordinates is 
    over the max range and return True if distance is more
    than max_range"""
    print(distance(coordinate_1, coordinate_2))
    return distance(coordinate_1, coordinate_2) > max_range

def compute_trigger(request):
    """Wrapper for functions below"""

    content_type = request.headers['content-type']

    if content_type == 'application/json':
        request_json = request.get_json(silent=True)
    else:
        raise ValueError("JSON is invalid")

    coordinate_1 = request_json['prediction']
    coordinate_2 = request_json['cur_position']

    result = {"too_far?": str(calculate_trigger(coordinate_1, coordinate_2, max_range))}

    return jsonify(result)