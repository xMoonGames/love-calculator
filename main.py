#!/usr/bin/env python

__author__ = "RenanMsV, RafaVIII"
__copyright__ = "Copyright 2023, xMoonGames"
__credits__ = ["RenanMsV", "RafaVIII"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""

import math
from consolemenu import *
from consolemenu.items import *
from consolemenu.prompt_utils import PromptUtils
from lovecalculator import LoveCalculator

def wait_for_input():
  PromptUtils(Screen()).enter_to_continue()

love_calculator = LoveCalculator()

def show_current_configs():
  return "Current names: First name: \"{}\", Second name: \"{}\"".format(love_calculator.name1 or "N/A", love_calculator.name2 or "N/A")

menu = ConsoleMenu(
  title = "Love Calculator - Calculates the chance on a successful relationship between two people by their names",
  subtitle = show_current_configs,
  exit_option_text = "Exit"
)

def change_first_name():
  name = input("Whats the first person's name? ").strip()
  love_calculator.change_first_name(name)
  print("First name set with success to", name)
  wait_for_input()

def change_second_name():
  name = input("Whats the second person's name? ").strip()
  love_calculator.change_second_name(name)
  print("Second name set with success to", name)
  wait_for_input()

def show_love_percentage():
  percentage_normal = int(love_calculator.calculate())
  percentage_reverse = int(love_calculator.calculate(reversed = True))

  print(f"The percentage of love between \"{love_calculator.name1}\" and \"{love_calculator.name2}\" are as follows:")

  if percentage_normal != percentage_reverse:
    print(f"The percentage is {math.floor((percentage_normal + percentage_reverse)/2)}%\n")
  else:
    print(f"The percentage is {percentage_normal}%")

  wait_for_input()

def configure_setup ():
  print("Add initial configuration:\n")
  change_first_name()
  change_second_name()

item_configure_setup = FunctionItem("Add initial configuration", configure_setup)
item_first_name = FunctionItem("Change first name", change_first_name, [])
item_second_name = FunctionItem("Change second name", change_second_name, [])
item_recalculate = FunctionItem("Show love percentage", show_love_percentage, [])

menu.append_item(item_configure_setup)
menu.append_item(item_first_name)
menu.append_item(item_second_name)
menu.append_item(item_recalculate)

menu.show()
