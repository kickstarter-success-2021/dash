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
        
            ## Process

            We cleaned a Kickstarter dataset, preserve more than 8000 rows, 
            
            and place the rows into a gradient boost model for testing. 
            
            The photo below shows the importances-- it is all about the ability to turn
            
            inital backers into a critical mass of sponsors. 
            
            As the number of backers increase, the white bars, denoting successful cases, 
            
            would increase as well. 
            
            

            """
        ),
        html.Img(src='assets/backer.png', className='img-fluid'),
    ],
    
)

layout = dbc.Row([column1])