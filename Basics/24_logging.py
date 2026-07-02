import logging

logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f"dividing {a} by {b}")
    
    if b == 0:
        logging.error("Can not be divided by zero!")
        return None
    
    result = a/b
    logging.info(f"Division successful: {a}/{b} = {result}")
    return result

def add(a,b):
    logging.debug(f"Adding {a} + {b}")
    result = a+b
    logging.info(f"Addition successful: {result}")
    return result

add(5, 3)
divide(10, 2)
divide(10, 0)   