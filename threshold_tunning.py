import time
import os
import sys

from src.word_segmentation_rules_generator.train_tag_rdr.train_tag_rdr import tag_rdr, train_rdr
from src.word_segmentation_rules_generator.eval_rdr_result.eval_rdr_result import eval_rdr_result



def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
    
    return line_count


# Redirect the standard output to the null device
sys.stdout = open(os.devnull, 'w')

FILE_TO_TRAIN = 'TIB_train_maxmatched_tagged.txt'
threshold=(10,10)
begin = time.time()
train_rdr(FILE_TO_TRAIN, threshold)
end = time.time()
print(f"Total runtime of the program is {end - begin}")
tag_rdr()
training_accuracy = eval_rdr_result()

tag_rdr('TIB_test_maxmatched.txt')
testing_accuracy = eval_rdr_result('TIB_test_maxmatched_tagged.txt', 'TIB_test_maxmatched.txt.TAGGED')

# After your code is executed, restore the standard output
sys.stdout = sys.__stdout__


rdr_file_path = 'TIB_train_maxmatched_tagged.txt.RDR'
current_dir = os.path.dirname(__file__)
relative_path = "src/word_segmentation_rules_generator/data/" + rdr_file_path
file_path = os.path.join(current_dir, relative_path)
lines_count = count_lines(file_path)



print("Threshold Value: >", threshold)
print(f"Total runtime of the program is {end - begin}")
print('Number of lines', lines_count)
print("Training accuracy Value:> ",training_accuracy)
print("Testing accuracy Value:> ",testing_accuracy)


