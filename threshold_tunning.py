import time
import os
import sys

from src.word_segmentation_rules_generator.train_tag_rdr.train_tag_rdr import tag_rdr, train_rdr
from src.word_segmentation_rules_generator.eval_rdr_result.eval_rdr_result import eval_rdr_result



def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        line_count = len(lines)
    
    return line_count

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
    
    return word_count

THREHOLD_LIST = [(50,20),(10,10),(5,5),(3,2),(1,1)]
FILE_TO_TRAIN = 'TIB_train_maxmatched_tagged.txt'

current_dir = os.path.dirname(__file__)
relative_path = "src/word_segmentation_rules_generator/data/" + FILE_TO_TRAIN
file_path = os.path.join(current_dir, relative_path)

print('Number of words in Training File: ', count_words(file_path))

for threshold in THREHOLD_LIST:
        
    # Redirect the standard output to the null device
    sys.stdout = open(os.devnull, 'w')

    begin = time.time()
    train_rdr(FILE_TO_TRAIN, threshold)
    end = time.time()
    print(f"Total runtime of the program is {end - begin}")
    
    #Tagging the training file and finding the accuracy
    tag_rdr()
    training_accuracy = eval_rdr_result()

    #Tagging the testing file and finding the accuracy
    tag_rdr('TIB_test_maxmatched.txt')
    testing_accuracy = eval_rdr_result('TIB_test_maxmatched_tagged.txt', 'TIB_test_maxmatched.txt.TAGGED')

    # After your code is executed, restore the standard output
    sys.stdout = sys.__stdout__

    #Finding number of rules 
    rdr_file_path = 'TIB_train_maxmatched_tagged.txt.RDR'
    current_dir = os.path.dirname(__file__)
    relative_path = "src/word_segmentation_rules_generator/data/" + rdr_file_path
    file_path = os.path.join(current_dir, relative_path)
    lines_count = count_lines(file_path)

    #Printing the values
    print("Threshold Value: >", threshold)
    print(f"Total runtime of the program is {end - begin}")
    print('Number of lines', lines_count)
    print("Training accuracy Value:> ",training_accuracy)
    print("Testing accuracy Value:> ",testing_accuracy)


