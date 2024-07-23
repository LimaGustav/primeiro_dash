import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)

dados_conceitos = {
    'java' : {'variáveis': 3,'condicionais':6,'loops':2,'poo':9,'funções':2},
    'python' : {'variáveis': 5,'condicionais':8,'loops':2,'poo':1,'funções':8},
    'sql' : {'variáveis': 8,'condicionais':6,'loops':2,'poo':0,'funções':6},
    'csharp' : {'variáveis': 8,'condicionais':9,'loops':9,'poo':9,'funções':8}
}

colors = {
    'java' : 'red',
    'python': 'blue',
    'sql' : 'yellow',
    'csharp': 'purple'
}

#______________________________Layout______________________________




app.layout = html.Div([
    html.H1("Gustavo Lima",style={'text-align':'center'}),
    html.Div(
        dcc.Dropdown(
            id='dropdown_linguaguens',
            options = [
                {'label':"Java",'value':'java'},
                {'label':"Python",'value':'python'},
                {'label':"C#",'value':'csharp'},
                {'label':"SQL",'value':'sql'}
            ],
            style={'width':"50vw", 'margin': '0 auto'},
            multi=True
            )
    ),
    dcc.Graph(
        id='scatter_plot'
        
    )
])




#______________________________Callbacks______________________________
@app.callback(
    Output('scatter_plot','figure'),
    [Input('dropdown_linguaguens','value')]
)
def atualizar_grafico(linguagens):

    scatter_trace = []

    for linguagem in linguagens:
        dados_linguagem = dados_conceitos[linguagem]
        for conceito,conhecimento in dados_linguagem.items():
            scatter_trace.append(
                go.Scatter(
                    x=[conceito],
                    y=[conhecimento],
                    mode='markers',
                    name=linguagem.title(),
                    marker=dict(
                        size=15,
                        color=colors[linguagem]
                    )
                )
            )

    scatter_layout = go.Layout(
        title='Minhas Linguagens',
        xaxis={
            'title':"Conhecimentos",'showgrid':False
        },
        yaxis={
            'title':"Nivel de conheciomento",'showgrid':False
        }

    )
    return {'data':scatter_trace, 'layout':scatter_layout}


if __name__ == "__main__":
    app.run_server(debug=True)
