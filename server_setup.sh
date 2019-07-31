# @Date:   2019
# @Last modified time: 2019
# @Copyright:
# Copyright 2019 Uday Kumar Adusumilli

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

#	http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.



sudo apt update
sudo apt install ubuntu-desktop gnome-panel gnome-settings-daemon gnome-terminal metacity nautilus vnc4server nvidia-384 -y
nvidia-smi --loop=1
sudo apt install python3-pip keras -y
sudo pip3 install opencv-python
sudo apt install python-matplotlib python-numpy python-pil python-scipy build-essential cython python-skimage python3-skimage -y
cp xstartup ../.vnc/
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-ppc64le.sh
