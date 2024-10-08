import os

from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from . import defaults
from .utils import has_internet


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


leftWidgets = [
    widget.Clock(
        **decoration(defaults.colors["blue"]),
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                defaults.terminal + " --hold -e gcalcli agenda"
            )
        },
        format="  %d/%m-%Y",
    ),
    widget.Clock(
        **decoration(defaults.colors["green"]),
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                defaults.terminal + " --hold -e gcalcli agenda"
            )
        },
        format=" %H:%M",
    ),
    widget.CurrentLayoutIcon(
        **decoration(defaults.colors["orange"]), use_mask=True, scale=0.75
    ),
    widget.CheckUpdates(
        **decoration(defaults.colors["purple"]),
        update_interval=90,
        custom_command="(checkupdates ; paru -Qua) | cat",
        display_format=" {updates}",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                defaults.terminal + " -e paru -Syu --noconfirm"
            )
        },
        no_update_string=" 0",
        colour_have_updates=defaults.colors["dark"],
        colour_no_updates=defaults.colors["dark"],
        restart_indicator="ﰇ",
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
        urgent_alert_method="text",
        urgent_text=defaults.colors["red"],
    ),
]

rightWidgets = [
    widget.DF(
        **decoration(defaults.colors["purple"]),
        # format="力 {r:0>2.0f}%",
        format=" {f}{m}B",
        visible_on_warn=False,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("baobab")},
    ),
    widget.CPU(
        **decoration(defaults.colors["yellow"]),
        format=" {load_percent:0>2.0f}%",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(defaults.terminal + " -e htop")
        },
    ),
    widget.Memory(
        **decoration(defaults.colors["green"]),
        format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
        measure_mem="G",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(defaults.terminal + " -e htop")
        },
    ),
    widget.ThermalSensor(
        **decoration(defaults.colors["orange"]),
        format=" {temp:.0f}°C",
        foreground=defaults.colors["dark"],
        foreground_alert=defaults.colors["dark"],
        # format="{tag}: {temp:.0f}{unit}",
        tag_sensor="Package id 0",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(defaults.terminal + " -e htop")
        },
    ),
    widget.GenPollText(
        **decoration(defaults.colors["blue"], left=True),
        func=has_internet,
        update_interval=30,
        fontsize=defaults.fontSize + 5,
    ),
    # widget.Wlan(
    #     **decoration(defaults.colors["blue"], left=True),
    #     format="󰖩 ",
    #     disconnected_message="睊 ",
    #     fontsize=defaults.fontSize + 5,
    #     mouse_callbacks={
    #         "Button1": lambda: qtile.cmd_spawn(
    #             "eww open-many --toggle background-closer system-menu"
    #         )
    #     },
    # ),
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
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                "eww open-many --toggle background-closer system-menu"
            )
        },
    ),
    widget.Battery(
        background=defaults.colors["blue"],
        format="{char}",
        discharge_char="",
        charge_char="",
        full_char="",
        unknown_char="",
        low_background=defaults.colors["blue"],
        low_foreground=defaults.colors["dark"],
        insertSeparator=False,
        show_short_text=False,
        update_interval=10,
        padding=1,
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                "eww open-many --toggle background-closer system-menu"
            )
        },
    ),
    widget.PulseVolume(
        **decoration(defaults.colors["blue"], right=True),
        fontsize=defaults.fontSize + 5,
        mute_format=" ",
        emoji=True,
        emoji_list=[" ", " ", " ", " "],
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                "eww open-many --toggle background-closer system-menu"
            )
        },
        insertSeparator=False,
    ),
    widget.TextBox(
        **decoration(defaults.colors["red"]),
        text="",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(
                os.path.expanduser("~/.config/rofi/powermenu/powermenu.sh")
            )
        },
        font="Font Awesome 5 Free",
        fontsize=defaults.fontSize,
    ),
]

barWidgets = parseWidgets(leftWidgets, middleWidgets, rightWidgets)

# logger.warning(barWidgets)
