# Filename : crawler.py
# authour 

import numpy as np


file_object = open('Question15.dat')
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )


print(all_the_text)