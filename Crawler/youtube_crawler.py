from googleapiclient.discovery import build

'''
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
'''


def search_crawling(query=None, max_results=10):
    DEVELOPER_KEY = "AIzaSyAH5Jbsl1i7YGvjXlc9I0baw9ihjOKkzJo"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    '''
    q: search keyword
    order: order method
    part: required parameters
    maxResults: num of results
    '''

    response = youtube.search().list(q=query,
                                     order="date",
                                     part="snippet",
                                     maxResults=max_results).execute()
    response = response['items']

    result = {'video_ids': [], 'pub_at': [], 'channel_ids': [], 'video_titles': [], 'descriptions': [],
              'thumbnails': [], 'channel_titles': []}

    for item in response:
        result['video_ids'].append(item['id']['videoId'])
        result['pub_at'].append(item['snippet']['publishedAt'])
        result['channel_ids'].append(item['snippet']['channelId'])
        result['video_titles'].append(item['snippet']['title'])
        result['descriptions'].append(item['snippet']['description'])
        result['thumbnails'].append(item['snippet']['thumbnails'])
        result['channel_titles'].append(item['snippet']['channelTitle'])

    return result



