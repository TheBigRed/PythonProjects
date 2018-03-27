import nbastats_api
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = nbastats_api.get_playerisolation()
    df.head()
    print(df)

    df.to_csv('./data/sampledata_new.csv', header=df.columns.values, index=False)

    # fig, ax = plt.subplots()
    # plt.scatter(df['GROUP_VALUE'], df['FG_PCT'] * 100)
    # ax.set_title("Shooting percentages active career")
    # plt.show()


if __name__ == '__main__':
    main()


'''Get particular row from dataframe && plot it'''
#plt.scatter(df.loc[405]['FGA'], df.loc[405]['FGM'])

'''Get certain columns and put into new dataframe'''
#df_new = df[['PLAYER_NAME', 'MIN', 'FGM', 'FGA', 'FG3M', 'FG3A', 'PTS']].copy()