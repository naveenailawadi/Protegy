from bs4 import BeautifulSoup
import pandas as pd
import requests

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

site_data = []
column_names = ['headline', 'summary', 'video_link']

for article in soup.find_all('article'):

    headline = article.h2.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://www.youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    site_data.append([headline, summary, yt_link])

df = pd.DataFrame(data=site_data, columns=column_names)

df.to_csv('coreys_file.csv', index=False)

print(df)
