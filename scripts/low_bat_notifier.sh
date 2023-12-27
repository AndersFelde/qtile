#!/usr/bin/env bash

### VARIABLES

POLL_INTERVAL=90     # seconds at which to check battery level
LOW_BAT=20
LOW_BAT_MODE=0

pollBattery() {
    bat=$(acpi -b | tail -n 1)
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
    while true
    do
        pollBattery
        echo $level
        echo $state
        echo $LOW_BAT
        if [[ $level -lt $LOW_BAT && "$state" == *"Discharging"* ]]; then
            notify-send --urgency=critical --expire-time=10000 "$level%: Low Battery!"
            if [[ $LOW_BAT_MODE -eq 0 ]]; then
                brightnessctl s 30%
                LOW_BAT_MODE=1
            fi
        else
            if [[ $LOW_BAT_MODE -eq 1 ]]; then
                brightnessctl s 90%
                LOW_BAT_MODE=0
            fi
        fi
        sleep $POLL_INTERVAL
    done
# fi
