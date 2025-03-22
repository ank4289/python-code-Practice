#try:
    #file=open("bt2",'r')
    #content=file.read()
    #print(content)
#except FileNotFoundError:
    #print("File not found")
#except IOError:
    #print("error occured while  reading the file")
#else:
    #print("file reading completed successfully")


from newmodule import mod1
print(mod1.sum(2,3))

import math
print(math.pow(2,3))

from newmodule import mod2
mod2.greet()
package =mod2.Person("Ankit")
package.intro()