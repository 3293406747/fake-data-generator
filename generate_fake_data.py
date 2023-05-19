"""
生成mock数据
"""
import random
import re
import string

from faker import Faker

from sucreditcode import CreditIdentifier


class GenerateFakeData:
	""" 生成假数据 """

	def __init__(self):
		self._faker = Faker(locale='zh-CN')

		self.emails = (
			'126.com',
			'sina.com',
			'qq.com',
			'163.com',
			'gmail.com',
			'outlook.com',
			'hostmail.com',
			'aliyun.com',
		)

		self._attrset = {
			'name': 'name',
			'phone': 'phone_number',
			'ssn': 'ssn',
			'job': 'job',
			'country': 'country',
			'city': 'city',
			'word': 'word',
			'card': 'card',
			'province': 'province',
			'email': lambda: self._string(random.randint(6, 16)) + "@" + random.choice(
				self.emails),
			'address': lambda: re.sub(r"[a-zA-Z]\w\s\d{3}", "", self._faker.address()) + "号",
			'company': lambda: self._faker.province().rstrip('省') + self._faker.company(),
		}

	def __getattr__(self, attr):
		if attr in self._attrset:
			if callable(self._attrset[attr]):
				return self._attrset[attr]
			return getattr(self._faker, self._attrset[attr])
		elif attr == "credit_code":
			return self.generate_credit_code
		elif str(attr).startswith("string"):
			return self.string
		raise AttributeError(f'Attribute {attr} not found')

	@staticmethod
	def credit_code():
		""" 生成统一社会信用代码 """
		creditIdentifier = CreditIdentifier()
		for _ in range(2):
			random_credit_code = creditIdentifier.gen_random_credit_code()
			if creditIdentifier.valid(random_credit_code["code"]):
				return random_credit_code["code"]
		else:
			return "generate credit code failed becase of system error,try to regenerate it!"



	@staticmethod
	def _string(length: int) -> str:
		""" 生成指定长度的字母数字组合的字符串 """
		if not isinstance(length, int):
			raise TypeError('type of arg length must be the int')
		elif length < 2:
			raise ValueError('length of arg length must > 1')

		num_count = random.randint(1, length - 1)
		letter_count = length - num_count
		num_array = random.choices(string.digits, k=num_count)
		letter_array = random.choices(string.ascii_letters, k=letter_count)
		all_array = num_array + letter_array
		random.shuffle(all_array)
		return ''.join(all_array)



if __name__ == '__main__':
	gmd = GenerateFakeData()
	print(gmd.company())
	print(gmd.credit_code())
	print(gmd.address())
	print(gmd.name())
	print(gmd.phone())
