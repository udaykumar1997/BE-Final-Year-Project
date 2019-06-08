sudo apt update
sudo apt install ubuntu-desktop gnome-panel gnome-settings-daemon gnome-terminal metacity nautilus vnc4server nvidia-384 -y
nvidia-smi --loop=1
sudo apt install python3-pip keras -y
sudo pip3 install opencv-python 
sudo apt install python-matplotlib python-numpy python-pil python-scipy build-essential cython python-skimage python3-skimage -y
cp xstartup ../.vnc/
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-ppc64le.sh
