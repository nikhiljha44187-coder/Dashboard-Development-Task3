# Dashboard Development using Plotly Dash

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load dataset
df = pd.read_csv("dashboard_data.csv")

# Create chart
fig = px.bar(
    df,
    x="Product",
    y="Sales",
    color="Region",
    title="Sales Dashboard"
)

# Initialize app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Interactive Sales Dashboard"),
    dcc.Graph(figure=fig)
])

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
