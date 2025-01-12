font = "CaskaydiaCove NF"
import os

fontSize = 18
padding = 10
separator = 25
margin = 3
spacerLength = 5
colors = {
    "white": "#dcdcdc",
    "black": "#000000",
    "dark": "#181a1f",
    "lightDark": "#21252b",
    "grey": "#ABB2BF",
    "lightRed": "#ff616e",
    "red": "#f44747",
    "green": "#8cc265",
    "yellow": "#E5C76B",
    "orange": "#f0a45d",
    "blue": "#61afef",
    "lightBlue": "#56b6c2",
    "darkBlue": "#4d78cc",
    "purple": "#c678dd",
    "transparent": "#00000000",
}
mod = "mod4"
terminal = "alacritty"
widget_defaults = dict(
    font=font,
    fontsize=fontSize,
    padding=padding,
    appendSeparator=True,
    foreground=colors["dark"],
)
home_dir = os.path.expanduser("~")
qtile_dir = os.path.join(home_dir, ".config", "qtile")
rofi_dir = os.path.join(home_dir, ".config", "rofi")
