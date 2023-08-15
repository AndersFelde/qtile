import re

from libqtile import layout
from libqtile.config import Match

from . import defaults

layouts = [
    layout.MonadTall(
        margin=8,
        border_focus=defaults.colors["blue"],
        border_normal=defaults.colors["dark"],
    ),
    # layout.Columns(
    #     border_focus=defaults.colors["blue"],
    #     border_normal=defaults.colors["dark"],
    # ),
    layout.MonadThreeCol(
        margin=8,
        border_focus=defaults.colors["blue"],
        border_normal=defaults.colors["dark"],
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    border_focus=defaults.colors["blue"],
    border_normal=defaults.colors["dark"],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="flameshot"),  # Screenshot
        Match(title=re.compile("Figure.*")),  # Matplotlib figures
    ],
)
