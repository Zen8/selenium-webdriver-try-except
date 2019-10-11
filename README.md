# selenium-webdriver-try-except
Try Except clause for Selenium Webdriver in Python.

Using try-except is the most common and natural way of handling unexpected errors along with many more exception handling constructs.

1. Arbitrary Exception

try:
    #your code <br>
except Exception as ex:
    print(ex)

2. Catch Multiple Exceptions in One Except Block

try:
    file = open('input-file', 'open mode')
except (IOError, EOFError) as e:
    print("Testing multiple exceptions. {}".format(e.args[-1]))

#Handle each exception in a dedicated block:

try:
    file = open('input-file', 'open mode')
except EOFError as ex:
    print("Caught the EOF error.")
    raise ex
except IOError as e:
    print("Caught the I/O error.")
    raise ex

#If you dont know what type of exception is thrown use the following:

try:
    file = open('input-file', 'open mode')
except:
    # In case of any unhandled error, throw it away
    raise
    
3. Re-raising Exceptions. Exceptions once raised keep moving up to the calling methods until handled. You can add an except clause which could just have a [raise] call without any argument.

try:
    # Intentionally raise an exception.
    raise Exception('I learn Python!')
except:
    print("Entered in except.")
    # Re-raise the exception.
    raise
Output:
Entered in except.
Traceback (most recent call last):
  File "python", line 3, in <module>
Exception: I learn Python!
  
Most Common Exception Errors
1. IOError – It occurs on errors like a file fails to open.
2. ImportError – If a python module can’t be loaded or located.
3. ValueError – It occurs if a function gets an argument of right type but an inappropriate value.
4. KeyboardInterrupt – It gets hit when the user enters the interrupt key (i.e. Control-C or Del key)
5. EOFError – It gets raised if the input functions (input()/raw_input()) hit an end-of-file condition (EOF) but without reading any data.

except IOError:
print('Error occurred while opening the file.')

except ValueError:
print('Non-numeric input detected.')

except ImportError:
print('Unable to locate the module.')

except EOFError:
print('Identified EOF error.')

except KeyboardInterrupt:
print('Wrong keyboard input.')

except:
print('An error occurred.')

   
