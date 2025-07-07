import subprocess

subprocess.run(['sudo',"update"])
subprocess.run(['sudo',"upgrade"])
subprocess.run(['sudo','apt','upgrade'])
subprocess.run(['sudo','apt','autoremove'])
print("The system may need to restart")
a = input("Would you like the system to restart")

if a==True:
  subprocess.run(['sudo','shutdown','-r','now','"The system will restart now"'])
