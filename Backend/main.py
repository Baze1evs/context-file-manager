import modules
import argparse
import os

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-qt', '--qtype')
	parser.add_argument('-t', '--type')
	parser.add_argument('-tb', '--typeb')
	parser.add_argument('-to', '--typemto')
	parser.add_argument('-tbo', '--typebmto')
	parser.add_argument('-qe', '--qextension')
	parser.add_argument('-e', '--ext')
	parser.add_argument('-eb', '--extb')
	parser.add_argument('-eo', '--extmto')
	parser.add_argument('-ebo', '--extbmto')
	parser.add_argument('-x', '--extract')

	args = vars(parser.parse_args())

	if args['extract']:
		modules.extract(os.getcwd(), os.getcwd())
	if args['qextension']:
		modules.quickSortByExtension(os.getcwd())
	if args['qtype']:
		modules.quickSortByType(os.getcwd())
	if args['type']:
		modules.sortByType(os.getcwd())
	if args['typemto']:
		modules.sortByType(os.getcwd(), False, True)
	if args['typeb']:
		modules.sortByType(os.getcwd(), True)
	if args['typebmto']:
		modules.sortByType(os.getcwd(), True, True)
	if args['ext']:
		modules.sortByExtension(os.getcwd())
	if args['extmto']:
		modules.sortByExtension(os.getcwd(), False, True)
	if args['extb']:
		modules.sortByExtension(os.getcwd(), True)
	if args['extbmto']:
		modules.sortByExtension(os.getcwd(), True, True)
