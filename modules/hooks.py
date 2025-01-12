from libqtile import hook, qtile
from libqtile.backend.base import Window
import subprocess
import os


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run(["chmod", "+x", script])
    subprocess.call([script])


@hook.subscribe.client_name_updated
def follow_url(client: Window) -> None:
    if client.urgent is True:
        qtile.current_screen.set_group(client.group)
        client.group.focus(client)
