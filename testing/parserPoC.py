from ConfigParser import SafeConfigParser


def ParseThis(file, section):
	parser = SafeConfigParser()
	parser.read(file)

	for option in parser.options(section):
		print "\t" + option
		try:
			if parser.get(section, option) != 'None':
				print option + ": " + parser.get(section, option)
			else:
				print option + ": Option doesn't exist"
		except:
			print option + ": Something went wrong"

print "First File:"
print "Section 1"
ParseThis('test2.ini', 'Section 1')


print "\n"
print "Second File: "
print "Section 1"
ParseThis('test1.ini', 'Section 1')

print "\n"
print "First File: "
print "Section 1"
ParseThis('test2.ini', 'Section 1')
