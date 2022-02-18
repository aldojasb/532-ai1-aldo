from dash import Dash, html, dcc, Input, Output
import altair as alt
import pandas as pd

# Read in global data
#cars = data.cars()
penguins = pd.read_csv('penguins.csv')


# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        #id='xcol-widget',
        id='island_dropdown',
        value='island',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in penguins.columns])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('island_dropdown', 'value'))
def plot_altair(island):
    #chart = alt.Chart(cars).mark_point().encode(
    #    x=xcol,
    #    y='Displacement',
    #    tooltip='Horsepower').interactive()
    bar_chart = alt.Chart(penguins, title='Adelie is the most common penguin species').mark_bar().encode(
        x=alt.X('count()'),
        y=alt.Y('species', sort='-x',title=''),
        color=island)
    
    return bar_chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)