# Imports from 3rd party libraries
# import joblib
<<<<<<< HEAD
from joblib import load
=======
#from joblib import load
#pipeline = load('assets/pipeline_joblib')
# a copy of the filepath (r'C:\Users\pflee\Desktop\Local Work\Video-Game-Rating-Formal\Video-Game-Rating\assets\pipline_joblib')
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# from joblib import load
# pipeline = load('assets/pipeline.joblib')

# Imports from this application
from app import app
from joblib import load

<<<<<<< HEAD
model = load('assets/model_gb')
=======
model = load('assets/model_xgb')
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b

category_list = ['film & video','art','technology','comics','fashion','crafts','publishing','design','food','theater','music','dance','photography']

sub_category_list = ['illustration', 'action', 'accessories', 'radio & podcasts',
       'hardware', 'woodworking', 'product design', 'narrative film',
       'drinks', 'events', 'cookbooks', 'documentary', 'plays',
       'footwear', 'mixed media', 'digital art', 'places', 'sculpture',
       'ready-to-wear', 'shorts', 'webcomics', 'painting',
       'performance art', 'family', 'anthologies', 'graphic design',
       'comic books', 'apps', 'software', '3d printing', 'comedy', 'web',
       'world music', "children's books", 'public art', 'pop', 'diy',
       'science fiction', 'immersive', 'vegan', 'fiction', 'gadgets',
       'wearables', 'performances', 'r&b', 'horror', 'experimental',
       'art books', 'sound', 'festivals', 'conceptual art', 'webseries',
       'civic design', 'apparel', 'animation', 'printing', 'nonfiction',
       'poetry', 'graphic novels', 'musical', 'food trucks', 'photobooks',
       'textiles', 'drama', 'music videos', 'jewelry', 'thrillers',
       'stationery', 'movie theaters', 'periodicals', 'small batch',
       'fantasy', 'fine art', 'farms', 'candles', 'television',
       'installations', 'pottery', 'typography', 'rock',
       'fabrication tools', 'diy electronics', 'crochet', 'couture',
       'video art', 'calendars', 'community gardens', 'residencies',
       'romance', 'bacon', 'academic', 'punk', 'literary journals',
       'young adult', "farmer's markets", 'flight', 'interactive design',
       'architecture', 'childrenswear', 'ceramics', 'zines', 'metal',
       'people', 'space exploration', 'spaces', 'knitting', 'pet fashion',
       'glass', 'robots', 'toys', 'nature', 'camera equipment',
       'embroidery', 'makerspaces', 'restaurants', 'weaving',
       'social practice', 'workshops', 'literary spaces', 'translations',
       'letterpress', 'quilts']

column1 = dbc.Col(
    [
<<<<<<< HEAD
        dcc.Markdown('''###### Category'''),
         dcc.Dropdown(
        id='category_1',
=======
        dcc.Markdown('''#### Category'''),
         dcc.Dropdown(
        id='category-dropdown',
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
        options=[
        {'label': i, 'value': i} for i in category_list
       ],
        value='art',
        className='mb-4'), 

        
<<<<<<< HEAD
        dcc.Markdown('''###### Sub Category'''),
         dcc.Dropdown(
        id='sub_category',
=======
        dcc.Markdown('''#### Sub Category'''),
         dcc.Dropdown(
        id='sub-category-dropdown',
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
        options=[
        {'label': i, 'value': i} for i in sub_category_list
       ],
        value='diy',
        className='mb-4'), 


<<<<<<< HEAD
        dcc.Markdown('''###### Goal (USD)'''),
        dcc.Slider(
            id='goal_in_usd',
=======
        dcc.Markdown('''#### Goal (USD)'''),
        dcc.Slider(
            id='goal-usd-slider',
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
            min=0,
            max=100000000,
            step=50000,
            value=1000,
        ),
<<<<<<< HEAD
        dcc.Markdown('', id='goal_in_usd'),


        dcc.Markdown('''###### Campaign Duration'''),
        dcc.Slider(
            id='campaign_duration',
=======
        dcc.Markdown('', id='goal-usd-slider-container'),


        dcc.Markdown('''#### Campaign Duration'''),
        dcc.Slider(
            id='campaign-duration-slider',
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
            min=2,
            max=100,
            step=10,
            value=2,
        ),
<<<<<<< HEAD
        dcc.Markdown('', id='campaign-duration-container'),
        
        html.H2('Possibility of Success', className='mb-5')
=======
        dcc.Markdown('', id='campaign-duration-slider-container'),
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b

        ],
    )

column2 = dbc.Col(
    [
<<<<<<< HEAD
        dcc.Markdown('''###### Backers Count'''),
        dcc.Slider(
            id='backers_count',
            min=0,
            max=60,
=======
        dcc.Markdown('''#### Backers Count'''),
        dcc.Slider(
            id='backers-count-slider',
            min=0,
            max=50,
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
            step=10,
            value=25,
        ),
        dcc.Markdown('', id='backers-count-slider-container'),


<<<<<<< HEAD
        dcc.Markdown('''###### Blurb Length'''),
        dcc.Slider(
            id='blurb_length',
=======
        dcc.Markdown('''#### Blurb Length'''),
        dcc.Slider(
            id='blurb-length-slider',
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
            min=0,
            max=50,
            step=10,
            value=25,
        ),
        dcc.Markdown('', id='blurb-length-slider-container'),


<<<<<<< HEAD
        dcc.Markdown('''###### Pledged Amount'''),
        
        dcc.Slider(
            id='pledged',
=======
        dcc.Markdown('''#### Pledged Amount'''),
        dcc.Slider(
            id='pledged-amount-slider',
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
            min=5,
            max=10000000,
            step=1000,
            value=500,
        ),
        dcc.Markdown('', id='pledged-amount-slider-container'),

<<<<<<< HEAD

        dcc.Markdown('',id='prediction-content', style={
        'textAlign':'center',
        'font-size':30}), 
        
        html.Div(id='prediction-content', className='lead') 
        
# , style= {"width": "200px", 
#                 "height":"200px"}

        ],
    
    )

# Takes inputs from user and returning to show their selection
@app.callback(
    dash.dependencies.Output('goal-usd-slider-container', 'children'),
    [dash.dependencies.Input('goal_usd', 'value')])
=======
        

        ],
    )

column3 =  dbc.Col([
            # dcc.Markdown('''#### Predicted Status'''),
            
            dcc.Markdown('',id='prediction-content', style={
            'textAlign':'center',
            'font-size':30})
])   

# Takes inputs from user and returning to show their selection
@app.callback(
    dash.dependencies.Output('goal-usd-slider-container', 'children'),
    [dash.dependencies.Input('goal-usd-slider', 'value')])
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
def update_output(value):
    return 'Goal(USD) = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('campaign-duration-slider-container', 'children'),
<<<<<<< HEAD
    [dash.dependencies.Input('campaign_duration', 'value')])
=======
    [dash.dependencies.Input('campaign-duration-slider', 'value')])
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
def update_output(value):
    return 'Campaign Duration = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('backers-count-slider-container', 'children'),
<<<<<<< HEAD
    [dash.dependencies.Input('backers_count', 'value')])
=======
    [dash.dependencies.Input('backers-count-slider', 'value')])
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
def update_output(value):
    return 'Backers Count = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('blurb-length-slider-container', 'children'),
<<<<<<< HEAD
    [dash.dependencies.Input('blurb_length', 'value')])
=======
    [dash.dependencies.Input('blurb-length-slider', 'value')])
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
def update_output(value):
    return 'Blurb Length = "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('pledged-amount-slider-container', 'children'),
<<<<<<< HEAD
    [dash.dependencies.Input('pledged', 'value')])
=======
    [dash.dependencies.Input('pledged-amount-slider', 'value')])
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
def update_output(value):
    return 'Pledged Amount = "{}"'.format(value)

# Callback for the prediction container
@app.callback(
    Output('prediction-content','children'),
<<<<<<< HEAD
    [ Input('backers_count', 'value'),
      Input('category', 'value'),
      Input('pledged', 'value'),
      Input('blurb_length', 'value'),
      Input('goal_in_usd', 'value'),
      Input('campaign_duration', 'value'),      
      Input('sub_category', 'value')
     ])

# backers_count,category,pledged,state,blurb_length,goal_in_usd,campaign_duration,sub_category

def predict(backers_count,category,pledged,state,blurb_length,goal_in_usd,campaign_duration,sub_category):
    df = pd.DataFrame(columns=["backers_count","category","pledged","state","blurb_length","goal_in_usd","campaign_duration","sub_category"], 
    data=[[backers_count,category,pledged,state,blurb_length,goal_in_usd,campaign_duration,sub_category]])
    y_pred = model.predict(df)[0]
    y_pred_prob = model.predictproba(df)[0]
    return "This campaign is {} likely to be {}.".format(round(y_pred_prob,2),y_pred)

layout = dbc.Row([column1, column2])
=======
    [ Input('category-dropdown', 'value'),
      Input('sub-category-dropdown', 'value'),
      Input('goal-usd-slider', 'value'),
      Input('campaign-duration-slider', 'value'),
      Input('backers-count-slider', 'value'),
      Input('blurb-length-slider', 'value'),
      Input('pledged-amount-slider', 'value')
     ])
def predict(category,subcategory,goalinusd,campaignduration,backerscount,blurblength,pledged):
    df = pd.DataFrame(columns=['category','sub_category','goal_in_usd','campaign_duration','backers_count','blurb_length','pledged'], 
    data=[[category,subcategory,goalinusd,campaignduration,backerscount,blurblength,pledged]])
    y_pred = model.predict(df)[0]
    if y_pred == 1:
        return "This campaign is likely to be successful."
    else:
        return "This campaign is likely to fail."
    #y_pred_prob = model.predictproba(df)[0]
    #return "This campaign is {} likely to be {}.".format(round(y_pred_prob,2),y_pred)
    #return "This campaign is likely to be {}.".format(y_pred)
layout = dbc.Row([column1, column2, column3])
>>>>>>> cda26828998a7ffd6b789cd304a1b119ce7a840b
