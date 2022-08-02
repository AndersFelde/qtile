#!/bin/sh
wallpaper="/usr/share/endeavouros/backgrounds/eos_wallpapers_community/Endy_planet.png"
feh --bg-scale $wallpaper
betterlockscreen -u $wallpaper & disown
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/low_bat_notifier.sh & disown

# remap caps to escape
setxkbmap -option "caps:escape"

# gestures
fusuma & disown

# notifications
dunst & disown

# Start welcome
eos-welcome & disown

# start polkit agent from GNOME
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown 

xset s on
xset s 600
