tar -xvzf msb.tgz
python parseShot.py
cat shot/* > shot.txt
python createDatabase.py:
