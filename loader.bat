@echo off
if %1 == spring (
  python loader.py %1 %2 %3 %4 %8 %9
) else if %1 == react (
  python loader.py %1 %2 %3 %4
) else (
  echo wrong project type
)
cd /D H:
cd /home/%1
plink -ssh %6 -pw %7 -m start_deploy.txt
if %5 EQU 1 plink -ssh %6 -pw %7 -m load_cert.txt