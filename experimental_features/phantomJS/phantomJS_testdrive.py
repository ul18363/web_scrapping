# -*- coding: utf-8 -*-

"""
Phantom JS ceased development on March 2018 thus it could become outdated, alternatives could be preferred.


Download phantomJS from: https://phantomjs.org/download.html
    sudo tar xzvf wine-1.9.19.tar.bz2
    cd wine-1.9.19
    ./configure
    make
    sudo make install
    sudo reboot
Things it needs:
    relies on Fontconfig (the package fontconfig or libfontconfig, depending on the distribution)
    GLIBCXX_3.4.9 and GLIBC_2.7.

ALTERNATIVELY


sudo apt-get update
sudo apt-get install build-essential chrpath libssl-dev libxft-dev
Install these packages needed by PhantomJS to work correctly.

sudo apt-get install libfreetype6 libfreetype6-dev
sudo apt-get install libfontconfig1 libfontconfig1-dev
Get it from the PhantomJS website.

cd ~
export PHANTOM_JS="phantomjs-1.9.8-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
sudo tar xvjf $PHANTOM_JS.tar.bz2
Once downloaded, move Phantomjs folder to /usr/local/share/ and create a symlink:

sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
Now, It should have PhantomJS properly on your system.

phantomjs --version

OR Shorter

sudo aptitude update
sudo aptitude install build-essential chrpath libssl-dev libxft-dev \
  libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev
PHANTOM_JS="phantomjs-1.9.8-linux-x86_64"
cd ~
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
tar -xvjf $PHANTOM_JS.tar.bz2
sudo mv $PHANTOM_JS /usr/local/share
sudo ln -s /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
phantomjs --version

"""