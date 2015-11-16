import sys
import logging
from ConfigParser import ConfigParser
from bacpypes.debugging import Logging, ModuleLogger
from bacpypes.consolelogging import ConsoleLogHandler
from bacpypes.core import run

from bacpypes.app import BIPSimpleApplication
from bacpypes.object import LocalDeviceObject

#debugging
_debug = 0
_log = ModuleLogger(globals())

#_main_

try: 
	_log.debug("initialization")

	_log.debug("running")

except Exception, e:
	_log.exception("an error has occured: %s", e)

finally:
	_log.debug("finally")
