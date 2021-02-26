import os

file_list = os.listdir('./secret_keys')
if 'drive-python-upload.json' in file_list:
    pass
else:
    import create_token
