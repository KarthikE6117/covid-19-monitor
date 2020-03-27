# covid19-monitor
This project is helpful in gathering the live global COVID19 statistical data to maintain a proper time based Dataset for further machine analysis/learning.

# About

Hey Coderz and Devs' out there! I'am Karthik. This is an API script which fetches the live COVID-19 data hosted in RAPID-api domain. This service was developed by 'astsiatsko' and this came to my view through RAPID-api platform. I have written this script to fetch the live data which are contained in JSON and fragment those JSON stuff into normal data. These data are furtherly comma seperated and appended as rows in a .csv file. This .csv file containing a history of time based data can be considered as a dataset and further statistical analysis and learning can be carried out with this dataset. So that we could be able to visualize the data with some graplical plots and analize the rates for the available parameters.
Public commits are always appriciated. If so ping me!

In order to use this script, first you have to sign up your free account in https://rapidapi.com/

Then head to this link and copy your API key which is present in a field named "X-RapidAPI-Key".

Then paste your key in line 17 of worldStat.py and proceed firing up the script.

-----------

# Libraries Required
  * requests
  * pandas 
  * datetime
  * json
  * csv
  * time
----------

# Usage

* Install the required libraries using the command,
                                
      pip install -r requirements.txt

* Run the main python file worldStat.py using the following command,

for windows,
    
    python3 worldStat.py
    
for linux,

    chmod 777 worldStat.py
    python3 worldStat.py
    
----------
    
# Developer's Info

Name: Karthik.

Email: karthikelango6117@gmail.com

Country: India.
