from libqtile import bar
from .widgets import widget, barWidgets
from libqtile.config import Screen
from . import defaults


print(barWidgets)
screens = [
    Screen(
        top=bar.Bar(
            barWidgets,
            # leftWidgets + middleWidgets,
            size=30,
            margin=10,
            background=defaults.colors["background"],
        ),
    ),
]
