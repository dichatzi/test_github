import pandas as pd

class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __call__(self, age):
        print(f"{self.name} {self.surname} is {age} years old...")


if __name__ == "__main__":
    print("Starting code execution")

    Dimitris = People(name="Dimitris", surname="Chatzigiannis")
    Dimitris(38)

    Michalis = People(name="Michalis", surname="Kazdaglis")
    Michalis(40)