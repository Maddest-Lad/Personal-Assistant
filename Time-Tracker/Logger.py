import csv
import os
import time
from datetime import datetime
from threading import Timer

import psutil

import Constants


class Logger:

    # Returns A List Of Programs Using A Memory threshold
    def get_active(self, threshold=None) -> list:
        if threshold is None:
            threshold = 1

        active_list = []
        skip_list = Constants.ignore_list

        for i in psutil.process_iter():

            # If An Important Program Is Assumed To Be Actively Running
            if i.memory_percent() > threshold and i.name() not in skip_list:
                active_list.append(i)

        # print(active_list)
        return active_list

    # Saves The Data Filtered From Dynamic or Threshold Functions To CSV Files
    def save_data(self, active_list):

        data_path = os.getcwd() + "//Data"  # CWD = Current Working Directory

        # Create The Data Folders And Files If They Don't Exist
        if not os.path.exists(data_path):
            try:
                os.mkdir(data_path)
            except (PermissionError, FileExistsError):
                pass

        csv_fields = ["Date", "Time"]  # Name Isn't Mentioned Here As It's In the File Name

        for i in active_list:

            program_path = data_path + "//" + i.name().split('.')[0] + ".csv"

            try:
                # Creates The CSV File If It Doesn't Exist
                if not os.path.exists(program_path):
                    with open(program_path, 'w') as temp_file:
                        writer = csv.writer(temp_file)
                        writer.writerow(csv_fields)
                        temp_file.close()

                # Lock The File Then Write The Data To The CSV File
                with open(program_path, 'a') as csv_file:
                    writer = csv.writer(csv_file, lineterminator='\n')
                    date = datetime.now().strftime('%Y-%m-%d')
                    time = datetime.now().strftime('%H:%M')
                    writer.writerow([date, time])
                    csv_file.close()
            except PermissionError:
                pass

    # The Thing That Get Called By Center Control
    def run(self):
        Timer(interval=60, function=self.run)
        self.save_data(self.get_active(threshold=0.25))


Logger().run()

while True:
    time.sleep(1)
