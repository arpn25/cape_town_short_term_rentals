import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directories
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

# Specific files
LISTINGS_FILE = os.path.join(RAW_DATA_DIR, "listings.csv")
CALENDAR_FILE = os.path.join(RAW_DATA_DIR, "calendar.csv.gz")
GDF_FILE = os.path.join(RAW_DATA_DIR,"neighbourhoods.geojson") 