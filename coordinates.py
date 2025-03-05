# coordinates.py

BROOKLYN_COORDINATES = {
    ('BROOKLYN', 'BATH BEACH'): [-73.9946, 40.5968],
    ('BROOKLYN', 'BAY RIDGE'): [-74.0306, 40.6247],
    ('BROOKLYN', 'BEDFORD STUYVESANT'): [-73.9417, 40.6883],
    ('BROOKLYN', 'BENSONHURST'): [-73.9854, 40.6078],
    ('BROOKLYN', 'BERGEN BEACH'): [-73.8883, 40.6181],
    ('BROOKLYN', 'BOERUM HILL'): [-73.9907, 40.6850],
    ('BROOKLYN', 'BOROUGH PARK'): [-73.9937, 40.6327],
    ('BROOKLYN', 'BRIGHTON BEACH'): [-73.9618, 40.5768],
    ('BROOKLYN', 'BROOKLYN HEIGHTS'): [-73.9941, 40.6943],
    ('BROOKLYN', 'BROWNSVILLE'): [-73.9156, 40.6634],
    ('BROOKLYN', 'BUSH TERMINAL'): [-74.0087, 40.6506],
    ('BROOKLYN', 'BUSHWICK'): [-73.9214, 40.7000],
    ('BROOKLYN', 'CANARSIE'): [-73.8977, 40.6370],
    ('BROOKLYN', 'CARROLL GARDENS'): [-73.9949, 40.6814],
    ('BROOKLYN', 'CLINTON HILL'): [-73.9680, 40.6922],
    ('BROOKLYN', 'COBBLE HILL'): [-73.9974, 40.6869],
    ('BROOKLYN', 'COBBLE HILL-WEST'): [-73.9974, 40.6869],
    ('BROOKLYN', 'CONEY ISLAND'): [-73.9835, 40.5771],
    ('BROOKLYN', 'CROWN HEIGHTS'): [-73.9515, 40.6673],
    ('BROOKLYN', 'CYPRESS HILLS'): [-73.8833, 40.6883],
    ('BROOKLYN', 'DOWNTOWN-FULTON FERRY'): [-73.9905, 40.7031],
    ('BROOKLYN', 'DOWNTOWN-FULTON MALL'): [-73.9879, 40.6923],
    ('BROOKLYN', 'DOWNTOWN-METROTECH'): [-73.9879, 40.6923],
    ('BROOKLYN', 'DYKER HEIGHTS'): [-74.0118, 40.6247],
    ('BROOKLYN', 'EAST NEW YORK'): [-73.8812, 40.6706],
    ('BROOKLYN', 'FLATBUSH-CENTRAL'): [-73.9618, 40.6344],
    ('BROOKLYN', 'FLATBUSH-EAST'): [-73.9404, 40.6508],
    ('BROOKLYN', 'FLATBUSH-LEFFERTS GARDEN'): [-73.9531, 40.6577],
    ('BROOKLYN', 'FLATBUSH-NORTH'): [-73.9731, 40.6452],
    ('BROOKLYN', 'FLATLANDS'): [-73.9182, 40.6317],
    ('BROOKLYN', 'FORT GREENE'): [-73.9743, 40.6900],
    ('BROOKLYN', 'GERRITSEN BEACH'): [-73.9244, 40.5870],
    ('BROOKLYN', 'GOWANUS'): [-73.9971, 40.6714],
    ('BROOKLYN', 'GRAVESEND'): [-73.9771, 40.5978],
    ('BROOKLYN', 'GREENPOINT'): [-73.9528, 40.7276],
    ('BROOKLYN', 'KENSINGTON'): [-73.9736, 40.6406],
    ('BROOKLYN', 'MADISON'): [-73.9656, 40.6081],
    ('BROOKLYN', 'MANHATTAN BEACH'): [-73.9579, 40.5771],
    ('BROOKLYN', 'MARINE PARK'): [-73.9396, 40.6099],
    ('BROOKLYN', 'MIDWOOD'): [-73.9682, 40.6181],
    ('BROOKLYN', 'MILL BASIN'): [-73.9133, 40.6205],
    ('BROOKLYN', 'NAVY YARD'): [-73.9743, 40.6900],
    ('BROOKLYN', 'OCEAN HILL'): [-73.9156, 40.6634],
    ('BROOKLYN', 'OCEAN PARKWAY-NORTH'): [-73.9682, 40.6181],
    ('BROOKLYN', 'OCEAN PARKWAY-SOUTH'): [-73.9682, 40.6181],
    ('BROOKLYN', 'OLD MILL BASIN'): [-73.9094, 40.6156],
    ('BROOKLYN', 'PARK SLOPE'): [-73.9837, 40.6729],
    ('BROOKLYN', 'PARK SLOPE SOUTH'): [-73.9837, 40.6729],
    ('BROOKLYN', 'PROSPECT HEIGHTS'): [-73.9622, 40.6788],
    ('BROOKLYN', 'RED HOOK'): [-74.0134, 40.6794],
    ('BROOKLYN', 'SEAGATE'): [-74.0025, 40.5777],
    ('BROOKLYN', 'SHEEPSHEAD BAY'): [-73.9586, 40.5908],
    ('BROOKLYN', 'SPRING CREEK'): [-73.8638, 40.6611],
    ('BROOKLYN', 'SUNSET PARK'): [-74.0048, 40.6458],
    ('BROOKLYN', 'WILLIAMSBURG-CENTRAL'): [-73.9606, 40.7140],
    ('BROOKLYN', 'WILLIAMSBURG-EAST'): [-73.9519, 40.7130],
    ('BROOKLYN', 'WILLIAMSBURG-NORTH'): [-73.9599, 40.7181],
    ('BROOKLYN', 'WILLIAMSBURG-SOUTH'): [-73.9579, 40.7074],
    ('BROOKLYN', 'WINDSOR TERRACE'): [-73.9840, 40.6626],
    ('BROOKLYN', 'WYCKOFF HEIGHTS'): [-73.9327, 40.7004]
}

def get_brooklyn_coordinates(neighborhood):
    """Retrieves Brooklyn coordinates based on Neighborhood."""
    if ('BROOKLYN', neighborhood) in BROOKLYN_COORDINATES:
        return BROOKLYN_COORDINATES[('BROOKLYN', neighborhood)]
    else:
        print(f"Warning: Coordinates not found for Brooklyn, {neighborhood}. Defaulting to Brooklyn Center.")
        return [-73.9442, 40.6782]  # Brooklyn default