import Adafruit_DHT
import sqlite3

sensor = Adafruit_DHT.DHT22

DHTpinIn = 4
#DHTpinOut = ?

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

humIn, tempIn = Adafruit_DHT.read_retry(sensor, DHTpinIn)
#humOut, tempOut = Adafruit_DHT.read_retry(sensor, DHTpinOut)


# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

if humIn is not None and tempIn is not None:
    print '{0:0.1f} {1:0.1f}' .format(tempIn, humIn)
else:
    print 'Failed to get reading. Try again!'

