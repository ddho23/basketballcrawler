from basketballCrawler import basketballCrawler as bc

players = bc.buildPlayerDictionary(suppressOutput=False)
bc.savePlayerDictionary(players, 'players.json')