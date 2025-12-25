from pympler.asizeof import asizeof; import threading; from time import sleep
class monitors:
	monitoring = True
	def monitor(objects: list[object]):
		while monitors.monitoring:
			for obj in objects:
				print(f"{type(obj)}: {obj} - {asizeof(obj)}B")
			sleep(5)
def start_monitor(objects: list[object]): monitors.monitoring = True; threading.Thread(target=monitors.monitor, args=(objects,)).start()
def stop_monitor(): monitors.monitoring = False
