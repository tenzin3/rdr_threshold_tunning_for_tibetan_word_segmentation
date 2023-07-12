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


modified_content=''

with open(input_file_path, 'r', encoding='utf-8') as file:
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
    
    #making sure there only one space
    pattern = r"[ ]+"
    replacement = ' '
    modified_content = re.sub(pattern, replacement, modified_content)


    #Labelling starts
    words_list = modified_content.split()
    Labelled_content = ''
    for words in words_list:
        
        
        #0 means B tag,1 means I tag
        tag=0
        
        last_char=0
        if words[len(words)-1]!='་' and words[len(words)-1]!='༌':
            last_char=1
        temp_content=''
        for word in words:
            temp_content+=word
            if word=='་' or word == '༌':
                if tag ==0:
                    temp_content+='/B '
                    tag=1
                else:
                    temp_content+='/I '
        if last_char==1:
            if tag==0:
                temp_content+='/B '
            else:
                temp_content+='/I '
        
             
        Labelled_content = Labelled_content+temp_content
        
        #Searching for /IS tag
        replacements = {
            '-(.{1,2}(་|༌)/)(I|B)(?=\s)': r'\1\3S'#For IS tags
        }
        for pattern, replacement in replacements.items():
            Labelled_content = re.sub(pattern, replacement, Labelled_content)


    # Open the output file in write mode and write the modified content
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(Labelled_content)

    print(output_file_path+" created successfully...")