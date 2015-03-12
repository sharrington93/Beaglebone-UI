#! /bin/sh
# Download the latest master from the GitHub repo, then unpack it to the root filesystem.
# WARNING: this will happily overwrite anything in its path.

mkdir -p ~/tmp
cd ~/tmp
rm master.zip
rm -R CANCorder-UI-master
wget https://github.com/BuckeyeCurrent/CANCorder-UI/archive/v1-dev.zip
unzip CANCorder-UI-1-dev.zip
sudo rsync -a CANCorder-UI-1-dev/ /

sudo /etc/init.d/apache2 restart
sudo /etc/init.d/mysql restart
