#/bin/sh

# config script for CANCorder

sudo a2enmod rewrite
sudo apt-get install mysql-server-5.6 phpmyadmin
# use password “buckeyes”

# beaglebone-specific config
sudo systemctl disable cloud9.service
sudo systemctl disable bone101.service
sudo systemctl disable gateone.service