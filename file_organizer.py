import os
import shutil

def organize_files(path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            file_extension = os.path.splitext(filename)[1]
            directory_path = os.path.join(path, file_extension[1:].upper() + '_files')
            if not os.path.exists(directory_path):
                os.mkdir(directory_path)
            shutil.move(os.path.join(path, filename), os.path.join(directory_path, filename))
    print('Organizing files completed successfully!')

if __name__ == '__main__':
    path = '/Users/subodh/Downloads/bckp-2'
    organize_files(path)