import time
from src.word_segmentation_rules_generator.train_tag_rdr.train_tag_rdr import tag_rdr, train_rdr




FILE_TO_TRAIN = 'TIB_train_maxmatched_tagged.txt'
threshold=(3,2)
begin = time.time()
train_rdr(FILE_TO_TRAIN, threshold)
end = time.time()
print(f"Total runtime of the program is {end - begin}")
tag_rdr()

