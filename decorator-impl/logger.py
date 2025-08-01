import sys
import traceback
import time

def genericExceptionHandler(tb=False, doExit=False, fileHandle=sys.stdout):
    excName, excData, excTb = sys.exc_info()
    print(f"Exception: {excName.__name__} - {excData}", sep=":", file=fileHandle)
    if tb is True:
        traceback.print_exception(excName, excData, excTb, file=fileHandle)
    if doExit is True:
        fileHandle.flush()
        fileHandle.close()
        sys.exit(0)


def logger(functionObject):
    def innerFunction(*args, **kwargs):
        # Obtaining the log file handle
        logFileHandle = None
        try:
            logFileHandle = open("log.txt", "a")
        except Exception:
            genericExceptionHandler(doExit=False)

        assert logFileHandle is not None, "Some deeper issue with log file handle"

        # Preprocessing start
        line = '-' * 40 + '\n'
        print(line, functionObject.__name__, file=logFileHandle)
        print('Time of call', time.ctime(time.time()), file=logFileHandle)

        if len(args) > 0:
            for i in range(len(args)):
                print(f"args[{i}]: {args[i]}", file=logFileHandle)
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                print(f"kwargs[{key}]: {value}", file=logFileHandle)
        # Preprocessing end

        try:
            result = functionObject(*args, **kwargs)
        except:
            genericExceptionHandler(tb=True, doExit=False, fileHandle=logFileHandle)
            result = None

        # Postprocessing start
        print("Result:", result, file=logFileHandle)
        print('Time of return', time.ctime(time.time()), file=logFileHandle)
        logFileHandle.flush()
        logFileHandle.close()
        # Postprocessing end

        return result
    return innerFunction
