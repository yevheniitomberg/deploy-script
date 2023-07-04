import os

os.system(f"sed -i -e 's/\\r$//' deploy.sh")
os.system(f"sed -i -e 's/\\r$//' restart.sh")
os.system(f"sed -i -e 's/\\r$//' stop.sh")