import runpy
import threading
import time

def poller():
    while True:
        print("Polling..")
        runpy.run_path("zipf.py")
        print("Polling complete..")
        time.sleep(1800)


t = threading.Thread(target=poller)
t.daemon = True
t.start()

#input_text = " "
#while not input_text == "exit":
#    if input_text == "show":
#        print_result()
#    input_text = input()
