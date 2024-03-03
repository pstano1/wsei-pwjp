import datetime
from math import pi
from abc import ABC, abstractmethod

def greetUser() -> str:
    output: str = "Cześć {}!\nTwoje imię ma {} liter i zaczyna się od {} Teraz masz {} lat, a za rok będzie to {}. Rok urodzenia to {}"
    name: str = str(input())
    age: int = int(input())
    birthYear = datetime.date.today().year - age
    return output.format(name, len(name), name[0], age, age + 1, birthYear)

# print(greetUser())

def checkUser(beveragePrice: int) -> str:
    age: int = int(input())
    walletWorth: int = int(input())

    if (age < 18 and walletWorth < beveragePrice):
        return "brakuje Ci {} lat oraz {} zł".format(18 - age, beveragePrice - walletWorth)
    if (age < 18 and walletWorth >= beveragePrice):
        return "brakuje Ci {} lat ale masz wystarczającą ilość pieniędzy".format(18 - age)
    if (age >= 18 and walletWorth < beveragePrice):
       return "jesteś pełnoletni ale brakuje Ci {} zł".format(beveragePrice - walletWorth)

    return "jesteś pełnoletni i masz wystarczającą ilość pieniędzy"

# print(checkUser(20))

def taxCalculator(grossIncome: float, isMonthly: bool) -> float:
    if (isMonthly):
        grossIncome *= 12
    
    if (grossIncome <= 120000):
        return grossIncome * 0.88
    
    grossIncome -= 120000
    return grossIncome * 0.68 + 120000 * 0.88

# print(taxCalculator(float(input), float(input())))

class Shape(ABC):
    @abstractmethod
    def getArea(self) -> float:
        pass

    def getUserInput(self) -> None:
        pass


class Circle(Shape):
    def __init__(self, radius: float = 0) -> None:
        self.radius = radius

    def getArea(self) -> float:
        if (self.radius < 0):
            return -1.0
        return pi * pow(self.radius, 2)
    
    def getUserInput(self) -> None:
        self.radius = float(input())
    

class Triangle(Shape):
    def __init__(self, baseLength: float = 0, height: float = 0) -> None:
        self.baseLength = baseLength
        self.height = height

    def getArea(self) -> float:
        if (self.baseLength < 0 or self.height < 0):
            return -1.0
        return (self.baseLength * self.height) / 2
    
    def getUserInput(self) -> None:
        self.baseLength = float(input())
        self.height = float(input())
    

class Rectangle(Shape):
    def __init__(self, baseLength: float = 0, height: float = 0) -> None:
        self.baseLength = baseLength
        self.height = height
    
    def getArea(self) -> float:
        if (self.baseLength < 0 or self.height < 0):
            return -1.0
        return self.baseLength * self.height
    
    def getUserInput(self) -> None:
        self.baseLength = float(input())
        self.height = float(input())


class ShapeAreaCalculator:
    supportedShapes: list[str] = ["circle", "triangle", "rectangle"]

    def __init__(self) -> None:
        self.userSelection: str = ""
        self.selectedShape: Shape

    def getUserInput(self) -> None:
        while (self.userSelection not in self.supportedShapes):
           self.userSelection = str(input())

        if (self.userSelection == "circle"):
            self.selectedShape = Circle()
            self.selectedShape.getUserInput()
            return
        
        if (self.userSelection == "triangle"):
            self.selectedShape = Triangle()
            self.selectedShape.getUserInput()
            return
        
        self.selectedShape = Rectangle()
        self.selectedShape.getUserInput()
        return
    
    def calculateArea(self) -> float:
        return self.selectedShape.getArea()


def t() -> None:
    calculator = ShapeAreaCalculator()

    calculator.getUserInput()
    print("Pole figury {} wynosi: {}".format(calculator.userSelection, calculator.calculateArea()))

t()

monthlyExpenses: dict[str, float] = {
    "jan": 2000,
    "feb": 1950.75,
    "mar": 3000,
    "apr": 2500,
    "may": 2300.50,
}

def checkExpenses(monthlyExpenses: dict[str, float]) -> None:
    sum: float = 0
    min: float = 0
    max: float = 0
    for month, value in monthlyExpenses.items():
        sum += float(value)
        if (min < value):
            min = value
        if (max < value):
            max = value

    avg: float = sum / len(monthlyExpenses)
    items = list(monthlyExpenses.items())
    lastKey = items[-1][0]
    if monthlyExpenses[lastKey] > avg:
        print("zacznij oszczędzać")
    else:
        print("jesteś bezpieczny")

    for month, value in monthlyExpenses.items():
        if value > avg:
            print("{}: {}".format(month, value))
   

# checkExpenses(monthlyExpenses)