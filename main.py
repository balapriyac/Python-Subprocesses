import subprocess
# simple Bash command
process_1 = subprocess.run("ls")
print(process_1)
print(process_1.args)
print(process_1.returncode)
print(process_1.stdout)
# simple Bash command with args
process_2 = subprocess.run(["ls","py_logging"])
print(process_2)
print(process_2.args)
print(process_2.returncode)
print(process_2.stdout)
# setting shell = True
process_3 = subprocess.run("ls py_logging",shell=True)
print(process_3)
print(process_3.args)
print(process_3.stdout)
# Capture and decode subprocess output
process_4 = subprocess.run("ls",capture_output=True)
print(process_4.stdout.decode())
# Capture subprocess output as text
process_5 = subprocess.run("ls",capture_output=True,text=True)
print(process_5.stdout)
# Explicitly capture output in stdout
process_6 = subprocess.run("ls",stdout=subprocess.PIPE,text=True)
print(process_6.stdout)
# Redirect subprocess output to a file
with open('contents.txt','w') as f_obj:
    subprocess.run("ls",stdout=f_obj,text=True)
# subprocess fails with non-zero returncode and error info on stderr
process_7 = subprocess.run(["ls","non-existent-directory"],capture_output=True)
print(process_7.returncode)
print(process_7.stderr)
process_8 = subprocess.run(["ls","non-existent-directory"],stderr=subprocess.PIPE)
print(process_8.stderr)
# check if external command runs successfully
process_9 = subprocess.run(["ls","non-existent-directory"],capture_output=True,check=True)
# Set the timeout parameter; ensure that process_9 succeeds before running the following processes
process10 = subprocess.run(["sleep","10"],capture_output=True,check=True,timeout=2)
# Handling the TimeoutExpired exception
try:
    process10 = subprocess.run(["sleep","10"],capture_output=True,check=True,timeout=2)
except subprocess.TimeoutExpired:
    print("subprocess timed out")
# pipe subprocess outputs
process1 = subprocess.run(["cat","sample.txt"],capture_output=True,text=True)
process2 = subprocess.run(["grep","-n","Python"],capture_output=True,text=True,input=process1.stdout)
print(process_2.stdout)
# modify env variables
import os
new_env = os.environ.copy()
new_env["PATH"] = os.pathsep.join(["/testapp/",new_env["PATH"]])
process_now = subprocess.run(["ls"],env=new_env)
