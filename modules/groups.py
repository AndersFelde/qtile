from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.lazy import lazy

from .keys import keys, mod

group_names = "123456789"


def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in group_names[:5]:
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner


def go_to_group_and_move_window(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=True)
            return

        if name in group_names[:5]:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen(0)
        else:
            qtile.current_window.togroup(name, switch_group=False)
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen(1)

    return _inner


groups = [Group(i, label="") for i in group_names]

for group in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                group.name,
                # lazy.group[group.name].toscreen(),
                lazy.function(go_to_group(group.name)),
                desc="Switch to group {}".format(group.name),
            ),
            Key(
                [mod],
                "Right",
                lazy.screen.next_group(skip_managed=True),
                desc="Switch to next group",
            ),
            Key(
                [mod],
                "Left",
                lazy.screen.prev_group(skip_managed=True),
                desc="Switch to previous group",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                group.name,
                # lazy.window.togroup(group.name, switch_group=False),
                lazy.function(go_to_group_and_move_window(group.name)),
                desc="Switch to & dont move focused window to group {}".format(
                    group.name
                ),
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
