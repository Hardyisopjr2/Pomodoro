PACKAGENAME = "pyttsx3"
import sys
import subprocess
print("Checking if requirements are satisfied, If not, installing packages.")
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', PACKAGENAME])