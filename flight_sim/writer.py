import time
import os

class Writer:
    def __init__(self):
        self.file_dir = './output/' + time.strftime('%Y%m%d_%H%M%S', time.localtime())

    def write_to_file(self, step):
		try:
			os.makedirs(self.file_dir)

		except FileExistsError:
			pass

		finally:
			self.write_flight_path(self.file_dir)

    def write_flight_path(self):
        pass
