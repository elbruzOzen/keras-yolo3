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
