from distutils.log import debug
import pickle
from re import X
from click.core import F
from flask import Flask, json,request,app,jsonify,url_for,render_template
import numpy as np
from numpy.core.numeric import outer
import pandas as pd

app= Flask(__name__)
#Project = pd.read_csv("https://raw.githubusercontent.com/sriram-22/Mushroom_Classification/main/mushrooms.csv")
model=pickle.load(open('rfmodel.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html',
    F1 = [{'cap_shape':'bell','map':0},{'cap_shape':'conical','map':1},{'cap_shape':'flat','map':2},{'cap_shape':'knobbed','map':3},{'cap_shape':'sunken','map':4},{'cap_shape':'convex','map':5}], 
    F2 = [{'cap_surface':'fibrous','map':0},{'cap_surface':'grooves','map':1},{'cap_surface':'smooth','map':2},{'cap_surface':'scaly','map':3}],
    F3 = [{'cap_color':'buff','map':0},{'cap_color':'cinnamon','map':1},{'cap_color':'red','map':2},{'cap_color':'gray','map':3},{'cap_color':'brown','map':4},{'cap_color':'pink','map':5},{'cap_color':'green','map':6},{'cap_color':'purple','map':7},{'cap_color':'white','map':8},{'cap_color':'yellow','map':9}],
    F4 = [{'bruises':'no','map':0},{'bruises':'bruises','map':1}],
    F5 = [{'odor':'almond','map':0},{'odor':'creosote','map':1},{'odor':'foul','map':2},{'odor':'anise','map':3},{'odor':'musty','map':4},{'odor':'none','map':5},{'odor':'pungent','map':6},{'odor':'spicy','map':7},{'odor':'fishy','map':8}],
    F6 = [{'gill_attachment':'attached','map':0},{'gill_attachment':'free','map':1}],
    F7 = [{'gill_spacing':'close','map':0},{'gill_spacing':'crowded','map':1}],
    F8 = [{'gill_size':'broad','map':0},{'gill_size':'narrow','map':1}],
    F9 = [{'gill_color':'buff','map':0},{'gill_color':'red','map':1},{'gill_color':'gray','map':2},{'gill_color':'chocolate','map':3},{'gill_color':'black','map':4},{'gill_color':'brown','map':5},{'gill_color':'orange','map':6},{'gill_color':'pink','map':7},{'gill_color':'green','map':8},{'gill_color':'purple','map':9},{'gill_color':'white','map':10},{'gill_color':'yellow','map':11}],
    F10 = [{'stalk_shape':'enlarging','map':0},{'stalk_shape':'tapering','map':1}],
    F11 = [{'stalk_root':'missing','map':0},{'stalk_root':'bulbous','map':1},{'stalk_root':'club','map':2},{'stalk_root':'equal','map':3},{'stalk_root':'rooted','map':4}],
    F12 = [{'stalk_surface_above_ring':'fibrous','map':0},{'stalk_surface_above_ring':'silky','map':1},{'stalk_surface_above_ring':'smooth','map':2},{'stalk_surface_above_ring':'scaly','map':3}],
    F13 = [{'stalk_surface_below_ring':'fibrous','map':0},{'stalk_surface_below_ring':'silky','map':1},{'stalk_surface_below_ring':'smooth','map':2},{'stalk_surface_below_ring':'scaly','map':3}],
    F14 = [{'stalk_color_above_ring':'buff','map':0},{'stalk_color_above_ring':'cinnamon','map':1},{'stalk_color_above_ring':'red','map':2},{'stalk_color_above_ring':'gray','map':3},{'stalk_color_above_ring':'brown','map':4},{'stalk_color_above_ring':'orange','map':5},{'stalk_color_above_ring':'pink','map':6},{'stalk_color_above_ring':'white','map':7},{'stalk_color_above_ring':'yellow','map':8}],
    F15 = [{'stalk_color_below_ring':'buff','map':0},{'stalk_color_below_ring':'cinnamon','map':1},{'stalk_color_below_ring':'red','map':2},{'stalk_color_below_ring':'gray','map':3},{'stalk_color_below_ring':'brown','map':4},{'stalk_color_below_ring':'orange','map':5},{'stalk_color_below_ring':'pink','map':6},{'stalk_color_below_ring':'white','map':7},{'stalk_color_below_ring':'yellow','map':8}],
    F16 = [{'veil_type':'partial','map':0}],
    F17 = [{'veil_color':'brown','map':0},{'veil_color':'orange','map':1},{'veil_color':'white','map':2},{'veil_color':'yellow','map':3}],
    F18 = [{'ring_number':'none','map':0},{'ring_number':'one','map':1},{'ring_number':'two','map':2}],
    F19 = [{'ring_type':'evanescent','map':0},{'ring_type':'flaring','map':1},{'ring_type':'large','map':2},{'ring_type':'none','map':3},{'ring_type':'pendant','map':4}],
    F20 = [{'spore_print_color':'buff','map':0},{'spore_print_color':'chocolate','map':1},{'spore_print_color':'black','map':2},{'spore_print_color':'brown','map':3},{'spore_print_color':'orange','map':4},{'spore_print_color':'green','map':5},{'spore_print_color':'purple','map':6},{'spore_print_color':'white','map':7},{'spore_print_color':'yellow','map':8}],
    F21 = [{'population':'abundant','map':0},{'population':'clustered','map':1},{'population':'numerous','map':2},{'population':'scattered','map':3},{'population':'several','map':4},{'population':'solitary','map':5}],
    F22 = [{'habitat':'woods','map':0},{'habitat':'grasses','map':1},{'habitat':'leaves','map':2},{'habitat':'meadows','map':3},{'habitat':'paths','map':4},{'habitat':'urban','map':5},{'habitat':'waste','map':6}])

"""
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    d = pd.DataFrame(columns=list(Project.columns)[1:])
    d.loc[len(d.index)] = list(data.values())
    output=int(model.predict(d))
    int(output)
    return jsonify(output)
"""

@app.route('/predict',methods=['POST'])
def predict():
    data = [[int(x) for x in request.form.values()]]
    output = int(model.predict(data))
    if output==1:
        final_output = "poisonous"
    else:
        final_output = "edible"
    return render_template("home.html",
        F1 = [{'cap_shape':'bell','map':0},{'cap_shape':'conical','map':1},{'cap_shape':'flat','map':2},{'cap_shape':'knobbed','map':3},{'cap_shape':'sunken','map':4},{'cap_shape':'convex','map':5}], 
    F2 = [{'cap_surface':'fibrous','map':0},{'cap_surface':'grooves','map':1},{'cap_surface':'smooth','map':2},{'cap_surface':'scaly','map':3}],
    F3 = [{'cap_color':'buff','map':0},{'cap_color':'cinnamon','map':1},{'cap_color':'red','map':2},{'cap_color':'gray','map':3},{'cap_color':'brown','map':4},{'cap_color':'pink','map':5},{'cap_color':'green','map':6},{'cap_color':'purple','map':7},{'cap_color':'white','map':8},{'cap_color':'yellow','map':9}],
    F4 = [{'bruises':'no','map':0},{'bruises':'bruises','map':1}],
    F5 = [{'odor':'almond','map':0},{'odor':'creosote','map':1},{'odor':'foul','map':2},{'odor':'anise','map':3},{'odor':'musty','map':4},{'odor':'none','map':5},{'odor':'pungent','map':6},{'odor':'spicy','map':7},{'odor':'fishy','map':8}],
    F6 = [{'gill_attachment':'attached','map':0},{'gill_attachment':'free','map':1}],
    F7 = [{'gill_spacing':'close','map':0},{'gill_spacing':'crowded','map':1}],
    F8 = [{'gill_size':'broad','map':0},{'gill_size':'narrow','map':1}],
    F9 = [{'gill_color':'buff','map':0},{'gill_color':'red','map':1},{'gill_color':'gray','map':2},{'gill_color':'chocolate','map':3},{'gill_color':'black','map':4},{'gill_color':'brown','map':5},{'gill_color':'orange','map':6},{'gill_color':'pink','map':7},{'gill_color':'green','map':8},{'gill_color':'purple','map':9},{'gill_color':'white','map':10},{'gill_color':'yellow','map':11}],
    F10 = [{'stalk_shape':'enlarging','map':0},{'stalk_shape':'tapering','map':1}],
    F11 = [{'stalk_root':'missing','map':0},{'stalk_root':'bulbous','map':1},{'stalk_root':'club','map':2},{'stalk_root':'equal','map':3},{'stalk_root':'rooted','map':4}],
    F12 = [{'stalk_surface_above_ring':'fibrous','map':0},{'stalk_surface_above_ring':'silky','map':1},{'stalk_surface_above_ring':'smooth','map':2},{'stalk_surface_above_ring':'scaly','map':3}],
    F13 = [{'stalk_surface_below_ring':'fibrous','map':0},{'stalk_surface_below_ring':'silky','map':1},{'stalk_surface_below_ring':'smooth','map':2},{'stalk_surface_below_ring':'scaly','map':3}],
    F14 = [{'stalk_color_above_ring':'buff','map':0},{'stalk_color_above_ring':'cinnamon','map':1},{'stalk_color_above_ring':'red','map':2},{'stalk_color_above_ring':'gray','map':3},{'stalk_color_above_ring':'brown','map':4},{'stalk_color_above_ring':'orange','map':5},{'stalk_color_above_ring':'pink','map':6},{'stalk_color_above_ring':'white','map':7},{'stalk_color_above_ring':'yellow','map':8}],
    F15 = [{'stalk_color_below_ring':'buff','map':0},{'stalk_color_below_ring':'cinnamon','map':1},{'stalk_color_below_ring':'red','map':2},{'stalk_color_below_ring':'gray','map':3},{'stalk_color_below_ring':'brown','map':4},{'stalk_color_below_ring':'orange','map':5},{'stalk_color_below_ring':'pink','map':6},{'stalk_color_below_ring':'white','map':7},{'stalk_color_below_ring':'yellow','map':8}],
    F16 = [{'veil_type':'partial','map':0}],
    F17 = [{'veil_color':'brown','map':0},{'veil_color':'orange','map':1},{'veil_color':'white','map':2},{'veil_color':'yellow','map':3}],
    F18 = [{'ring_number':'none','map':0},{'ring_number':'one','map':1},{'ring_number':'two','map':2}],
    F19 = [{'ring_type':'evanescent','map':0},{'ring_type':'flaring','map':1},{'ring_type':'large','map':2},{'ring_type':'none','map':3},{'ring_type':'pendant','map':4}],
    F20 = [{'spore_print_color':'buff','map':0},{'spore_print_color':'chocolate','map':1},{'spore_print_color':'black','map':2},{'spore_print_color':'brown','map':3},{'spore_print_color':'orange','map':4},{'spore_print_color':'green','map':5},{'spore_print_color':'purple','map':6},{'spore_print_color':'white','map':7},{'spore_print_color':'yellow','map':8}],
    F21 = [{'population':'abundant','map':0},{'population':'clustered','map':1},{'population':'numerous','map':2},{'population':'scattered','map':3},{'population':'several','map':4},{'population':'solitary','map':5}],
    F22 = [{'habitat':'woods','map':0},{'habitat':'grasses','map':1},{'habitat':'leaves','map':2},{'habitat':'meadows','map':3},{'habitat':'paths','map':4},{'habitat':'urban','map':5},{'habitat':'waste','map':6}]
    ,prediction = "Your mushroom is "+final_output+ "!")
    

if __name__=="__main__":
    app.run(debug=True)