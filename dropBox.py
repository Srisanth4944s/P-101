import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):        
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as fileReader:
            dbx.files_upload(fileReader.read(), file_to)

def main():
    access_token = 'iX6JRBgPleUAAAAAAAAAAToHuWyDGLona361JGPWhPUX8AO414w7K3KANgqF9LZL'
    tData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt' 

    tData.upload_file(file_from, file_to)

main()


