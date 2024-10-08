#blank screen
xset s on
xset s 900 #15 min

locker="betterlockscreen -l blur"
killer="systemctl suspend"
notifier='notify-send "Locking in 10 sec" "betterlockscreen -l blur" -a locker -u normal'

xss-lock -- betterlockscreen -l blur &
xautolock -time 10 -locker "$locker" -nowlocker \
"$locker" -killtime 10 -killer "$killer" -notify 10 \
-notifier "$notifier" -detectsleep -noclose

