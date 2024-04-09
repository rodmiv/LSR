import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc

power_histogram = dcc.Graph(id='power_hist')
toughness_histogram = dcc.Graph(id='toughness_hist')
pvt_heatmap = dcc.Graph(id='power_vs_toughness_hist')
type_counts = dcc.Graph(id='types_bar_plot')

