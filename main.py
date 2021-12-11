
import sched, time

url = "https://stellarflyff.com/server-status"
s = sched.scheduler(time.time, time.sleep)

def get_data(sc):
	print("Retreving information from " + url + "...")
	s.enter(5, 1, get_data, (sc,))

# Start the loop immediately 
s.enter(0, 1, get_data, (s,))
s.run()