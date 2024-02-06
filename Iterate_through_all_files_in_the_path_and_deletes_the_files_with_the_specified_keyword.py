
import os

def remove_copied_files(path):
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return

    # Iterate through all files in the path
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            if "- Copy" in file:
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")

if __name__ == "__main__":
    path = input("Enter the path: ")
    remove_copied_files(path)
    
