#!/bin/bash

# You can call this script like this:
# $./brightness.sh up
# $./brightness.sh down
# $./brightness.sh mute
theme="Papirus-Dark"

function get_brightness {
    brightnessctl -m | awk -F "," '{print $4}'
}


function send_notification {
    DIR=`dirname "$0"`
    brightness=`get_brightness`
    # Make the bar with the special character ─ (it's not dash -)
    # https://en.wikipedia.org/wiki/Box-drawing_character
    #bar=$(seq -s "─" $(($brightness/5)) | sed 's/[0-9]//g')
    icon_name="/usr/share/icons/Papirus-Dark/24x24/actions/xfpm-brightness-lcd.svg"
    # bar=$(seq -s "─" $(($brightness/5)) | sed 's/[0-9]//g')
    # Send the notification
    # notify-send "$brightness" -i "$icon_name" -t 2000 -h int:value:"$brightness" -h string:synchronous:"$bar" --replace-id=555 -a brightness
    notify-send "$brightness" -i "$icon_name" -t 2000 -h int:value:"$brightness" --replace-id=555 -a brightness
    
}

case $1 in
    up)
        brightnessctl -q set 5%+
        send_notification
    ;;
    down)
        brightnessctl -q set 5%-
        send_notification
    ;;
esac