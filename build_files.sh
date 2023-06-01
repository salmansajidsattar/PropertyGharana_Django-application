echo " BUILD START"
python3.6.5 -m pip install -r requirements.txt
python3.6.5 manage.py collectstatic
echo " BUILD END"