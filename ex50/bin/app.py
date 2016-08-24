import signal
import time
import traceback
from multiprocessing import Process, Pool

def trace_back(signal, frame):
	print ''.join(traceback.format_stack(frame))

for num in range(1,20):
	print num, signal.getsignal(num)

signal.signal(signal.SIGQUIT, trace_back)
handler = signal.signal(signal.SIGTERM, trace_back)
handler = signal.signal(signal.SIGINT, trace_back)
print handler


	
def sub():
	while True:
		print 'child'
		time.sleep(3)
	print 'exiting child'
	
def parent():
	while True:
		print 'parent'
		time.sleep(5)
	
	print 'exiting parent'


if __name__ == "__main__":
	pool = Pool(2)
	pool.apply_async(sub, ())
	pool.apply_async(parent, ())
#	sub_process = Process(target=sub)
#	sub_process.start()
	pool.close()
#	pool.join()
	time.sleep(100)
