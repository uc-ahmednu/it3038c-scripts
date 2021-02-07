#! /bin/bash
# This script outputs the IP addres and hostname of a machine

echo 'This is a script. Hello!'

greeting="this is a script. hello!"
echo $greeting, thanks for joining us!
echo '$greeting,thanks for joining us! you owe me $20'
echo "$greeting,thanks for joining us!"
echo "$greeting,you owe me $20" 
echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME

