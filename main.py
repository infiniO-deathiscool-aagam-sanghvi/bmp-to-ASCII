import struct

def main():
    file_path = input("Enter filename: ")+".bmp"
    scale_factor = 3  # Adjust this to fit your screen!
    
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return

    # Header extraction
    pixel_offset = struct.unpack('<I', data[10:14])[0]
    width = struct.unpack('<i', data[18:22])[0]
    height = struct.unpack('<i', data[22:26])[0]
    row_size = ((width * 3 + 3) // 4) * 4
    
    chars = "█▓▒░ " 
    num_chars = len(chars)
    output_lines = []

    for y in range(height - 1, -1, -scale_factor):
        row_start = pixel_offset + (y * row_size)
        line = ""
        for x in range(0, width * 3, scale_factor * 3):
            b = data[row_start + x]
            g = data[row_start + x + 1]
            r = data[row_start + x + 2]

            avg = (r + g + b) // 3
            char_index = (avg * (num_chars - 1)) // 255
            line += chars[char_index] * 2
        
        output_lines.append(line)

    final_output = "\n".join(output_lines)

    # 1. Still print it to the terminal
    print(final_output)

    # 2. SAVE TO FILE (Instead of pyperclip)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(final_output)
    
    print("\n--- Success! Art saved to 'output.txt' ---")
    print("Open 'output.txt' in the sidebar to copy it!")

if __name__ == "__main__":
    main()