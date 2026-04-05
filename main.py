import sys
import os

def main():
    
    
    if len(sys.argv) < 2:
        print("Usage: python art.py <path_to_bmp>")
        return

    file_path = sys.argv[1]

    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    if not file_path.lower().endswith('.bmp'):
        print("Error: Please provide a .bmp file.")
        return

    print(f"Opening: {file_path}...")
    
    
    with open(file_path, 'rb') as f:
        data = f.read()
        print(f"Read {len(data)} bytes of binary data.")
        

if __name__ == "__main__":
    main()
