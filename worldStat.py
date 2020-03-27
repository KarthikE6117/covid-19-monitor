import requests
import pandas as pd
import datetime
import json
import csv
import time

try:
    def exceptionCompromise():    
        star = 30*"*"
        appendCount = 0
        getsTriggered = 0
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"

        headers = {
            'x-rapidapi-host' : 'coronavirus-monitor.p.rapidapi.com',
            'x-rapidapi-key' : 'YOUR API KEY'                  # fetch your key before execution
        }
        print("COVID-19 Monitor Initiated - STAMP : "+ str(datetime.datetime.now()))
        phpList = ["affected.php", "cases_by_particular_country", "worldstat.php", "latest_stat_by_country.php"]  #available endpoints... for further development 
        response = requests.get(url, headers = headers)
        responseJSON = response.json()
        jsonObject = json.loads(response.text)
        beautifiedJson = json.dumps(jsonObject, indent = 2)

        print(beautifiedJson) 

        
        print("\nAPPENDING WORLD STATISTICS"+star)
        print("Total Cases : "+str(responseJSON['total_cases'])+"\n"+"Total Deaths : "+str(responseJSON['total_deaths'])+"\n"+"Total Recovered : "+str(responseJSON['total_recovered'])+"\n"+"New Cases : "+str(responseJSON['new_cases'])+"\n"+"New Deaths : "+str(responseJSON['new_deaths'])+"\n")
        print(star+" Recorded on: "+responseJSON['statistic_taken_at']+" "+star)

        getsTriggered += 1
        numberOfCases = str(responseJSON['total_cases'])
        numberOfDeaths = str(responseJSON['total_deaths'])
        numberOfPatientsRecovered = str(responseJSON['total_recovered'])
        numberOfNewCases = str(responseJSON['new_cases'])
        numberOfNewDeaths = str(responseJSON['new_deaths'])

        colsList = ['total_cases', 'total_deaths', 'total_recovered', 'new_cases', 'new_deaths', 'statistic_taken_at'] #csv headers


        def noCases(numberOfCases, jResp):
            if numberOfCases != str(jResp['total_cases']):
                return True
            else:
                return False

        def noDeaths(numberOfDeaths, jResp):
            if numberOfDeaths != str(jResp['total_deaths']):
                return True
            else:
                return False

        def noRecovered(numberOfPatientsRecovered, jResp):
            if numberOfPatientsRecovered != str(jResp['total_recovered']):
                return True
            else:
                return False

        def noNewCases(numberOfNewCases, jResp):
            if numberOfNewCases != str(jResp['new_cases']):
                return True
            else:
                return False

        def noNewDeaths(numberOfNewDeaths, jResp):
            if numberOfNewDeaths != str(jResp['new_deaths']):
                return True
            else:
                return False

        def conditionOnSuccess(dataSetList):  #unused method...
            writer.writerow(dataSetList)

        def listGenerator(numberOfCases, numberOfDeaths, numberOfPatientsRecovered, numberOfNewCases, numberOfNewDeaths, statTakenOn):
            dataList = [numberOfCases, numberOfDeaths, numberOfPatientsRecovered, numberOfNewCases, numberOfNewDeaths, statTakenOn]
            return dataList

        #with open('dataSetNight.csv', 'w', newline='') as file:   #for initial purpose only
        with open('dataSet.csv', 'a+', newline='') as file:
            
            writer = csv.writer(file)
            #writer.writerow(colsList)      #for initial purpose only (header part)        
            initiator = 0
            
            while True:
                
                newResp = requests.get(url, headers = headers)
                getsTriggered +=1
                jResp = newResp.json()
                cases = noCases(numberOfCases, jResp)
                deaths = noDeaths(numberOfDeaths, jResp)
                recovered = noRecovered(numberOfPatientsRecovered, jResp) 
                newCases = noNewCases(numberOfNewCases, jResp)
                newDeaths = noNewDeaths(numberOfNewDeaths, jResp) 
                
                if initiator == 0:
                    
                    initRowList = [str(jResp['total_cases']), str(jResp['total_deaths']), str(jResp['total_recovered']), str(jResp['new_cases']), str(jResp['new_deaths']), str(jResp['statistic_taken_at'])]
                    writer.writerow(initRowList)
                    initiator = 1
                
                if cases or deaths or recovered or newCases or newDeaths == True:
                    
                    success = 1
                    numberOfCases = str(jResp['total_cases'])
                    numberOfDeaths = str(jResp['total_deaths'])
                    numberOfPatientsRecovered = str(jResp['total_recovered'])
                    numberOfNewCases = str(jResp['new_cases'])
                    numberOfNewDeaths = str(jResp['new_deaths'])
                    statTakenOn = str(jResp['statistic_taken_at'])
                    
                    dataSetList = listGenerator(numberOfCases, numberOfDeaths, numberOfPatientsRecovered, numberOfNewCases, numberOfNewDeaths, statTakenOn)
                    # call for conditionOnsuccess
                    writer.writerow(dataSetList)
                    #printing FromNow JSONs
                    print("New Data Recorded : "+ str(datetime.datetime.now()))
                    jsonObjectFromNow = json.loads(newResp.text)
                    beautifiedJsonFromNow = json.dumps(jsonObjectFromNow, indent = 2)
                    print(beautifiedJsonFromNow)
                    print(star+star)
                    
                    if success == 1:
                        appendCount += 1
                        print("Number of Appends :", appendCount)
                        print("GETs Triggered so far :", getsTriggered)
                        print(star+star)
                        success = 0
                else:
                    time.sleep(2)        #to reduce the network usage 
    exceptionCompromise()
except requests.exceptions.ConnectionError:    
    print("Connection Timed Out.\nEstablishing Connection within a while...")
    time.sleep(5)
    exceptionCompromise()

