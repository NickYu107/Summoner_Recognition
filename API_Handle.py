import requests

API_KEY = "RGAPI-7e4b0ac2-34fa-4d67-a2b7-8484c848e4bc"
REGION = "na1"

def requestSummonerData(summonerName):
    URL = "https://" + REGION + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + API_KEY
    response = requests.get(URL)
    return response.json()

def requestRankedInformation(ID):
    URL = "https://" + REGION + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + "?api_key=" + API_KEY
    response = requests.get(URL)
    return response.json()

def requestLiveGameInformation(ID):
    URL = "https://" + REGION + ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + ID + "?api_key=" + API_KEY
    response = requests.get(URL)
    return response.json()


def main():
    #Summoner_Name = "Yamikaze"
    Summoner_Name = (str)(input("Please enter your Summoner Name: "))
    Summoner_JSON = requestSummonerData(Summoner_Name)
    Name = Summoner_JSON["name"]
    Level = Summoner_JSON["summonerLevel"]
    Summoner_ID = Summoner_JSON["id"]
    Account_ID = Summoner_JSON["accountId"]

    print("Name: %s"%(Name))
    print("Level: %d"%(Level))
    
    print("--------------------------------------------------Player Ranked Information")
    Ranked_JSON = requestRankedInformation(Summoner_ID)
    if not Ranked_JSON:
        print("Player is Unranked")
    else:
        for item in Ranked_JSON:
            print("Queue Type: %s"%(item["queueType"]))
            print("Division: %s %s | %d Points"%(item["tier"], item["rank"],item["leaguePoints"]))
            print("Wins %d"%(item["wins"]))
            print("Losses %d"%(item["losses"]))
            
            Win_Rate = item["wins"]/(item["wins"]+item["losses"])
            
            print("Win Rate: "+"{:.2%}".format(Win_Rate))
    
    print("--------------------------------------------------Live Game Information")
    #Live_JSON = requestLiveGameInformation(Summoner_ID)
    #print(Live_JSON)
    

if __name__ == "__main__":
    main()