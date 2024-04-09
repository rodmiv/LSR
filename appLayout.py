### Imports ###
import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import html

### Locals ###
from Components.NavBar import navbar
from Components.Plots import power_histogram, toughness_histogram, type_counts, pvt_heatmap
### Layout ###


def myLayout():
    return 