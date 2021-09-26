import subprocess
import os
import time
import signal

proc_args = ['arecord', '-D' , 'plughw:1' , '-c1' , '-r' , '44100' , '-f' , 'S16_LE' , '-t' , 'wav' , '-V' , 'mono' , '-v' , 'raw_audio.wav']
rec_proc = subprocess.Popen(proc_args, shell=False, preexec_fn=os.setsid)
print("startRecordingArecord()> rec_proc pid= " + str(rec_proc.pid))

time.sleep(5)
os.killpg(rec_proc.pid, signal.SIGTERM)
rec_proc.terminate()
rec_proc = None
print("stopRecordingArecord()> Recording stopped")