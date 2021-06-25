# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Insights

            The gradient boost classifier model, the one in this app, shows that the most important factors are the number of initial backers,

            the goal in usd and the pledged amount. The picture below shows our model's important features. The model is a simple illustration

            that fund-rasing success is all about turning backers into more sponsors.



            The model is obviously wrong, because classifiers pick more potent, and potentially leaking indicator. In plain English, the classifers

            detect failure, about 40% of total cases, with the backer_counts and pledged amount, rather than categories or sub-categories.



            """

        ),

    # html.Img(src='assets/Rating Distribution.PNG', className='img-fluid'),

    html.Img(src='assets/rf_kickstarter.png', className='img-fluid')

    ],
)




layout = dbc.Row([column1])
