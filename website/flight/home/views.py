from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pickle 

# utility functions 
def load_dataset():
    # load the dataset using pickle
    with open("N:/ml-projects/regression/flight-price-prediction-using-sagemaker/Notebooks/df.pkl","rb") as file:
        df= pickle.load(file)
        return df

def predict(airline,date,src,dest,departure, arrival_time, duration, total_stops):
    pass 
# Create your views here.
def home(request):

    if request.method == "POST":
        airline = request.POST.get('airline')
        date = request.POST.get('date')
        src = request.POST.get('src')
        dest = request.POST.get('dest')
        departure = request.POST.get('departure')
        arrival_time = request.POST.get('arrival-time')
        duration = request.POST.get('duration')
        total_stops = request.POST.get('total-stops')
        additional_info = request.POST.get('additional')

        prediction= predict(airline,date,src,dest,departure, arrival_time, duration, total_stops)

    else:
        df= load_dataset()

        airline= df['airline'].unique().tolist()
        source= df['source'].unique().tolist()
        destination= df['destination'].unique().tolist()
        additional_info= df['additional_info'].unique().tolist()

        context= {
            'airline': airline,
            'source': source,
            'destination': destination,
            'additional_info':additional_info
        }


        template= loader.get_template('home.html')
        return HttpResponse(template.render(context, request))

