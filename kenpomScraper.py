#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 19:59:08 2022

@author: roberthannon
"""

import requests
from bs4 import BeautifulSoup


URL = "https://kenpom.com/"
result = requests.get(URL)

soup = BeautifulSoup(result.content, 'html5lib')

#print(soup.prettify())
#print(soup.get_text())

#res = soup.title

#print(res.get_text())

#print(list(soup.children))

items = [type(item) for item in list(soup.children)]

#print(items)

html = list(soup.children)[1]

#print(list(html.children))

#print(type(item) for item in list(html.children))

#iterator = html.find_all('a')

iteratorNew = html.find_all('a')

iteratorWords = [x.get_text() for x in iteratorNew]

iteratorConf = html.find_all('td', class_='conf')

iteratorTeam = html.find_all('td', class_='next_left')

iteratorConference = [x.get_text() for x in iteratorConf]

iteratorTeams = [x.get_text() for x in iteratorTeam]

#print(iteratorTeams)

i = 0

teamsConf = {}

for x in iteratorTeams:
    teamsConf[x] = [i + 1, iteratorConference[i]]
    i = i + 1
        

#print(teamsConf)

val = input("What would you like to know? Press c for conference ranking, n for total ncaa rankings, h for head to head rankings, i for individual rankings, or b to see the best matchups of the day \n")

if val == "n":
    i = 1
    for x in iteratorTeams:
        print (i, iteratorTeams[i-1], iteratorConference[i-1], "\n")
        i = i + 1
        
if val == "c":
    i = 0
    p = 1
    conf = input("What Conference? \n")
    for x in iteratorConference:
        if x == conf:
            print(p, iteratorTeams[i])
            p = p + 1
        i = i + 1
    
if val == "h":
    team1 = input("Team name? \n")
    team2 = input("Another? \n")
    if teamsConf[team1][0] < teamsConf[team2][0]:
        print(team1)
    else:
        print(team2)
    
if val == "i":
    team = input("Team name? \n")
    print(teamsConf[team][0], team)
    
    
    
if val == "b":
    URL2 = "https://www.ncaa.com/scoreboard/basketball-men/d1"
    result2 = requests.get(URL2)

    soup2 = BeautifulSoup(result2.content, 'html5lib')

    iteratorNew2 = soup2.find_all('span', class_= 'gamePod-game-team-name')

    iteratorWords2 = [x.get_text() for x in iteratorNew2]
    
    games = []
    
    i = 0
    
    while i < len(iteratorWords2):
        games.append([iteratorWords2[i], iteratorWords2[i + 1]])
        i = i + 2
    
    gamesRanking = []
    
    for x in games:
        if x[0] == "Southern U.":
            x[0] = "Southern"
        elif x[1] == "Southern U.":
            x[1] = "Southern"
        if x[0] == "Col. of Charleston":
            x[0] = "Charleston"
        elif x[1] == "Col. of Charleston":
            x[1] = "Charleston"
        if x[0] == "Central Conn. St.":
            x[0] = "Central Connecticut"
        elif x[1] == "Central Conn. St.":
            x[1] = "Central Connecticut"
        if x[0] == "N.C. Central":
            x[0] = "North Carolina Central"
        elif x[1] == "N.C. Central":
            x[1] = "North Carolina Central"
        if x[0] == "Bethune-Cookman":
            x[0] = "Bethune Cookman"
        elif x[1] == "Bethune-Cookman":
            x[1] = "Bethune Cookman"
        if x[0] == "Grambling":
            x[0] = "Grambling St."
        elif x[1] == "Grambling":
            x[1] = "Grambling St."
        if x[0] == "Prairie View":
            x[0] = "Prairie View A&M"
        elif x[1] == "Prairie View":
            x[1] = "Prairie View A&M"
        if x[0] == "UMES":
            x[0] = "Maryland Eastern Shore"
        elif x[1] == "UMES":
            x[1] = "Maryland Eastern Shore"
        if x[0] == "Alcorn":
            x[0] = "Alcorn St."
        elif x[1] == "Alcorn":
            x[1] = "Alcorn St."
        if x[0] == "UConn":
            x[0] = "Connecticut"
        elif x[1] == "UConn":
            x[1] = "Connecticut"
        if x[0] == "ETSU":
            x[0] = "East Tennessee St."
        elif x[1] == "ETSU":
            x[1] = "East Tennessee St."
        if x[0] == "St. John's (NY)":
            x[0] = "St. John's"
        elif x[1] == "St. John's (NY)":
            x[1] = "St. John's"
        if x[0] == "CSU Bakersfield":
            x[0] = "Cal St. Bakersfield"
        elif x[1] == "CSU Bakersfield":
            x[1] = "Cal St. Bakersfield"
        gamesRanking.append([x[0], x[1], abs(teamsConf[x[0]][0] - teamsConf[x[1]][0])])
    
    
    for x in range(len(gamesRanking)-1, 0, -1):
        for y in range(x):
            if gamesRanking[y][2] > gamesRanking[y+1][2]:
                temp = gamesRanking[y]
                gamesRanking[y] = gamesRanking[y + 1]
                gamesRanking[y+1] = temp
    

    i=0
    for x in gamesRanking:
        i = i + 1
        print(i, x[0], "at", x[1])
        
    
                                            
                    
            
        
    
        
        


