from enum import Enum, auto, unique

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

@unique
class Status(Enum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500

class Planet(Enum):
    MERCURY = (3.3e23, 2.4e6)
    EARTH = (6.0e24, 6.4e6)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    @property
    def gravity(self):
        return 6.674e-11 * self.mass / self.radius ** 2

if __name__ == "__main__":
    print(Color.RED.name, Color.RED.value)
    print(Status(404).name)
    print("members:", [m.name for m in Color])
    print("earth heavier pull:", Planet.EARTH.gravity > Planet.MERCURY.gravity)
    try:
        Status.OK.value = 201
    except AttributeError as e:
        print("immutable:", e)
