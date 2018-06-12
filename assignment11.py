print("Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.")

import _thread
import time

# Define a function for the thread
# def print_time(threadName,delay):
#     count=0
#     while count < 5:
#         time.sleep(2)
#         count+=1
#         print("hello,we are in thread")
#
# try:
#     _thread.start_new_thread(print_time,("Thread-1",2,))
#    # _thread.start_new_thread(print_time,("Thread-2",4,))
# except:
#     print("Error:unable to start thread")
# c=1
# while c<2:
#     pass
#
# print("Q2.Make a thread that prints numbers from 1 - 10, waits for 1 sec between")
#
#
# def print_time(threadName, delay):
#     count = 0
#     while count < 10:
#         time.sleep(1)
#         count += 1
#         print("count=",count)
#
#
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2,))
# # _thread.start_new_thread(print_time,("Thread-2",4,))
# except:
#     print("Error:unable to start thread")
#
# while 1:
#     pass

print("Q3.Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display. Delay goes like 2 sec - 4 sec - 6 sec - 8 sec - 10 sec")
#list1 = ['physics', 'chemistry', 1997, 2000];
# def print_time(threadName, delay):
#     count = 0
#     while count < 4:
#         time.sleep(delay)
#
#         print("count=",list1[count])
#         count += 1
#
#
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2,))
# # _thread.start_new_thread(print_time,("Thread-2",4,))
# except:
#     print("Error:unable to start thread")
#
# while 1:
#     pass
#

print("Q4. Call factorial function using thread.")
# import threading
# class fact(threading.Thread):
#     Number=0
#     def __init__(self, number):
#         threading.Thread.__init__(self)
#         self.Number = number
#
#     def run(self):
#         f=1
#         count=self.Number
#         while(count >0):
#             f=f*self.Number
#             count=count-1
#             self.Number=self.Number-1
#         print("factorial=",f)
#
# threads = []
#
# thread = fact(int(input("enter no""")))
#
# thread.start()

