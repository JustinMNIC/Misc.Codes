import os
from PIL import Image
import imagehash
import psutil
import time

def find_duplicates(directory):
    hash_dict = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and (filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg')):
            with Image.open(filepath) as img:
                hash_value = str(imagehash.average_hash(img))
            if hash_value in hash_dict:
                print(f"Found duplicate: {filename}")
                os.remove(filepath)
            else:
                hash_dict[hash_value] = filename


def get_processes_using_file(filepath):
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for item in proc.open_files():
                if item.path == filepath:
                    processes.append((proc.info['pid'], proc.info['name']))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def convert_to_webp(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and (filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg')):
            with Image.open(filepath) as img:
                webp_filename = os.path.splitext(filepath)[0] + ".webp"
                img.save(webp_filename, "WEBP")
                for _ in range(5):
                    try:
                        os.remove(filepath)
                        print(f"Converted {filename} to {webp_filename}")
                        break  
                    except PermissionError:
                        print(f"File {filename} is being used by another process. Retrying...")
                        time.sleep(1)  
                        processes = get_processes_using_file(filepath)
                        if processes:
                            print("Processes using the file:")
                            for pid, name in processes:
                                print(f"PID: {pid}, Name: {name}")
                else:
                    print(f"Failed to remove {filename} after multiple attempts.")


def main(directory):
    find_duplicates(directory)
    convert_to_webp(directory)

if __name__ == "__main__":
    directory = input("Enter the directory path:")
    main(directory)
