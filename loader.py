import sys
import shutil
import os

def copytree(src,dst):
    os.system("cp -r "+src+" "+dst)

project = sys.argv[1]
directory = sys.argv[2]
mappedRemoteDisk = sys.argv[3]
port = sys.argv[4]

pathToDir = f"{mappedRemoteDisk}:/home/{directory}"

if not os.path.exists(pathToDir):
    os.makedirs(pathToDir)

with open(f"{pathToDir}/start_deploy.txt", "w") as f:
    f.write(f"cd /home/{directory}\npython3 fix_sh.py\n./deploy.sh")

with open(f"{pathToDir}/load_cert.txt", "w") as f:
    f.write(f"cd /home/{directory}\npython3 cert.py {directory}")

with open(f"{pathToDir}/configure_nginx.txt", "w") as f:
    f.write(f"cd /home/{directory}\npython3 nginx_settings.py {directory} {port}")

shutil.copy(f"{os.getcwd()}\\nginx_settings.py", pathToDir)
shutil.copy(f"{os.getcwd()}\\cert.py", pathToDir)
shutil.copy(f"{os.getcwd()}\\fix_sh.py", pathToDir)

# Text files to execute remote scripts
if project == "spring":
    typeOfBuild = sys.argv[5]
    jarFileName = sys.argv[6]
    with open(f"{pathToDir}/deploy.sh", "w") as f:
        f.write(f"#!/bin/bash\nnohup java -jar {jarFileName} > app.log 2>&1 &\necho $! > save_pid.txt")

    with open(f"{pathToDir}/restart.sh", "w") as f:
        f.write(f"cd /home/{directory}\nkill $(cat save_pid.txt)\nrm save_pid.txt\n./deploy.sh")

    with open(f"{pathToDir}/stop.sh", "w") as f:
        f.write(f"cd /home/{directory}\nkill $(cat save_pid.txt)\nrm save_pid.txt")

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

elif project == "react":
    with open(f"{pathToDir}/deploy.sh", "w") as f:
        f.write(f"#!/bin/bash\nnohup serve -s build -l {port} > app.log 2>&1 &\necho $! > save_pid.txt")

    with open(f"{pathToDir}/restart.sh", "w") as f:
        f.write(f"cd /home/{directory}\nkill $(cat save_pid.txt)\nrm save_pid.txt\n./deploy.sh")

    with open(f"{pathToDir}/stop.sh", "w") as f:
        f.write(f"cd /home/{directory}\nkill $(cat save_pid.txt)\nrm save_pid.txt")

    elementsOfPath = os.getcwd().split("\\")
    elementsOfPath.pop()
    elementsOfPath.append("build")
    path = "\\".join(elementsOfPath)
    copytree(path, pathToDir)

