import struct
import pyperclip  # You need to: pip install pyperclip

def main():
    file_path = input("file") 
    
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return

    # Extract Header Info
    pixel_offset = struct.unpack('<I', data[10:14])[0]
    width = struct.unpack('<i', data[18:22])[0]
    height = struct.unpack('<i', data[22:26])[0]

    row_size = ((width * 3 + 3) // 4) * 4
    chars = "█▓▒░ " 
    num_chars = len(chars)

    # This list will hold every line of our art
    output_lines = []

    for y in range(height - 1, -1, -1):
        row_start = pixel_offset + (y * row_size)
        line = ""
        for x in range(0, width * 3, 3):
            b = data[row_start + x]
            g = data[row_start + x + 1]
            r = data[row_start + x + 2]

            avg = (r + g + b) // 3
            char_index = (avg * (num_chars - 1)) // 255
            
            line += chars[char_index] * 2
        
        output_lines.append(line)

    # Join everything with newlines into one giant string
    final_output = "\n".join(output_lines)

    # 1. Print to terminal so you can see it
    print(final_output)

    # 2. SEND TO CLIPBOARD
    pyperclip.copy(final_output)
    print("\n--- Success! The pixel art is now in your clipboard. ---")

if __name__ == "__main__":
    main()
