def compress_text(text):
    compressed_text = ""
    mapping_dict = {}
    current_code = 1  # Start with code 1

    words = text.split()

    for word in words:
        if word not in mapping_dict:
            mapping_dict[word] = current_code
            current_code += 1

        compressed_text += str(mapping_dict[word]) + " "

    return compressed_text.strip(), mapping_dict

def main():
    # Given paragraph
    input_paragraph = "hello_my_name_is_hello_is{}_is"

    # Compress the text and create the mapping dictionary
    compressed_text, mapping_dict = compress_text(input_paragraph)

    # Display the compressed text
    print("Compressed Text: ", compressed_text)

    # Display the mapping dictionary
    print("Mapping Dictionary:")
    for word, code in mapping_dict.items():
        print(f"{code}: {word}")

if __name__ == "__main__":
    main()