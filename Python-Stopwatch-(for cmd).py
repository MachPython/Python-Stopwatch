import time
print('this is your own stop watch for people who are above google')
time.sleep(2)
def time_convert(sec):
mins = sec // 60
sec = sec % 60
hours = mins // 60
mins = mins % 60
print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
input("press enter to start stopwatch")
start_time = time.time()
input("press enter to stop stopwatch")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
time.sleep(200)
