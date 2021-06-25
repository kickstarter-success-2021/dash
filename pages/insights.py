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
            
            The gradient boost classifier model, the one in this app, shows that the most important factors are the number
            
            of initial backers, the goal in usd and the pledged amount. The picture below is from the model's close 
            
            cousin, XGBoost Classifier, that shows similar result. It is all about turning backers into more 
            
            sponsors. 

            """
        
        ), 
    
    # html.Img(src='assets/Rating Distribution.PNG', className='img-fluid'),

<<<<<<< HEAD
    html.Img(src='assets/xgb_kikstarter.png', className='img-fluid')
=======
    #html.Img(src='assets/XGBoost All Features.png', className='img-fluid')
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
    
    ],
)



       
layout = dbc.Row([column1])