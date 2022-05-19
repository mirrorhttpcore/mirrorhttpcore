import subprocess
from threading import Thread
#subprocess.run(["python3", "-m", "pip", "install", "flask"])
#Thread(target=subprocess.run, args=(["python3", "upload-version-1.0-upload.py"]))
print("upload runned! Port: 8384")
subprocess.run(["python3", "-m", "http.server", "--cgi", "8080"])
