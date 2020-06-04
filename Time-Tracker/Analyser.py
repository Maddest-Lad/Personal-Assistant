import csv
import os
from datetime import datetime


class Analyser:

    def __init__(self):
        self.data_path = os.getcwd() + "\\Data"

    def process_data(self):

        data_file = [os.path.join(self.data_path, file) for file in os.listdir(self.data_path)]

        processed_data = []

        for program in data_file:
            with open(program) as csv_file:

                use_time = 0
                current_day = datetime.now().strftime('%Y-%m-%d')

                data = list(csv.reader(csv_file))

                try:
                    previous_time = extract_min(data[3][1])

                    for i in data:

                        if "Date" not in i and len(i) != 0 and i[0] is current_day and len(data) > 5:
                            current_time = extract_min(i[1])

                            if previous_time + 1 is current_time or previous_time is 60 and current_time is 0:
                                use_time += 1

                            previous_time = current_time

                    processed_data.append((use_time, program.split("\\")[-1]))

                except IndexError:
                    pass

        return processed_data if len(processed_data) > 0 else None


def extract_min(time):
    return int(time.split(":")[1])
