from __future__ import absolute_import, division, print_function

import json

import pandas as pd
import plotly
import plotly.graph_objs as go


class GraphsGen:
    """Manage graphs for the web clients."""
    #
    # # TODO remove this , ( right know this is just a demo with sales cube )
    # @staticmethod
    # def generate_graphes(dataframe):
    #     """
    #     Generate graphs for a pandas DataFrame, if you want to add graphs, you have to do it in this function.
    #
    #     :param dataframe: the DataFrame
    #     :return: dict of ids as keys and json graphs as values
    #     """
    #     x = []
    #     x_pie = []
    #     y = []
    #     for idx, row in dataframe.iterrows():
    #         # x_pie to avoid the long words
    #         x_pie.append(row[-2])
    #         x.append(row[-2])
    #         y.append(row[-1])
    #
    #     x = pd.Series(x)
    #     y = pd.Series(y)
    #     # https: // plot.ly / python / reference
    #     # Create the Plotly Data Structure
    #     # go.Scatter
    #     # go.Bar
    #     graphs = [
    #         dict(
    #             data=[go.Bar(x=x, y=y)],
    #             layout=dict(
    #                 # title='Bar Plot',
    #                 yaxis=dict(title="{0}".format(dataframe.columns[-1])),
    #                 xaxis=dict(
    #                     # title="Product"
    #                 ))),
    #
    #
    #         # dict(
    #         #     data=[go.Scatter(
    #         #         x=x,
    #         #         y=y
    #         #         # x = df["Product"],
    #         #         # y=df["count"]
    #         #     )],
    #         #     layout=dict(
    #         #         title='Bar Plot',
    #         #         yaxis=dict(
    #         #             title="Amount"
    #         #         ),
    #         #         xaxis=dict(
    #         #             # title="Product"
    #         #         )
    #         #     )
    #         # ),
    #         dict(data=[{
    #             'labels': x_pie,
    #             'values': y,
    #             'type': 'pie',
    #             'visible' : True,
    #             'showlegend' : True,
    #             # 'show_link' : False,
    #             # # 'link' : False,
    #             # 'colorscale' : 'blues',
    #             # 'textposition' : 'outside',
    #             # 'textinfo' : 'value+percent',
    #             'pull': .2,
    #             'hole': .2
    #         }])
    #     ]
    #
    #     # Add "ids" to each of the graphs to pass up to the client
    #     # for templating
    #     ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
    #     graph_json = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    #
    #     return {'ids': ids, 'graph_json': graph_json}

    @staticmethod
    def generate_pie_graphes(dataframes):
        """
        Generate graphs for a pandas DataFrame, if you want to add graphs, you have to do it in this function.

        :param dataframe: the DataFrame
        :return: dict of ids as keys and json graphs as values
        """
        graphs = []
        for dataframe in dataframes:
            x = []
            y = []
            for idx, row in dataframe.iterrows():
                # x_pie to avoid the long words
                x.append(row[-2])
                y.append(row[-1])

            y = pd.Series(y)
        # https: // plot.ly / python / reference
        # Create the Plotly Data Structure
        # go.Scatter
        # go.Bar
            graphs.append(dict(data=[{
                    # 'title' : dataframe.name,
                    'labels': x,
                    'values': y,
                    'type': 'pie',
                    'visible': True,
                    'showlegend': True,
                    # 'show_link' : False,
                    # # 'link' : False,
                    # 'colorscale' : 'blues',
                    # 'textposition' : 'outside',
                    # 'textinfo' : 'value+percent',
                    'pull': .2,
                    'hole': .2
                }]))



        # Add "ids" to each of the graphs to pass up to the client
        # for templating
        ids = ['pie_graph-{}'.format(i) for i, _ in enumerate(graphs)]
        # ids = [dataframe.name for dataframe in dataframes]
        graph_json = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

        return {'ids': ids, 'graph_json': graph_json}

    # TODO remove this , ( right know this is just a demo with sales cube )
    @staticmethod
    def generate_bar_graphes(dataframes):
        """
        Generate graphs for a pandas DataFrame, if you want to add graphs, you have to do it in this function.

        :param dataframe: the DataFrame
        :return: dict of ids as keys and json graphs as values
        """
        graphs = []
        for dataframe in dataframes:
            traces = []
            for measure in dataframe[dataframe.columns[1:]]:

                x = list(dataframe[dataframe.columns[0]])
                y = list(dataframe[measure])
                # https: // plot.ly / python / reference
                # Create the Plotly Data Structure
                # go.Scatter
                # go.Bar
                traces.append(go.Bar(
                    x=x,
                    y=y,
                    name=measure))


            graphs.append(
                dict(
                    data=traces,
                    show_link=False,
                    layout=go.Layout(
                    barmode='group'
                    )
                )

            )


        # Add "ids" to each of the graphs to pass up to the client
        # for templating
        ids = ['bar_graph-{}'.format(i) for i, _ in enumerate(graphs)]
        graph_json = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

        # TODO use this
        # div = offplot.plot(fig, show_link=False, output_type="div", include_plotlyjs=False)

        return {'ids': ids, 'graph_json': graph_json}

    # TODO remove this , ( right know this is just a demo with sales cube )
    @staticmethod
    def generate_line_graphes(dataframes):
        """
        Generate graphs for a pandas DataFrame, if you want to add graphs, you have to do it in this function.

        :param dataframe: the DataFrame
        :return: dict of ids as keys and json graphs as values
        """
        graphs = []
        for dataframe in dataframes:
            traces = []
            for measure in dataframe[dataframe.columns[1:]]:
                x = list(dataframe[dataframe.columns[0]])
                y = list(dataframe[measure])
                # https: // plot.ly / python / reference
                # Create the Plotly Data Structure
                # go.Scatter
                # go.Bar
                traces.append(go.Scatter(
                    x=x,
                    y=y,
                    name=measure,
                    mode='lines+markers'))


            graphs.append(
                dict(
                    data=traces,
                    # show_link=False
                    # layout=go.Layout(
                    #     barmode='group'
                    # )
                )

            )
        # N = 100
        # import numpy as np
        # random_x = np.linspace(0, 1, N)
        # random_y0 = np.random.randn(N) + 5
        # random_y1 = np.random.randn(N)
        # random_y2 = np.random.randn(N) - 5
        #
        # # Create traces
        # trace0 = go.Scatter(
        #     x=random_x,
        #     y=random_y0,
        #     mode='lines',
        #     name='lines'
        # )
        # trace1 = go.Scatter(
        #     x=random_x,
        #     y=random_y1,
        #     mode='lines+markers',
        #     name='lines+markers'
        # )
        # trace2 = go.Scatter(
        #     x=random_x,
        #     y=random_y2,
        #     mode='markers',
        #     name='markers'
        # )

        # graphs = [
        #     dict(
        #         data=traces,
        #         )
        # ]


        # Add "ids" to each of the graphs to pass up to the client
        # for templating
        ids = ['line_graphe-{}'.format(i) for i, _ in enumerate(graphs)]
        graph_json = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

        # TODO use this
        # div = offplot.plot(fig, show_link=False, output_type="div", include_plotlyjs=False)

        return {'ids': ids, 'graph_json': graph_json}