import plugin
from .screens.calculator_screen import CalculatorScreen

class CalculatorPlugin(plugin.PluginObject):

	def get_main_screen():
		return CalculatorScreen()

	def get_screens():
		return [CalculatorScreen()]