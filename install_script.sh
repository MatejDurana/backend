git clone https://github.com/MatejDurana/backend.git
cd backend
python3.10 -m venv env
. env/bin/activate
python3.10 -m pip install -r requirements.txt
deactivate 


cd models

cd crowsonkb/
python3.10 -m venv crowsonkb_env
. crowsonkb_env/bin/activate
python3.10 -m pip install -r requirements.txt
pip install -e ./
deactivate 
cd ..


cd zhanghang
python3.10 -m venv zhanghang_env
. zhanghang_env/bin/activate
python3.10 -m pip install -r requirements.txt
deactivate 
cd experiments/models
bash download_model.sh
cd ..
cd ..
cd ..


cd gordicaleksa
python3.6 -m venv gordicaleksa_env
. gordicaleksa_env/bin/activate
python3.6 -m pip install -r requirements.txt
deactivate
cd ..


cd nkolkin/
python3.10 -m venv nkolkin_env
. nkolkin_env/bin/activate
python3.10 -m pip install -r requirements.txt
deactivate 
cd ..
cd ..



