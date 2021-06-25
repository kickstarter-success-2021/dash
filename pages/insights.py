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
            
            The random forest classifier, the model serving this app, shows that the most important factors are the number of initial backers, 
            
            the goal in usd and the pledged amount. The picture below shows our model's features. The model illustrates the simple truth that 
            
            fund-rasing success is about securing investors. However, the subcategory is often the  last straw that may make or break the deal. 
            
            
            
            In plain English, the classifers detect failures, about 40% of total cases, with the backer_counts and pledged amount, rather than 
            
            categories or sub-categories, which ranked as the 4th most important factor. We can only live with the best tool that we have, and use  
            
            our models, especially those that think like us, with much caution. After all as in all good investments, honesty is in details, and good
            
            projects are highly tailored to specific needs. Let us all judge investments with caution. 
            
            
            
             

            """
        
        ), 
    
    # html.Img(src='assets/Rating Distribution.PNG', className='img-fluid'),

    html.Img(src='assets/rf_kickstarter.png', className='img-fluid')
    
    ],
)



       
layout = dbc.Row([column1])