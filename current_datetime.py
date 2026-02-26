import time

def get_current_time():
    cut_time = time.localtime()
    return time.strftime('%Y-%m-%d %H:%M:%S', cut_time)
print("Current time: ",get_current_time())







