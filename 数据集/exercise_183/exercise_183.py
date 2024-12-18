from math import sqrt

# A function that calculates distance to horizon in meters given height in meters
def horizon_distance(h):
    R = 6_371_000
    return sqrt(2 * R * h + h ** 2)


airplane_height = 12_000
d_horizon = horizon_distance(airplane_height)
print(
    f"You can see ~{round(d_horizon / 1000)}km from a commercial flight.")