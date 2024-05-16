linux:
conda create --name ShareRide python=3.8
conda activate ShareRide
./build.sh 
python -m gunicorn webproject.asgi:application -k uvicorn.workers.UvicornWorker

windows:
icacls build.sh /grant Everyone:RX
