from libqtile.lazy import lazy
from libqtile.config import Key

from .defaults import mod, terminal

# mod = "mod4"
# terminal = "alacritty"


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.layout.next(), desc="Toggle between windows"),
    Key([mod], "z", lazy.next_layout(), desc="Toggle between zoom and not zoom layout"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key(
        [mod, "shift", "control"],
        "l",
        lazy.layout.swap_column_right(),
    ),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("/home/kippster/.config/qtile/scripts/volume.sh up"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("/home/kippster/.config/qtile/scripts/volume.sh down"),
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("/home/kippster/.config/qtile/scripts/volume.sh mute"),
    ),
    Key([mod], "b", lazy.group["scratchpad"].dropdown_toggle("alacritty")),
    Key([mod], "comma", lazy.spawn("xautolock -locknow")),
    Key(
        [mod],
        "space",
        lazy.spawn("/home/kippster/.config/rofi/launchers/misc/launcher.sh"),
        desc="Application launcher",
    ),
    Key(
        ["mod1"],  # alt
        "Tab",
        lazy.spawn("/home/kippster/.config/rofi/launchers/misc/window_switcher.sh"),
        desc="Application launcher",
    ),
    Key(
        [mod],  # alt
        "f",
        lazy.window.toggle_floating(),
        desc="Application launcher",
    ),
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn("flameshot gui --clipboard --accept-on-select"),
    ),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "p", lazy.spawn("flameshot gui")),
]
