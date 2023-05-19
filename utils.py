import pyperclip as pyperclip


class Clipboard:
	"""剪切板，包括剪切板内容的获取及设置"""

	@staticmethod
	def get():
		"""获取剪贴板内容"""
		return pyperclip.paste()

	@staticmethod
	def set(text):
		"""设置剪贴板内容"""
		pyperclip.copy(text)