import requests


def mainCall(stateName):

    data = requests.get('https://data.covid19india.org/data.json').json()
    statewise = data['statewise']


    stateDict = {}

    for i in range(len(statewise)):
        statename = ((statewise[i]['state']).lower()).replace(" ","")
        stateDict[statename] = i



    userInp = stateName
    userInp = (userInp.lower()).replace(" ","")

    return statewise[stateDict[userInp]]   



