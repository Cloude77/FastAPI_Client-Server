import requests
import sys

SERVER_URL = "http://localhost:8000"


def upload_file(file_path):
    with open(file_path, 'rb') as file:
        response = requests.post(f"{SERVER_URL}/upload", files={"file": file})

        if response.status_code == 200:
            print(f"File {file_path} uploaded successfully.")
        else:
            print(f"Failed to upload file. Status code: {response.status_code}")


def download_file(filename):
    response = requests.get(f"{SERVER_URL}/download", params={"filename": filename})

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"File {filename} download successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python client.py [upload/download] [file_path/filename]")
        sys.exit(1)

    action = sys.argv[1]
    file_arg = sys.argv[2]

    if action == "upload":
        upload_file(file_arg)
    elif action == "download":
        download_file(file_arg)
    else:
        print("Invalid action. Use 'upload' or 'download'.")
