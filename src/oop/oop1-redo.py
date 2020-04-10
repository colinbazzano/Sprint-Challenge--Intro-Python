# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# BASE CLASS


class Vehicle:
    pass

# Sub Class 1 level deep


class FlightVehicle(Vehicle):
    pass


# Sub Class 2 levels deep
class Starship(FlightVehicle):
    pass
# Sub Class 2 levels deep


class Airplane(FlightVehicle):
    pass
# Sub Class 1 level deep


class GroundVehicle(Vehicle):
    pass
# Sub Class 2 levels deep


class Car(GroundVehicle):
    pass
# Sub Class 2 levels deep


class Motorcycle(GroundVehicle):
    pass
