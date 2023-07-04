@echo off
python loader.py %1 %2 %3 %4 %5 %6
cd /D H:
cd /home/%1
plink -ssh %8 -pw %9 -m start_deploy.txt
if %7 EQU 1 plink -ssh %8 -pw %9 -m load_cert.txt