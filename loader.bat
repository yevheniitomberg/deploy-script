@echo off
shift

if %0 == spring (
  set /P jasyptDecision=Configure jasypt key?
  if %jasyptDecision% == 1 (
    set /P key=Enter your jasypt key: 
    python loader.py %0 %1 %2 %3 %8 %9 %key%
  )
  else (
    python loader.py %0 %1 %2 %3 %8 %9
  )
) else if %0 == react (
  python loader.py %0 %1 %2 %3
) else (
  echo wrong project type
)
cd /D H:
cd /home/%1
plink -ssh %6 -pw %7 -m start_deploy.txt
if %5 EQU 1 plink -ssh %6 -pw %7 -m configure_nginx.txt
if %4 EQU 1 plink -ssh %6 -pw %7 -m load_cert.txt