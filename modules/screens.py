from libqtile import bar, hook, qtile
from libqtile.config import Screen

from . import defaults
from .widgets import barWidgets

screens = [
    Screen(
        top=bar.Bar(
            barWidgets,
            # leftWidgets + middleWidgets,
            size=30,
            margin=10,
            background=defaults.colors["transparent"],
        ),
    ),
    Screen(
        top=bar.Bar(
            barWidgets.copy(),
            # leftWidgets + middleWidgets,
            size=30,
            margin=10,
            background=defaults.colors["transparent"],
        ),
    ),
]


@hook.subscribe.screen_change
def restart_on_randr(_):
    qtile.cmd_reload_config()
