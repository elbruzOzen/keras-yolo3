import os

"""
    Appends text, removes file
    Keeps and internal counter, can append the counter value into text
    
    Author: Elbruz Ozen - University of California, San Diego, 11/2019
"""

"""
    Static methods
"""


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def append_to_file(file_name, text):
    with open(file_name, "a+") as my_file:
        my_file.write(text+'\n')


def read_log(file_name):

    detected_object_list = []

    with open(file_name, "r") as my_file:
        while True:
            detected_objects_current = []
            frame_id = my_file.readline()
            if frame_id == '':
                break
            obj_count = int(my_file.readline().strip())

            for i in range(obj_count):
                line = my_file.readline()
                # Second is the confidence
                fragments = line.split()
                # If the line is not entirely written, do not try to unpack
                if len(fragments) != 6:
                    break
                pred, _, left, top, right, bottom = fragments
                detected_objects_current.append([pred, [int(left), int(top), int(right), int(bottom)]])
            detected_object_list.append(detected_objects_current)
    return detected_object_list

"""
    Object
"""

class LogManager:

    def __init__(self):
        self.frame_id = 0

    def increment_frame_count(self):
        self.frame_id = self.frame_id + 1

    def append_frame_id(self, file_name):
        with open(file_name, "a+") as my_file:
            my_file.write(str(self.frame_id)+'\n')
