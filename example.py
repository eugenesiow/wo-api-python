from wo import WO
import logging
###uncomment for printing debug info
#logging.getLogger('requests').setLevel(logging.WARNING)
#logging.basicConfig(level=logging.DEBUG)
logging.captureWarnings(True)
#import urllib3
#urllib3.disable_warnings()



appid = "55d6b06b4d6b5d1d21449967"
appsec = "eac2b1a25ef936ce" 
username = ""
password = ""



client = WO('ui.webobservatory.me', appid, appsec, username ,password )

##login after the client creation
res = client.login()
if res:
    print "Error message:"+ res


##demo of the query using a string:
err, res1 = client.query('55d587a24d6b5d1d21449966','select * from iot.traffic_data limit 50;')
if not err:
    print "\n\n"
    print "RESULT 1:"
    print res1
else:
    print err