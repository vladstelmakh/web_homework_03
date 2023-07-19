import os
import shutil
import concurrent.futures

def process_file(file_path, destination_folder, action):
    filename = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, filename)

    if action == 'move':
        shutil.move(file_path, destination_path)
        print(f"Moved {file_path} to {destination_path}")
    elif action == 'copy':
        shutil.copy(file_path, destination_path)
        print(f"Copied {file_path} to {destination_path}")
    elif action == 'delete':
        os.remove(file_path)
        print(f"Deleted {file_path}")
    else:
        print(f"Invalid action: {action}")

def process_directory(directory, destination_folder, action):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(process_file, file_path, destination_folder, action)

def main():
    # Ввод директории и выбор действия из консоли
    directory = input("Enter the directory to process: ")
    destination_folder = input("Enter the destination directory: ")
    action = input("Select an action for files ('move', 'copy', or 'delete'): ")

    # Проверка существования директорий
    if not os.path.exists(directory):
        print(f'Directory "{directory}" does not exist.')
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Обработка папки с использованием нескольких потоков
    process_directory(directory, destination_folder, action)

    print('Sorting complete.')

if __name__ == '__main__':
    main()
