#!/usr/bin/env bash

python --version
sudo easy_install pip

pip install \
   pandas\
   sklearn\
   pyarrow\
   --user

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
pip3 install jupyter

#jupyter notebook
