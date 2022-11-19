import modules
import argparse
import os

# This file should not be called by the user. The registry uses this file.
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-qt', '--qtype', help='Probably the most useful sort. Sorts files based on filegroups. For example, .txt and '
		                       '.docx would be moved to the Documents folder.', action='store_true')
	parser.add_argument(
		'-t', '--type', help='Sorts files based on custom filegroups. Checked extensions would be moved '
		                     'to the Type folder.', action='store_true')
	parser.add_argument(
		'-tb', '--typeb', help='Sorts files based on custom filegroups. Checked extensions would be moved '
		                       'to the Type folder.', action='store_true')
	parser.add_argument(
		'-to', '--typemto', help='Sorts files based on custom filegroups. Checked extensions would be moved '
		                         'to the Type folder.', action='store_true')
	parser.add_argument(
		'-tbo', '--typebmto', help='Sorts files based on custom filegroups. Checked extensions would be moved '
		                           'to the Type folder.', action='store_true')
	parser.add_argument(
		'-qe', '--qextension', help='Sorts files purely by extension.', action='store_true')

	parser.add_argument(
		'-e', '--ext', help='Sorts files based on custom filegroups. Checked extensions would be moved '
		                    'to the Extension folder.', action='store_true')
	parser.add_argument(
		'-eb', '--extb', help='Sorts files based on custom filegroups. Checked extensions would be moved '
		                      'to the Extension folder.', action='store_true')
	parser.add_argument(
		'-eo', '--extmto', help='Sorts files based on custom filegroups. Checked extensions would be moved '
		                        'to the Extension folder.', action='store_true')
	parser.add_argument(
		'-ebo', '--extbmto', help='Sorts files based on custom filegroups. Checked extensions would be moved '
		                          'to the Extension folder.', action='store_true')
	parser.add_argument(
		'-x', '--extract', help='Uproots ALL files in sub directories to current directory. Be careful, this will '
		                        'clear out any and all subfolders', action='store_true')

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
