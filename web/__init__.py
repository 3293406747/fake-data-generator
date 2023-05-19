from generate_fake_data import GenerateFakeData
from utils import Clipboard

gfd = GenerateFakeData()
clipboard = Clipboard()


def faker(target: str):
	result = getattr(gfd, target)()
	clipboard.set(result)
	return result