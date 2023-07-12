import re

file_path = "Tibetan_language_train_BI_tag_labelled.txt"  # Replace with the actual file path


modified_content=''

with open(file_path, 'r', encoding='utf-8') as file:
    # Read the file content
    file_content = file.read()
    replacements = {
        '/IS': '/B',
        '/I': '/B'
    }

    # Use regex and re.sub() to perform replacements
    modified_content = re.sub('|'.join(re.escape(key) for key in replacements.keys()), lambda match: replacements[match.group(0)], file_content)


# Open the output file in write mode and write the modified content
with open('Tibetan_language_train_RAW.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(modified_content)
