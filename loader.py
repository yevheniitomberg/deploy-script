import sys
import shutil
import os

directory = sys.argv[1]
jarFileName = sys.argv[2]
port = sys.argv[3]
project = sys.argv[4]
typeOfBuild = sys.argv[5]
mappedRemoteDisk = sys.argv[6]

pathToDir = f"{mappedRemoteDisk}:/home/{directory}"

if not os.path.exists(pathToDir):
    os.makedirs(pathToDir)

# Text files to execute remote scripts
if project == "spring":
    with open(f"{pathToDir}/start_deploy.txt", "w") as f:
        f.write(f"cd /home/{directory}\n./deploy.sh")

    with open(f"{pathToDir}/load_cert.txt", "w") as f:
        f.write(f"cd /home/{directory}\npython3 nginx_cert.py {directory} {port}")

    with open(f"{pathToDir}/deploy.sh", "w") as f:
        f.write(f"#!/bin/bash\nnohup java -jar {jarFileName} ^> app.log 2^>^&1 ^&\necho $! ^> save_pid.txt")

    with open(f"{pathToDir}/restart.sh", "w") as f:
        f.write(f"cd /home/{directory}\nkill -9 cat save_pid.txt\nrm save_pid.txt\n./deploy.sh")

    with open(f"{pathToDir}/stop.sh", "w") as f:
        f.write(f"cd /home/{directory}\nkill -9 cat save_pid.txt\nrm save_pid.txt")

    shutil.copy(f"{os.getcwd()}\\nginx_cert.py", pathToDir)

    #Build finding
    elementsOfPath = os.getcwd().split("\\")
    elementsOfPath.pop()

    if typeOfBuild == "maven":
        elementsOfPath.append("target")
    elif typeOfBuild == "gradle":
        elementsOfPath.append("build")
        elementsOfPath.append("libs")

    path = "\\".join(elementsOfPath)
    # Jar copying
    shutil.copy(f"{path}\\{jarFileName}", f"{mappedRemoteDisk}:/home/{directory}")
