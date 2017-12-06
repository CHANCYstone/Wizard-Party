import sys
from sets import Set

def main(argv):
	print "Hello!"
	if len(argv) != 2:
		print("Usage: python phase2algorithm.py [path_to_input#.py] [path_to_output#.py]")
		return#need to create .out beforehand
	print "Hey!"
	finalOrder = processInput(argv[0], argv[1])
	
	print finalOrder

def processInput(input_file, output_file):
	fin = open(input_file, "r")
	fout = open(output_file, "w")

	num_wiz_in_input = int(fin.readline().split()[0])
	num_constraints = int(fin.readline().split()[0])

	#output_ordering = fout.readline().split()
	#output_ordering_set = set(output_ordering)
	#output_ordering_map = {k: v for v, k in enumerate(output_ordering)}
	wizards = Set()

	for i in range(num_constraints):
		line_num = i + 3
		constraint = fin.readline().split()

		c = constraint
		m = [k for v,k in enumerate(constraint)]

		for j in range(2):
			wizards.add(str(m[j]))

	prestring = ''

	for i,wiz in enumerate(wizards):
		if i < (len(wizards)-1):
			#fout.write(str(wiz) + ",")
			prestring += str(str(wiz) + " ")
		else:
			#fout.write(str(wiz)+'\n')
			#prestring.append((wiz))
			prestring += str(wiz) +'\n'
	fout.write(prestring)
	return prestring
	#wizards

if __name__ == '__main__':
	main(sys.argv[1:])


