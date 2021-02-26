from oauth2client import file
from googleapiclient.discovery import build
from httplib2 import Http


store = file.Storage('drive-python-upload.json')
creds = store.get()

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (
    './hello.txt',
)

folder_id = '1QNln3KZAisoV61a0LejnQ5MZ4KoPyes9'

for file_title in FILES:
    file_name = file_title
    metadata = {'name': 'test', #업로드 이후 파일명
                'parents': [folder_id],
                'mimeType': None
                }
    res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
    if res:
        print('uploaded "%s" (%s)' % (file_name, res['mimeType']))
        # print('uploaded "%s" (%s)' % (file_name, res))
