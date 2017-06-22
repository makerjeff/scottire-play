#!/usr/bin/env python
# Foundations of Python Network Programming - CH1 - search1.py

# NOTE: Does not work, new API requires API key.

from googlemaps import Client as GoogleMaps

address = '207 N. Defiance St, Archbold, OH'
print GoogleMaps().address_to_latlng(address)

