from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

except ImportError:
    flags = None


CLIENT_SECRET_FILE = './secret_keys/credentials.json'
CREDENTIAL_FILENAME = './secret_keys/drive-python-upload.json'
SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage(CREDENTIAL_FILENAME)
creds = store.get()

if not creds or creds.invalid:
    print('make new storage data file')
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    creds = tools.run_flow(flow, store, flags) if flags else tools.run(flow, store)

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
