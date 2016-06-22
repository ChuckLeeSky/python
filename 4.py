from collections import Counter
import re

def create_list(filename):
	datalist = []
	with open(filename,'r') as f:
		for line in f:
			content = re.sub(, repl, string)