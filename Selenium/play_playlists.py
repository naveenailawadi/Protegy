from SpotifyObject import SpotifyBot
from secrets import USERNAME, PASSWORD
import pandas as pd
import sys


def main(csv):
    bot = SpotifyBot()
    bot.login(USERNAME, PASSWORD)

    # get the playlists and playtimes
    df = pd.read_csv(csv)

    # go through all the rows
    for index, row in df.iterrows():
        bot.play_playlist(row['playlist'], row['playtime'])


if __name__ == '__main__':
    csv = sys.argv[1]
    print(f"Going to play megaplaylist in {csv}")
    main(csv)
