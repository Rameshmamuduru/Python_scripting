import logging

#logging.basicConfig(level=logging.DEBUG , filename="output.log" , filemode="w")


#create a logger
logger = logging.getLogger("my_test_logger")

#set the logger level
logger.setLevel(logging.DEBUG)

#create a logging file
fh = logging.FileHandler("output.log")

#format for the message for formatter
f = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 

#set that file need to follow that format
fh.setFormatter(f)

# add file handlet to logger
logger.addHandler(fh)

#===================================================================================
#create a logger
logger = logging.getLogger("my_PROD_logger")

#set the logger level
logger.setLevel(logging.WARNING)

#create a logging file
ph = logging.FileHandler("out.log")

#format for the message for formatter
p = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 

#set that file need to follow that format
ph.setFormatter(p)

# add file handlet to logger
logger.addHandler(ph)

###############################################################################








#logging.disable

def validate_name(name):
    if len(name) < 2:
        logger.info("checking for the length")
        return "invalid name"
    elif name.isspace():
        logger.warning("checking if the name is a space")
        return "Invalid Name"
    elif name.isalpha():
        logger.debug("checking if name is alphabet")
        return "Name is valid"
    elif name.replace(' ','').isalpha():
        logger.error("checking for the full name")
        return "name is valid"
    else:
        logger.critical("Failed all checks")
        return "name is valid"

print(validate_name("   "))