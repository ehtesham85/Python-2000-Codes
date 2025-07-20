# Digital Clock by importing time module
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)