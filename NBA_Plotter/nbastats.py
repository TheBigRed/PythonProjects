import nbastats_api
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = nbastats_api.get_playerisolation()
    df.head()
    #print(df)

    #df.to_csv('./data/sampledata_new.csv', header=df.columns.values, index=False)
    df1 = df[df.Poss > 200]
    print(df1)
    fig, ax = plt.subplots()
    #plt.scatter(df['GROUP_VALUE'], df['FG_PCT'] * 100)
    plt.scatter(df1['Poss'], df1['PPG'])
    ax.set_title("Shooting percentages active career")
    for label, x, y in zip(df1['PlayerLastName'], df1['Poss'], df1['PPG']):
        plt.annotate(
            label,
            xy=(x, y), xytext=(-5, 5),
            textcoords='offset points', ha='right', va='bottom')
    plt.show()


if __name__ == '__main__':
    main()


'''Get particular row from dataframe && plot it'''
#plt.scatter(df.loc[405]['FGA'], df.loc[405]['FGM'])

'''Get certain columns and put into new dataframe'''
#df_new = df[['PLAYER_NAME', 'MIN', 'FGM', 'FGA', 'FG3M', 'FG3A', 'PTS']].copy()

'''Get subplot with column value over a certain number'''
#df1 = df[df.Poss > 200]

'''Labelling scatter points on scatter plot'''
# for label, x, y in zip(df1['PlayerLastName'], df1['Poss'], df1['PPG']):
#     plt.annotate(
#         label,
#         xy=(x, y), xytext=(-5, 5),
#         textcoords='offset points', ha='right', va='bottom')