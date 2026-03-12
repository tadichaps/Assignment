# Define a Dog class
class Dog:
    def make_sound(self):
        return "Woof! 🐶"


# Define a Cat class
class Cat:
    def make_sound(self):
        return "Meow! 🐱"


# Function that works with any object
# that has a make_sound() method
def process_sound(sound_object):
    """
    This function expects an object that
    implements a make_sound() method.
    It does NOT care about the object's type.
    """
    print(sound_object.make_sound())


# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Pass both objects to the same function
process_sound(dog)   # Output: Woof! 🐶
process_sound(cat)   # Output: Meow! 🐱