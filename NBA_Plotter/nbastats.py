import pandas
import requests
import json
import os


def main():
    df = scrapeURL()
    df.head()
    #print(df)
    df.to_csv('./data/sampledata.csv', header=df.columns.values, index=False)


def scrapeURL():
    user_agent_headers = {'user-agent':
                              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

    baseURL_playerstat = 'http://stats.nba.com/stats/leaguedashplayerstats?'

    parameters_playerstat = {
        'College': '',
        'Conference': '',
        'Country': '',
        'DateFrom': '',
        'DateTo': '',
        'Division': '',
        'DraftPick': '',
        'DraftYear': '',
        'GameScope': '',
        'GameSegment': '',
        'Height': '',
        'LastNGames': 0,
        'LeagueID': '00',
        'Location': '',
        'MeasureType': 'Base',
        'Month': 0,
        'OpponentTeamID': 0,
        'Outcome': '',
        'PORound': 0,
        'PaceAdjust': 'N',
        'PerMode': 'PerGame',
        'Period': 0,
        'PlayerExperience': '',
        'PlayerPosition': '',
        'PlusMinus': 'N',
        'Rank': 'N',
        'Season': '2016-17',
        'SeasonSegment': '',
        'SeasonType': 'Regular Season',
        'ShotClockRange': '',
        'StarterBench': '',
        'TeamID': 0,
        'VsConference': '',
        'VsDivision': '',
        'Weight': '',
    }

    response = requests.get(baseURL_playerstat, params=parameters_playerstat, headers=user_agent_headers)
    response.raise_for_status()
    headers = response.json()['resultSets'][0]['headers']
    stats = response.json()['resultSets'][0]['rowSet']

    #print(json.dumps(response.json(), indent=4, sort_keys=True))

    stats_df = pandas.DataFrame(stats, columns=headers)
    stats_df['Season'] = parameters_playerstat['Season']
    stats_df.drop(['AGE', 'TEAM_ID' , 'GP', 'W', 'L', 'W_PCT', 'PLAYER_ID', 'BLK_RANK',  'BLKA_RANK',  'PF_RANK', 'CFID', 'CFPARAMS'], axis=1, inplace=True)
    return stats_df


if __name__ == '__main__':
    main()
