import os
import shutil

# Define the paths
downloads_folder = os.path.expanduser('~/Downloads')

# Define the destination folders for different file types
destination_folders = {
    'videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov', '.wmv'],
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'programs': ['.exe', '.msi', '.dmg', '.bat', '.sh', '.msix'],
    'documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.ppt', '.csv', '.epub', '.rtf'],
    'compressed': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '3d': ['.fbx', '.obj', '.gltf', 'stl', '.amf', '.3mf'],
}

# Create directories if they don't exist
for folder in destination_folders:
    os.makedirs(os.path.join(downloads_folder, folder), exist_ok=True)


# Function to move files based on their extension
def move_file(file_name):
    file_extension = os.path.splitext(file_name)[1].lower()

    for category, extensions in destination_folders.items():
        if file_extension in extensions:
            source = os.path.join(downloads_folder, file_name)
            destination = os.path.join(downloads_folder, category, file_name)

            print(f'Moving {file_name} to {category}')
            shutil.move(source, destination)
            return


# Get a list of files in the Downloads folder
files = [f for f in os.listdir(downloads_folder) if os.path.isfile(os.path.join(downloads_folder, f))]

# Move each file to the appropriate folder
for file in files:
    move_file(file)

print("File organization completed.")
