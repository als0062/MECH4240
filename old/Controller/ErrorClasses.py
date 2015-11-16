
class ComputerNotConnectedToIP(Exception):
    def __init__(self, deviceName, IP):
        self.name = deviceName
        self.IP = IP
        Exception.__init__(self, "The computer is not currently connected to the IP address for %s at address %s", name, IP)
