import os

DATA_PATH = os.path.join("data", "raw")

def check_data_folder():
    if os.path.exists(DATA_PATH):
        print(f"Data folder found at: {DATA_PATH}")
    else:
        print("Data folder not found!")

if __name__ == "__main__":
    check_data_folder()
