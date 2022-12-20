from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from currency_converter import CurrencyConverter
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from django.shortcuts import redirect

import math
from .models import carbonfootprintModel,co2predictModel,co2predictionModel


# input tonnes 

def convert(amount, currency):
    
    c = CurrencyConverter()
    convert = c.convert(amount, str(currency), 'USD')
    
    return convert 

# Create your views here.
# import convert
@csrf_exempt
def foot_print(request):
    if request.method == "POST":
        print(request.POST)
        if 'elecbill' in request.POST:


            electric_bill = request.POST['elecbill']

            gas_bill = request.POST['gasbill']

            oil_bill = request.POST['oilbill']

            yearly_mileage = request.POST['yearmilage']

            currency = request.POST['currency']

            
            electric = int(convert(electric_bill, currency)*105)
        
            gas = int(convert(gas_bill, currency)*105)

            oil = int(convert(oil_bill, currency)*113)

            mile = int(convert(yearly_mileage, currency)*0.79)


          
            total =  electric+gas+oil+mile
            
            
            print("*******************")
            print(total)
            data = {}
            data['formsd'] = 'not'
            data['coemitted'] = str(round(float(total),2))
            ans = (int(total)/1000)*38
            data['value'] = str((int(ans)))
            mod = carbonfootprintModel(electric_bill = electric_bill,  gas_bill = gas_bill, oil_bill = oil_bill,currency=currency,mile=yearly_mileage)
            mod.save()
            data['calculator'] = 'show'
            return render(request,'cal.html',context=data)
            

        else:


            oil_co2 = request.POST['oil_co2']

            oil_co2_per_capita = request.POST['oil_co2_per_capita']

            co2_growth_predt = request.POST['co2_growth_predt']

            co2_growth_abs = request.POST['co2_growth_abs']

            cumulative_co2 = request.POST['cumulative_co2']

            cumulative_oil_co2 = request.POST['cumulative_oil_co2']

            share_global_co2 = request.POST['share_global_co2']

            share_global_oil_co2 = request.POST['share_global_oil_co2']

            share_global_cumulative_co2 = request.POST['share_global_cumulative_co2']

            share_global_cumulative_oil_co2 = request.POST['share_global_cumulative_oil_co2']

            population = request.POST['population']

           


            inputlist = [[oil_co2,oil_co2_per_capita,co2_growth_predt,co2_growth_abs,cumulative_co2,cumulative_oil_co2,share_global_co2,share_global_oil_co2,share_global_cumulative_co2,share_global_cumulative_oil_co2,population]]

            modl =co2predictionModel(oil_co2 = oil_co2,oil_co2_per_capita = oil_co2_per_capita,co2_growth_abs = co2_growth_abs,cumulative_co2 = cumulative_co2,cumulative_oil_co2 = cumulative_oil_co2,share_global_co2 = share_global_co2,share_global_oil_co2 = share_global_oil_co2,share_global_cumulative_co2 = share_global_cumulative_co2,share_global_cumulative_oil_co2 =share_global_cumulative_oil_co2,population = population)
            modl.save()
            li = model(inputlist)
            print("**************************")
            anse = float(li[1])
            ansde = float(li[0])
            

            print(ansde)
            data = {}
            
            ans = int((float(ansde)*10000)*38)
            data['formsd'] = 'not'
            data['value'] = str(int(round(float(ans),4)))
            data['coemitted'] = str(round(float(ansde),2))
            data['percoemitted'] = str((round(float(anse),2)))
            data['calculator'] = 'no'
            data['mi'] = 'yes'
            return render(request,'cal.html',context=data)

  

    return render(request,'model.html')



@csrf_exempt
def tresscal(request):
    data ={
        'formsd' :'show'
    }

    if request.method == "POST":
        co2tocal = request.POST['co2tocal']
        ans = (int(co2tocal)/1000)*38
        data['formsd'] = 'not'
        data['value'] = str(int(ans))
        data['coemitted'] = str(round(int(co2tocal),2))
        data['calculator'] = 'show'

    print(data)
    return render(request,'cal.html',context=data)


@csrf_exempt
def model(inputlist):
    ans = []

    # data = pd.read_csv("data.csv")
    df = pd.read_csv("Clean_data.csv")
    # clean_dataset = data

    # missing_values_year = dict.fromkeys(clean_dataset['year'].unique(), 0)
    # for i, row in clean_dataset.iterrows():
    #     missing_values_year[row['year']] += row.isnull().sum()

    # missing_values_year = dict(sorted(missing_values_year.items(), key=lambda item: item[1]))


    
    # clean_dataset = clean_dataset[(clean_dataset['year'] >= 1991) & (clean_dataset['year'] <= 2020)]

    # countries_count_missing = dict.fromkeys(clean_dataset['country'].unique(), 0)

    # for i, row in clean_dataset.iterrows():
    #     countries_count_missing[row['country']] += row.isnull().sum()

    # countries_missing_sorted = dict(sorted(countries_count_missing.items(), key=lambda item: item[1]))



    # select_countries = []
    # for key, val in countries_missing_sorted.items():
    #     if val<1400:
    #         select_countries.append(key)

    # clean_dataset = clean_dataset[clean_dataset['country'].isin(select_countries)]


    # data = clean_dataset

    # features = ["co2", "co2_per_capita","oil_co2","oil_co2_per_capita","co2_growth_prct","co2_growth_abs","cumulative_co2","cumulative_oil_co2",
    #            "share_global_co2","share_global_oil_co2","share_global_cumulative_co2","share_global_cumulative_oil_co2","population"]

    # remove_features = ['iso_code','trade_co2',
    #         'cement_co2','cement_co2_per_capita', 'flaring_co2', 'flaring_co2_per_capita',"coal_co2","coal_co2_per_capita","cumulative_coal_co2","share_global_coal_co2",
    #        'gas_co2', 'gas_co2_per_capita',"share_global_cumulative_coal_co2",
    #        'other_industry_co2', 'other_co2_per_capita', 
    #        'co2_per_gdp', 'co2_per_unit_energy',
    #        'consumption_co2', 'consumption_co2_per_capita',
    #        'consumption_co2_per_gdp',  'cumulative_cement_co2',
    #         'cumulative_flaring_co2', 'cumulative_gas_co2',
    #         'cumulative_other_co2', 'trade_co2_share',
    #         'share_global_cement_co2', 
    #        'share_global_flaring_co2', 'share_global_gas_co2',
    #         'share_global_other_co2',
    #         'share_global_cumulative_cement_co2',
    #        'share_global_cumulative_flaring_co2',
    #        'share_global_cumulative_gas_co2',
    #        'share_global_cumulative_other_co2', 'total_ghg', 'ghg_per_capita',
    #        'total_ghg_excluding_lucf', 'ghg_excluding_lucf_per_capita', 'methane',
    #        'methane_per_capita', 'nitrous_oxide', 'nitrous_oxide_per_capita',
    #        'gdp', 'primary_energy_consumption', 'energy_per_capita',
    #        'energy_per_gdp']

    # data = data.drop(remove_features,axis='columns')

    # remove = ['country','year']
    # df = data
    # df = df.drop(remove,axis='columns')

    # df.to_csv('Clean_data.csv', index=False)

    df = df.dropna(axis='rows', how='any')

    label_col = ['co2','co2_per_capita']
    features_col = ["oil_co2","oil_co2_per_capita","co2_growth_prct","co2_growth_abs","cumulative_co2","cumulative_oil_co2",
               "share_global_co2","share_global_oil_co2","share_global_cumulative_co2","share_global_cumulative_oil_co2","population"]
    features = np.array(df[features_col])
    labels =  np.array(df[label_col])

    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(features,labels,test_size=0.7,random_state=42)

    from sklearn.ensemble import RandomForestRegressor

    regressor = RandomForestRegressor(random_state = 42)
    regressor.fit(X_train, Y_train) 

    predictions = regressor.predict(X_test)

    regressor.score(X_test,Y_test)
    print("Random Forest Regression Score:",regressor.score(X_test,Y_test))
    predications = regressor.predict(X_test)
    print ("Score on training dataset     :",regressor.score(X_train,Y_train))
    print("Score on testing dataset      :",regressor.score(X_test, Y_test))


    # predictions = regressor.predict([[1.718,0.129,-6.76,-0.176,61.610,31.330,0.01,0.02,0.01,0.01,13299016.0]])
    # print("$$$$$$$$$$$$")
    # print(predictions)
    predictions = regressor.predict(inputlist)
    print("*****************************************************")
    print(predictions)
    return predictions[0][0],predictions[0][1]
