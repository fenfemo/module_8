from symtable import Class


class Car:
    def __init__(self, model, vin_number, number):
        self.model = model
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number
        if self.__is_valid_number(number):
            self.__numbers = number

    def __is_valid_vin(self, number):
        if not isinstance(number,int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if number > 9999999 or number < 1000000:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_number(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumber('Некорректный тип данных для номеров')
        if len(number) != 6:
            raise IncorrectCarNumber('Неверная длина номера')

class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self,message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')