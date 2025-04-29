import os, signal

pid = int(input("PID del receptor: "))
os.kill(pid, signal.SIGUSR1)
