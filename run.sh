sudo apt-get update
sudo apt-get install tesseract-ocr -y
sudo apt-get install git -y
sudo apt-get install python-pip -y
sudo apt-get install libmagickwand-dev -y 
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk -y 
sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev -y
sudo pip install git+https://github.com/jflesch/pyocr.git
sudo pip install wand
sudo pip install flask
sudo pip install pytesseract

git clone https://github.com/salmandhariwala/python-pdf-ocr.git

sudo nohup python ~/python-pdf-ocr/flask_server/app.py &






