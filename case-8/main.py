# Project 08: Text Compression Using Character Runs
text = input("Enter text to compress: ")
compressed = ""

if len(text) == 0:
    print("Compressed text: (empty)")
else:
    current_character = text[0]
    count = 1

    for index in range(1, len(text)):
        if text[index] == current_character:
            count = count + 1
        else:
            compressed = compressed + current_character + str(count)
            current_character = text[index]
            count = 1

    # Add the final character run.
    compressed = compressed + current_character + str(count)

    print("Original text :", text)
    print("Compressed text:", compressed)
