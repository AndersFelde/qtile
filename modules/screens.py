from libqtile import bar
from .widgets import barWidgets
from libqtile.config import Screen
from . import defaults


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
]
