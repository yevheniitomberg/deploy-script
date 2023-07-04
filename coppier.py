import os
import shutil
import sys

builder = sys.argv[3]

shutil.copy(f"{os.getcwd()}\\nginx_cert.py", f"H:/home/{sys.argv[2]}")
shutil.copy(f"{os.getcwd()}\\load_cert.txt", f"H:/home/{sys.argv[2]}")
shutil.copy(f"{os.getcwd()}\\start_deploy.txt", f"H:/home/{sys.argv[2]}")
shutil.copy(f"{os.getcwd()}\\fix_sh.py", f"H:/home/{sys.argv[2]}")
elementsOfPath = os.getcwd().split("\\")
elementsOfPath.pop()
if builder == "maven":
    elementsOfPath.append("target")
elif builder == "gradle":
    elementsOfPath.append("build")
    elementsOfPath.append("libs")

path = "\\".join(elementsOfPath)

shutil.copy(f"{path}\\{sys.argv[1]}", f"H:/home/{sys.argv[2]}")

os.remove(f"{os.getcwd()}\\start_deploy.txt")
os.remove(f"{os.getcwd()}\\load_cert.txt")

