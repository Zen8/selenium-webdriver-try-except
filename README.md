# selenium-webdriver-try-except
Try Except clause for Selenium Webdriver in Python.

Most Common Exception Errors
1. IOError – It occurs on errors like a file fails to open.
2. ImportError – If a python module can’t be loaded or located.
3. ValueError – It occurs if a function gets an argument of right type but an inappropriate value.
4. KeyboardInterrupt – It gets hit when the user enters the interrupt key (i.e. Control-C or Del key)
5. EOFError – It gets raised if the input functions (input()/raw_input()) hit an end-of-file condition (EOF) but without reading any data.

except IOError:<br>
print('Error occurred while opening the file.')

except ValueError:<br>
print('Non-numeric input detected.')

except ImportError:<br>
print('Unable to locate the module.')

except EOFError:<br>
print('Identified EOF error.')

except KeyboardInterrupt:<br>
print('Wrong keyboard input.')

except:<br>
print('An error occurred.')

   
