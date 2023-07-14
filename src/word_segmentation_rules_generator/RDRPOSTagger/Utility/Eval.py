import re
import sys

from .Utils import getWordTag, readDictionary

# os.chdir("../")
# sys.setrecursionlimit(100000)
# sys.path.append(os.path.abspath(""))
# os.chdir("./Utility")

def computeAccuracy_and_return_wrong_tagged_results(goldStandardCorpus, taggedCorpus):
    tagged = open(taggedCorpus, encoding="utf-8").read().split()
    goldStandard = open(goldStandardCorpus, encoding="utf-8").read().split()
    if len(tagged) != len(goldStandard):
        print(
            "The numbers of word tokens in {} and {} are not equal!".format(
                goldStandardCorpus, taggedCorpus
            )
        )
        return 0
    numwords = 0
    count = 0
    wrong_tagged_wordtag = ''
    for i in range(len(tagged)):
        numwords += 1
        word1, tag1 = getWordTag(tagged[i])
        word2, tag2 = getWordTag(goldStandard[i])
        pattern = r"[་]+"
        word1 = re.sub(pattern, "་", word1)
        word2 = re.sub(pattern, "་", word2)
        if word1 != word2 and word1 != "''" and word2 != "''":
            print(
                "Words are not the same in gold standard and tagged corpora, at the index",
                i,
            )
            return 0

        if tag1.lower() == tag2.lower():
            count += 1
        else:
            wrong_tagged_wordtag += goldStandard[i]+'  '+tagged[i]+'\n'

    return wrong_tagged_wordtag, count * 100.0 / numwords


    
def computeAccuracy(goldStandardCorpus, taggedCorpus):
    tagged = open(taggedCorpus, encoding="utf-8").read().split()
    goldStandard = open(goldStandardCorpus, encoding="utf-8").read().split()
    if len(tagged) != len(goldStandard):
        print(
            "The numbers of word tokens in {} and {} are not equal!".format(
                goldStandardCorpus, taggedCorpus
            )
        )
        return 0
    numwords = 0
    count = 0
    for i in range(len(tagged)):
        numwords += 1
        word1, tag1 = getWordTag(tagged[i])
        word2, tag2 = getWordTag(goldStandard[i])
        pattern = r"[་]+"
        word1 = re.sub(pattern, "་", word1)
        word2 = re.sub(pattern, "་", word2)
        if word1 != word2 and word1 != "''" and word2 != "''":
            print(
                "Words are not the same in gold standard and tagged corpora, at the index",
                i,
            )
            return 0

        if tag1.lower() == tag2.lower():
            count += 1

    return count * 100.0 / numwords


def computeAccuracies(fullDictFile, goldStandardCorpus, taggedCorpus):
    """
    Return known-word accuracy, unknown-word accuracy and the overall accuracy
    """
    tagged = open(taggedCorpus, encoding="utf-8").read().split()
    goldStandard = open(goldStandardCorpus, encoding="utf-8").read().split()
    if len(tagged) != len(goldStandard):
        print(
            "The numbers of word tokens in {} and {} are not equal!".format(
                goldStandardCorpus, taggedCorpus
            )
        )
        return 0

    fullDICT = readDictionary(fullDictFile)

    numwords = count = 0
    countKN = countUNKN = 0
    countCorrectKN = countCorrectUNKN = 0

    for i in range(len(tagged)):
        numwords += 1
        word1, tag1 = getWordTag(tagged[i])
        word2, tag2 = getWordTag(goldStandard[i])
        pattern = r"[་]+"
        word1 = re.sub(pattern, "་", word1)
        word2 = re.sub(pattern, "་", word2)
        if word1 != word2 and word1 != "''" and word2 != "''":
            print(
                "Words are not the same in gold standard and tagged corpora, at the index "
                + str(i)
            )
            return 0

        if tag1.lower() == tag2.lower():
            count += 1

        if word1 in fullDICT:
            countKN += 1
            if tag1.lower() == tag2.lower():
                countCorrectKN += 1
        else:
            countUNKN += 1
            if tag1.lower() == tag2.lower():
                countCorrectUNKN += 1

    if countUNKN == 0:
        return countCorrectKN * 100.0 / countKN, 0.0, count * 100.0 / numwords
    else:
        return (
            countCorrectKN * 100.0 / countKN,
            countCorrectUNKN * 100.0 / countUNKN,
            count * 100.0 / numwords,
        )


if __name__ == "__main__":
    print(str(computeAccuracy(sys.argv[1], sys.argv[2])) + "%")
    pass
