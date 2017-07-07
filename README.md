# Python HTTP server for controlling Alphabot-RPi combo
## How to use
```
python server.py
```
## Autostart on boot
Edit /etc/rc.local file in your RPi memory card
```
# some code

python /file/location/server.py &

exit 0
```
