#!/bin/bash
wallpaper="/usr/share/endeavouros/backgrounds/eos_wallpapers_community/Endy_planet.png"
feh --bg-scale $wallpaper

if [ -n "$(ls -A /home/kippster/.cache/betterlockscreen/current/ 2>/dev/null)" ]
then
    #contains file
    echo "Already created wallpaper"
else
    #does not contain file
    betterlockscreen -u $wallpaper
fi
