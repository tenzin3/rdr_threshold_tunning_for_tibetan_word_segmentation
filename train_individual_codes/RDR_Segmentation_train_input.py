import re


# Open the file in read mode
file_path = "Tibetan_language_train.txt"  # Replace with the actual file path
with open(file_path, 'r', encoding='utf-8') as file:
    # Read the file content
    file_content = file.read()
    
    intial_patterns = {
        #  '(་|༌)':r'\1 ', #Full stop (2 different kind)
          '\?':' ',
          '\+':' ',
          '([^༅])།':r'\1 །', 
          '།\s*།':'།_། ',
          '([^_༅])། ': r'\1 །_ ',# དུ། -> དུ །_ 
          ' །([^_])': r' །_ \1', # །བསྲེགས ->  །_ བསྲེགས་
          '([^།་༌_ ]) ': r'\1་ ',  # Putting full stop དུ། -> དུ་ །_
          
    }

    modified_content = file_content
    for pattern, replacement in intial_patterns.items():
        modified_content = re.sub(pattern, replacement, modified_content)


    pattern = r"[ ]+"
    replacement = ' '
    modified_content = re.sub(pattern, replacement, modified_content)

# Open the output file in write mode and write the modified content
with open('Tibetan_language_train_segmented.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(modified_content)