import sys
import os

with open("start_deploy.txt", "w") as f:
    f.write(f"cd /home/{sys.argv[1]}\npython3 fix_sh.py\n./deploy.sh")
with open("load_cert.txt", "w") as f:
    f.write(f"cd /home/{sys.argv[1]}\npython3 nginx_cert.py {sys.argv[1]} {sys.argv[2]}")