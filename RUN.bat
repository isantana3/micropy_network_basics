@REM ampy --port COM5 ls
cd micropy_network_basics
ampy --port COM5 put model
ampy --port COM5 put service
ampy --port COM5 put view
ampy --port COM5 put .env
ampy --port COM5 put main.py /main.py
ampy --port COM5 run main.py