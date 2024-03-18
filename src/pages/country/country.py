import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

from taipy.gui import Markdown

from data.data import data
default_country = 'Afghanistan'

geolocator = Nominatim(user_agent="my_app")


def country_init(data,country):
    grouped_by_country = data.groupby('country')
    data_by_specific_country = grouped_by_country.get_group(country)

    return data_by_specific_country
def get_area(row):
    location = geolocator.reverse((row['latitude'], row['longitude']), exactly_one=True)
    return location.address
data_by_specific_country = country_init(data,default_country)

data_by_specific_country['Area'] =  data_by_specific_country.apply(get_area, axis=1)

def on_change_country(state):
    state.data_by_specific_country = country_init(data,state.default_country)

    state.data_by_specific_country['Area'] =  state.data_by_specific_country.apply(get_area, axis=1)

country_md = Markdown("pages/country/country.md")