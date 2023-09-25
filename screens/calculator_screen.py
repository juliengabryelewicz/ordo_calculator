from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

import re

class CalculatorScreen(Screen):

	solution = StringProperty("")

	def __init__(self, **kwargs):
		super(CalculatorScreen, self).__init__(**kwargs)
		self.operators=["/","*","+","-"]
		self.last_is_operator=None
		self.last_button=None
		
	def write_operation(self,button_text):
		if button_text=="C":
			self.solution=""
		elif self.solution and (self.last_is_operator and button_text in self.operators):
			return
		elif self.solution=="" and button_text in self.operators:
			return
		else:
			self.solution=self.solution+button_text
		self.last_button=button_text
		self.last_is_operator=self.last_button in self.operators

	def write_solution(self):
		self.solution=str(eval(re.sub(r'\b0+(?!\b)', '', self.solution)))

	pass