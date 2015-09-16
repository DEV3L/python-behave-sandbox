"""
This file helped clarify for me how Python handles class and instance variables.

Instances of a class refer to the class value until modified on the instance

This file can simply be ran from the console: 
python class_variable_test.py
"""

class SomeClass():
    a_field = None


def main():
    print("classfield: " + str(SomeClass.a_field)) # None

    instanceOne = SomeClass()
    print("instance_field_1: " + str(instanceOne.a_field)) # None

    instanceOne.a_field = "One"
    print("instance_field_1: " + instanceOne.a_field) # One
    print("classfield: " + str(SomeClass.a_field)) # None

    SomeClass.a_field = "Classfield"
    print("classfield: " + SomeClass.a_field) # Classfield
    print("instance_field_1: " + instanceOne.a_field) # One

    instanceTwo = SomeClass()
    print("instance_field_2: " + instanceTwo.a_field) # Classfield

    SomeClass.a_field = "Classfield_Other"
    print("instance_field_2: " + instanceTwo.a_field) # Classfield_Other

    instanceTwo.a_field = "Two"
    print("instance_field_2: " + instanceTwo.a_field) # Two
    print("classfield: " + SomeClass.a_field) # Classfield


if __name__ == '__main__':
    main()
