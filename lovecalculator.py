#!/usr/bin/env python

"""lovecalculator.py: Calculates the chance on a successful relationship between two people by their names"""

__author__ = "RenanMsV, RafaVIII"
__copyright__ = "Copyright 2023, xMoonGames"
__credits__ = ["RenanMsV", "RafaVIII"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""

import math

class LoveCalculator(object):
  '''
    Calculates the chance on a successful relationship between two people by their names

    love_calculator = LoveCalculator("Name 1", "Name 2")
    print(love_calculator.calculate())
  '''
  def __init__(self, name1 = "", name2 = ""):
    self.name1 = name1
    self.name2 = name2
    self.numbers = ""
  def __calculate_internal__(self, name1, name2):
    self.numbers = ""
    def calc_char_repetitions (n):
      checked_chars = ""
      _numbers = ""
      for character in n:
        if character in checked_chars:
          continue
        checked_chars += character
        _numbers += str(n.count(character))
      return _numbers

    self.numbers += calc_char_repetitions(name1)
    self.numbers += calc_char_repetitions(name2)

    #print("Starting numbers", numbers)

    while True:
      new_numbers = ""
      quantity_of_numbers = len(self.numbers)
      should_drop = (quantity_of_numbers % 2) != 0 # é impar?
      for x in range(0, math.floor(quantity_of_numbers/2)):
        current = int(self.numbers[x])
        last = int(self.numbers[len(self.numbers)-x-1])
        sum = int(current + last)
        #print("The sum of", atual, "and", ultimo, "is", soma)
        new_numbers += str(sum)
      if should_drop == True:
        number_to_drop = self.numbers[math.floor(quantity_of_numbers/2)]
        #print("Dropping the number",  number_to_drop, "\n")
        new_numbers += number_to_drop

      #print("New numbers", new_numbers)
      self.numbers = new_numbers
      if len(self.numbers) <= 2:
        break

    return self.numbers
  def change_first_name(self, name):
    '''Set the first name'''
    self.name1 = name
  def change_second_name(self, name):
    '''Set the second name'''
    self.name2 = name
  def calculate (self, reversed = False):
    '''Shows the percentage on screen'''
    if reversed == True:
      return self.__calculate_internal__(self.name2, self.name1)
    return self.__calculate_internal__(self.name1, self.name2)

if __name__ == '__main__':
  pass
