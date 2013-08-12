import logging

from x10.controllers.cm11 import CM11

logger = logging.getLogger()
hdlr = logging.StreamHandler() # Console
formatter = logging.Formatter('%(module)s - %(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

dev = CM11('/dev/ttyUSB1')
dev.open()

loop=1
while (loop == 1):
        data=dev.read()
        if (data <> ""):
                print_data = int(data)
                print_data = "%x"%(print_data)
                print "data = " + str(print_data)
        if (data == 90):
                dev.write(0xc3)
                first=dev.read()
                first="%x"%(first)
                second=dev.read()
                second="%x"%(second)
                third=dev.read()
                third= "%x"%(third)
                fourth=dev.read()
                fourth = "%x"%(fourth)
                print "first = " + str(first) + " second = " + str(second) + " third = " + str(third) + " fourth = " + str(fourth)

dev.close()
