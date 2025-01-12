#!/bin/bash
wallpaper="/usr/share/backgrounds/archlinux/gritty.png"
feh --bg-scale $wallpaper

if [ -n "$(ls -A ~/.cache/betterlockscreen/current/ 2>/dev/null)" ]
then
    #contains file
    echo "Already created wallpaper"
else
    #does not contain file
    betterlockscreen -u $wallpaper
fi
