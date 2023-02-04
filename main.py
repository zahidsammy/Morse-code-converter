import tkinter as tk

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def text_to_morse(text):
    # Convert the text to upper case
    text = text.upper()
    # Split the text into words and convert each word to Morse code
    words = text.split()
    morse_words = [
        ' '.join([morse_code[char] for char in word])
        for word in words
    ]
    # Join the Morse code words into a single string
    morse_text = '   '.join(morse_words)
    return morse_text

def convert():
    input_text = input_entry.get()
    output_text = text_to_morse(input_text)
    output_label.config(text=output_text)

root = tk.Tk()
root.title("Morse Code Converter")

input_label = tk.Label(root, text="Input text:")
input_label.grid(row=0, column=0)

input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

output_label = tk.Label(root, text="")
output_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()



