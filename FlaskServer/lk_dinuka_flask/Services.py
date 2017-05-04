def validateUser(username, password):
    try:
        if username == 'a' and password == 'a':
            return True
    except Exception as e:
        printLog('error', e)


def printLog(level, message):
    if level == 'info':
        print "[INFO]: ", message
    elif level == 'error':
        print "[ERROR]: ", message
    elif level == 'process':
        print "[PROCESS]: ", message
