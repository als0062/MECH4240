import subprocess
# import time
subprocess.call("sudo ifconfig eth0 192.168.92.70 netmask 255.255.255.0", shell=True)
subprocess.call("ifconfig", shell=True)
subprocess.call("sudo ifconfig eth0 192.168.92.69 netmask 255.255.255.0", shell=True) 
subprocess.call("ifconfig", shell=True)
# subprocess.call('ls', shell=True)
# subprocess.call("cd Pipe", shell=True)
# time.sleep(2)
# subprocess.call("clear", shell=True)



