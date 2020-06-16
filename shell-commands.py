sudo apt-get install python3-pip
pip3 install virtualenv
mkdir Dev   (can use any name for these folders)
cd Dev
mkdir trydjango
cd trydjango

virtualenv -p python3 .
source bin/activate

pip install django==2.0.7

deactivate (to deactivate virtual env)
source /bin/activate (to activate current folders virtual env)

