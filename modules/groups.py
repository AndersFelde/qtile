from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import keys, mod
from libqtile.config import ScratchPad, DropDown

groups = [Group(i, label="") for i in "123456789"]

for group in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key([mod], "Right", lazy.screen.next_group(), desc="Switch to next group"),
            Key(
                [mod], "Left", lazy.screen.prev_group(), desc="Switch to previous group"
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "alacritty",
                "alacritty",
                width=0.8,
                height=0.6,
                on_focus_lost_hide=True,
            )
        ],
    )
)
