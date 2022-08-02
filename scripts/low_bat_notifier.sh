#!/bin/bash

### VARIABLES

POLL_INTERVAL=90     # seconds at which to check battery level
LOW_BAT=99

pollBattery() {
    bat=$(acpi -b)
    state=$(echo ${bat} | awk '{print $3}')

    if [[ "$state" = "Not" ]]; then
        level=$(echo ${bat} | awk '{print $5}')
        level=${level::-1}
        
    else
        level=$(echo ${bat} | awk '{print $4}')
        if [[ "$state" == *"Unknown"* ]]; then
            level=${level::-1}
        else
            if [[ "$level" == "100%" ]]; then
                level=${level::-1}
            else
                level=${level::-2}
            fi
        fi
    fi
}

# If BAT0 doesn't work for you, check available devices with command below
#
#   $ ls -1 /sys/class/power_supply/
#
# BAT_PATH=/sys/class/power_supply/BAT0
# BAT_STAT=$BAT_PATH/status

# if [[ -f $BAT_PATH/charge_full ]]
# then
#     BAT_FULL=$BAT_PATH/charge_full
#     BAT_NOW=$BAT_PATH/charge_now
# elif [[ -f $BAT_PATH/energy_full ]]
# then
#     BAT_FULL=$BAT_PATH/energy_full
#     BAT_NOW=$BAT_PATH/energy_now
# else
#     exit
# fi


#check if the notification is launched 3 times, then quit the script
# launched=0

# Run only if battery is detected
# if ls -1qA /sys/class/power_supply/ | grep -q .
# then
    while true
    do
     #    bf=$(cat $BAT_FULL)
     #    bn=$(cat $BAT_NOW)
     #    bs=$(cat $BAT_STAT)

     #    bat_percent=$(( 100 * $bn / $bf ))
     #    if [[ $bat_percent -lt $LOW_BAT && "$bs" = "Discharging" ]]
     #    then
     #        notify-send --urgency=critical --expire-time=10000 "$bat_percent% : Low Battery!"
	    # # launched=$((launched+1))
	    # # (( "$launched" == 3 )) && exit
     #    fi
        pollBattery
        echo $level
        echo $state
        echo $LOW_BAT
        if [[ $level -lt $LOW_BAT && "$state" == *"Discharging"* ]]; then
            notify-send --urgency=critical --expire-time=10000 "$level%: Low Battery!"
        fi
        sleep $POLL_INTERVAL
    done
# fi
