@echo off
mkdir H:\home\%1
python .\opener.py %1 %3
python .\coppier.py %2 %1 %5
cd /D H:
cd /home/%1
copy NUL deploy.sh
echo #!/bin/bash >> deploy.sh
echo nohup java -jar %2 ^> app.log 2^>^&1 ^& >> deploy.sh
echo echo $! ^> save_pid.txt >> deploy.sh
copy NUL restart.sh
echo #!/bin/bash >> restart.sh
echo kill -9 cat save_pid.txt >> restart.sh
echo rm save_pid.txt >> restart.sh
echo ./deploy.sh >> restart.sh
copy NUL stop.sh
echo #!/bin/bash >> stop.sh
echo kill -9 cat save_pid.txt >> stop.sh
echo rm save_pid.txt >> stop.sh
plink -ssh %6 -pw %7 -m start_deploy.txt
if %4 EQU 1 plink -ssh %6 -pw %7 -m load_cert.txt