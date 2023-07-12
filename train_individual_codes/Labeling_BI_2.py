import re

file_path = "Tibetan_language_train_segmented.txt"  # Replace with the actual file path


modified_content=''

with open(file_path, 'r', encoding='utf-8') as file:
    # Read the file content
    file_content = file.read()

    words_list = file_content.split()
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
        
             
        modified_content = modified_content+temp_content
        
        #Searching for /IS tag
         # Define a dictionary with replacements
        replacements = {
            '-(.{1,2}(་|༌)/)(I|B)(?=\s)': r'\1IS'#For IS tags
        }
        for pattern, replacement in replacements.items():
            modified_content = re.sub(pattern, replacement, modified_content)


        # Use regex and re.sub() to perform replacements
        #modified_content = re.sub('|'.join(re.escape(key) for key in replacements.keys()), lambda match: replacements[match.group(0)], modified_content)
        


# Open the output file in write mode and write the modified content
with open('Tibetan_language_train_BI_tag_labelled.txt', 'w', encoding='utf-8') as output_file:
      output_file.write(modified_content)