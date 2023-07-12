import re
import sys

# Open the file in read mode

# Check if the correct number of arguments is provided
if len(sys.argv) < 2:
    print("Usage: python script.py input_file")
    sys.exit(1)

input_file_path = sys.argv[1]

user_input = input("Enter name for your output file: ")
output_file_path = user_input+".txt"

with open(input_file_path, 'r', encoding='utf-8') as file:
    # Read the file content
    file_content = file.read()
    
    intial_patterns = {
          '\?':' ',
          '\+':' ',
           '-':'',
          '(་|༌)':r'\1 ', #Full stop (2 different kind)
          '([^༅])།':r'\1 །', 
          '།\s*།':'།_། ',
          '([^_༅])། ': r'\1 །_ ',# དུ། -> དུ །_ 
          ' །([^_])': r' །_ \1', # །བསྲེགས ->  །_ བསྲེགས་
          '([^།་༌_ ]) ': r'\1་ '  # Putting full stop དུ། -> དུ་ །_
    
    }

    modified_content = file_content
    for pattern, replacement in intial_patterns.items():
        modified_content = re.sub(pattern, replacement, modified_content)


    pattern = r"[ ]+"
    replacement = ' '
    modified_content = re.sub(pattern, replacement, modified_content)

# Open the output file in write mode and write the modified content
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(modified_content)

print(output_file_path+" created successfully...")