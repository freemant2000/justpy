from multiprocessing import Process
from jpcore.mytest_child import entry_point


proc = Process(
    target=entry_point,
    args=("hi",)
)
proc.daemon = True
proc.start()
print("started")
a=input()
print("killing")
proc.terminate()