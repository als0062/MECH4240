import ConfigParser
#Config = ConfigParser.ConfigParser()

def ConfigSectionMap(section, Config):
    dict1 = {}
    options = Config.options(section) 
    for option in options:
        try:
            if Config.get(section, option) == 'None':
                a=5
            else:
                dict1[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def CompIPToRequestIP(compIP):
	RequestIP = compIP[-2:]
	#Not working if IP address ends in a value larger that 100...not sure if it is an issue
	if int(RequestIP) < 1 or int(RequestIP) > 99:
	    print "Error : Invalid IP address"
	    return None
	RequestIP = int(RequestIP) - int(1)
	if int(RequestIP) < 10:
	    RequestIP = str(compIP)[:-2] + "0" + str(RequestIP)
	else:
	    RequestIP = str(compIP)[:-2] + str(RequestIP)
	return RequestIP

def iniParser(iniFile):
    Config = ConfigParser.ConfigParser()
    Config.read(iniFile)
    dictionary = ConfigSectionMap("BACpypes", Config)
    return dictionary

def parsePorts(iniFile):
    Config = ConfigParser.ConfigParser()
    Config.read(iniFile)
    dictionary = ConfigSectionMap("Ports", Config)
    return dictionary
