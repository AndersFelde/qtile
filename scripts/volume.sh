#!/bin/bash

# You can call this script like this:
# $./volume.sh up
# $./volume.sh down
# $./volume.sh mute
theme="Papirus-Dark"

function get_volume {
    amixer -D pulse get Master | grep '%' | head -n 1 | cut -d '[' -f 2 | cut -d '%' -f 1
}

function is_mute {
    amixer -D pulse get Master | grep '%' | grep -oE '[^ ]+$' | grep off > /dev/null
}

function send_notification {
    DIR=`dirname "$0"`
    volume=`get_volume`
    # Make the bar with the special character ─ (it's not dash -)
    # https://en.wikipedia.org/wiki/Box-drawing_character
#bar=$(seq -s "─" $(($volume/5)) | sed 's/[0-9]//g')
if [ "$volume" = "0" ]; then
    icon_name="/usr/share/icons/$theme/24x24/actions/audio-volume-muted.svg"
    notify-send "$volume""      " -i "$icon_name" -t 2000 -h int:value:"$volume" -h string:synchronous:"─" --replace-id=555 -a volume
    else
	if [  "$volume" -lt "10" ]; then
	     icon_name="/usr/share/icons/$theme/24x24/actions/audio-volume-low.svg"
notify-send "$volume""     " -i "$icon_name" --replace-id=555 -t 2000 -a volume
    else
        if [ "$volume" -lt "30" ]; then
            icon_name="/usr/share/icons/$theme/24x24/actions/audio-volume-low.svg"
        else
            if [ "$volume" -lt "70" ]; then
                icon_name="/usr/share/icons/$theme/24x24/actions/audio-volume-medium.svg"
            else
                icon_name="/usr/share/icons/$theme/24x24/actions/audio-volume-high.svg"
            fi
        fi
    fi
fi
bar=$(seq -s "─" $(($volume/5)) | sed 's/[0-9]//g')
# Send the notification
notify-send "$volume" -i "$icon_name" -t 2000 -h int:value:"$volume" -h string:synchronous:"$bar" --replace-id=555 -a volume

}

case $1 in
    up)
	# Set the volume on (if it was muted)
	amixer -D pulse set Master on > /dev/null
	# Up the volume (+ 5%)
	amixer -D pulse sset Master 5%+ > /dev/null
	send_notification
	;;
    down)
	amixer -D pulse set Master on > /dev/null
	amixer -D pulse sset Master 5%- > /dev/null
	send_notification
	;;
    mute)
    	# Toggle mute
	amixer -D pulse set Master 1+ toggle > /dev/null
	if is_mute ; then
    DIR=`dirname "$0"`
    notify-send -i "/usr/share/icons/$theme/24x24/actions/audio-volume-muted.svg" --replace-id=555 -u normal "Mute" -t 2000 -a volume
	else
	    send_notification
	fi
	;;
esac