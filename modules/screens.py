from libqtile import bar
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
