# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_t1 = pd.read_excel('Task1.xlsx','Top_20')
df = pd.read_excel('temp_change_grouped.xlsx','Well_Processed_Data')
df_t3_1 = pd.read_excel('task3.xlsx','Correlation_Developed_Temp_Foss')
df_t3_2 = pd.read_excel('task3.xlsx','Correlation_Develping_Temp_Foss')
df_t4 = pd.read_excel('Season_Temp_Data_Combined.xlsx','Seasons_Consolidated')

fig = px.line(df,x='Year',y=['Developing','Developed','World'])
fig_task4 = px.line(df_t4,x='Year',y=['Winter_temp_change','Spring','Summer','Fall'],color_discrete_sequence=['brown', 'blue','red','orange'])
#fig_task4.update_traces(line_color='#456987')
fig_task1 = px.histogram(df_t1,y='Country_Name',x='Average')
fig_task3_1 = px.scatter(df_t3_1, x="Developed (Temp_Change)", y="Developed (Fossil_Fuel)",color='Year', trendline="ols")
fig_task3_2 = px.scatter(df_t3_2, x="Developing (Temp_Change)", y="Developing (Fossil_Fuel)", color='Year', trendline="ols")

app.layout =html.Div(children=[
    dcc.Graph(
        id = 'example-graph',
        figure = fig_task1       
    ),
    html.H1(children='Task 2: Analyzing the temperature change patterns of developed and developing countries\
            . ',),
    html.Div([
        html.P('This is a sample content'),
        ],style={  'color': 'blue', 'fontSize': 24, 'marginBottom': 25, 'marginTop': 25}),
    dcc.Graph(
        id='example-graph', 
        figure=fig
    ),
    html.H1(children='Task 3: Analyzing the consumption of fossil fuels in developed countries and its relation to Temperature change\
            . ',),
    dcc.Graph(
        id='example-graph',
        figure=fig_task3_1
    ),
    html.H1(children='Task 3: Analyzing the consumption of fossil fuels in developing countries and its relation to Temperature change\
            . ',),
    dcc.Graph(
        id='example-graph',
        figure=fig_task3_2
    ),
    html.H1(children='Task 4: Analyzing the effect of season on temperature change\
            . ',),
    dcc.Graph(
        id='example-graph',
        figure=fig_task4
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
