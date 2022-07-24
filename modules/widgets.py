from qtile_extras import widget
from libqtile import qtile
from qtile_extras.widget.decorations import RectDecoration
from . import defaults
import os


class Volume(widget.Volume):
    def setIcon(self):
        if self.volume <= 0:
            self.text = "婢 "
        elif self.volume <= 35:
            self.text = " "
        elif self.volume < 70:
            self.text = " "
        else:
            self.text = "墳 "

    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        self.setIcon()
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        self.setIcon()
        self.draw()

        if wob:
            with open(self.wob, "a") as f:
                f.write(str(self.volume) + "\n")


def parseWidgets(leftWidgets, middleWidgets, rightWidgets):
    allWidgets = [leftWidgets, middleWidgets, rightWidgets]

    for widgets in allWidgets:
        i = 1
        for _ in range(len(widgets) - 1):
            if not hasattr(widgets[i], "insertSeparator"):
                widgets.insert(
                    i,
                    widget.Sep(
                        padding=defaults.separator,
                        linewidth=0,
                        background=defaults.colors["transparent"],
                    ),
                )
                i += 2
                continue
            i += 1
    return (
        leftWidgets
        + [widget.Spacer()]
        + middleWidgets
        + [widget.Spacer()]
        + rightWidgets
    )


def decoration(color=defaults.colors["dark"], left=False, right=False):
    radius = 8
    if left:
        radius = [8, 0, 0, 8]
    elif right:
        radius = [0, 8, 8, 0]

    return {
        "decorations": [RectDecoration(colour=color, radius=radius, filled=True)],
    }


# decor = {
#     "decorations": [
#         RectDecoration(colour=defaults.colors["dark"], radius=8, filled=True)
#     ],
# }

# leftDecor = {
#     "decorations": [
#         RectDecoration(
#             colour=defaults.colors["dark"], radius=[8, 0, 0, 8], filled=True
#         )
#     ],
# }

# rightDecor = {
#     "decorations": [
#         RectDecoration(
#             colour=defaults.colors["dark"], radius=[0, 8, 8, 0], filled=True
#         )
#     ],
# }

leftWidgets = [
    # widget.Image(
    #     **decoration(),
    #     filename="~/.config/qtile/eos-c.png",
    #     mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show combi")},
    # ),
    widget.Clock(
        **decoration(defaults.colors["blue"]),
        format="  %d %m %Y",
    ),
    widget.Clock(
        **decoration(defaults.colors["green"]),
        format="%H:%M",
    ),
    widget.CurrentLayout(
        **decoration(defaults.colors["orange"]),
    ),
]

middleWidgets = [
    widget.GroupBox(
        **decoration(),
        highlight_method="text",
        this_screen_border=defaults.colors["blue"],
        this_current_screen_border=defaults.colors["blue"],
        active=defaults.colors["white"],
        inactive=defaults.colors["grey"],
        padding=defaults.padding,
        margin_x=0,
    ),
]

rightWidgets = [
    widget.DF(
        **decoration(defaults.colors["purple"]),
        format="力 {r:0>2.0f}%",
        visible_on_warn=False,
    ),
    widget.CPU(
        **decoration(defaults.colors["yellow"]), format=" {load_percent:0>2.0f}%"
    ),
    widget.Memory(
        **decoration(defaults.colors["green"]),
        format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
        measure_mem="G",
    ),
    widget.CheckUpdates(
        **decoration(defaults.colors["orange"]),
        update_interval=1800,
        distro="Arch_paru",
        display_format=" {updates}",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(defaults.terminal + " -e paru")
        },
        no_update_string=" 0",
        colour_have_updates=defaults.colors["dark"],
        colour_no_updates=defaults.colors["dark"],
    ),
    widget.Wlan(
        **decoration(defaults.colors["blue"], left=True),
        format=" ",
        disconnected_message="睊 ",
        fontsize=defaults.fontSize + 5,
    ),
    widget.UPowerWidget(
        background=defaults.colors["blue"],
        border_charge_colour=defaults.colors["dark"],
        fill_normal=defaults.colors["dark"],
        border_colour=defaults.colors["dark"],
        border_critical_colour=defaults.colors["red"],
        fill_critical=defaults.colors["red"],
        fill_low=defaults.colors["orange"],
        percentage_low=0.4,
        percentage_critical=0.1,
        insertSeparator=False,
        battery_height=15,
        battery_width=30,
    ),
    widget.Battery(
        background=defaults.colors["blue"],
        format="{char}",
        discharge_char="",
        charge_char="",
        full_char="",
        low_background=defaults.colors["blue"],
        low_foreground=defaults.colors["dark"],
        insertSeparator=False,
        show_short_text=False,
        update_interval=10,
        padding=1,
    ),
    Volume(
        **decoration(defaults.colors["blue"], right=True),
        fontsize=defaults.fontSize + 5,
        # font="Font Awesome 5 Free",
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")},
        insertSeparator=False,
    ),
    widget.TextBox(
        **decoration(defaults.colors["red"]),
        text="",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                os.path.expanduser("~/.config/rofi/powermenu.sh")
            )
        },
        font="Font Awesome 5 Free",
        fontsize=defaults.fontSize,
    ),
]

barWidgets = parseWidgets(leftWidgets, middleWidgets, rightWidgets)

# logger.warning(barWidgets)
