import ftplib
import requests
from pathlib import Path

# FTP login information
ftp_host = '103.42.57.100'
ftp_user = 'tool'
ftp_password = 'aaztZ5FWATmmXiyF'

# Google Drive file URL
file_url = 'https://drive.google.com/uc?export=download&id=18dpGq_qbmBQ9MRdeeiWnZo3PITjKUbkH'
local_filename = 'index.html'

def download_file(url, local_path):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    with open(local_path, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded to {local_path}")

def upload_file_to_ftp(local_path, ftp_host, ftp_user, ftp_password, ftp_dir):
    with ftplib.FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_password)
        ftp.cwd(ftp_dir)
        with open(local_path, 'rb') as file:
            ftp.storbinary(f'STOR {Path(local_path).name}', file)
        print(f"File uploaded to FTP directory {ftp_dir}")

# Step 1: Download the file
download_file(file_url, local_filename)

# Step 2: Upload the file to the FTP server
upload_file_to_ftp(local_filename, ftp_host, ftp_user, ftp_password, '/lich/lich-am-hom-nay')
