import logging
import os
from functools import wraps


def get_logger(log_file_name, log_sub_dir = ""):
    ''' creates log file and returns logger object '''
    log_dir = './'
    log_dir = os.path.join(log_dir, log_sub_dir)

    # create log file directory
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_path = log_file_name if os.path.exists(log_file_name) \
        else os.path.join(log_dir, (str(log_file_name) + '.log'))

    logger = logging.Logger(log_file_name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')

    console = logging.StreamHandler()
    file_handler = logging.FileHandler(filename = log_path)

    console.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)

    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger

'''

def arglist( *args, **kwargs ):
    s = ""
    for a in args:
      s += repr(a) + ","
    for k,v in kwargs.items():
      s += "{k}={v}, ".format( k= k, v=repr(v) )
    return "( {s} )".format( s=s )


def log_decorator(logger, level=logging.INFO,  name = None, message = None):
    def decorate(func):
        logname = name if name else func.__module__
        logmsg = message if message else logname + '.' + func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            call_msg = logmsg + arglist(*args, **kwargs)
            logger.log(level, call_msg)
            print(call_msg)
            retval = func(*args, **kwargs)
            ret_msg = logmsg + " returning {r}".format(r=retval)
            logger.log(level, ret_msg)
            print(ret_msg)
            return retval

        return wrapper
    return decorate
'''