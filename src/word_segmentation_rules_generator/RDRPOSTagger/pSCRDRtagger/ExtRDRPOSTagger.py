import sys
from multiprocessing import Pool

from ..SCRDRlearner.Object import FWObject, getWordTag
from ..SCRDRlearner.SCRDRTree import SCRDRTree
from ..SCRDRlearner.SCRDRTreeLearner import SCRDRTreeLearner
from ..Utility.Config import NUMBER_OF_PROCESSES, THRESHOLD

# os.chdir("../")
# sys.setrecursionlimit(100000)
# sys.path.append(os.path.abspath(""))
# os.chdir("./pSCRDRtagger")


def unwrap_self_ExtRDRPOSTagger(arg, **kwarg):
    return ExtRDRPOSTagger.tagInitializedSentence(*arg, **kwarg)


class ExtRDRPOSTagger(SCRDRTree):
    def __init__(self):
        self.root = None

    def tagInitializedSentence(self, initSen):
        wordTags = (
            initSen.replace("“", "''").replace("”", "''").replace('"', "''").split()
        )
        sen = []
        for i in range(len(wordTags)):
            fwObject = FWObject.getFWObject(wordTags, i)
            word, tag = getWordTag(wordTags[i])
            node = self.findFiredNode(fwObject)
            if node.depth > 0:
                sen.append(word + "/" + node.conclusion)
            else:  # Fired at root, return initialized tag
                sen.append(word + "/" + tag)
        return " ".join(sen)

    def tagInitializedCorpus(self, inputFile):
        lines = open(inputFile, encoding="utf-8").readlines()
        # Change the value of NUMBER_OF_PROCESSES to obtain faster tagging process!
        pool = Pool(processes=NUMBER_OF_PROCESSES)
        taggedLines = pool.map(
            unwrap_self_ExtRDRPOSTagger, zip([self] * len(lines), lines)
        )
        out = open(inputFile + ".TAGGED", "w", encoding="utf-8")
        for line in taggedLines:
            out.write(line + "\n")
        out.close()
        print("\nOutput file: " + inputFile + ".TAGGED")


def printHelp():
    print("\n===== Usage =====")
    print(
        "\n#1: To train RDRPOSTagger in case of using output from an external initial POS tagger:"
    )
    print(
        "\npython ExtRDRPOSTagger.py train GOLD-STANDARD-TRAINING-CORPUS TRAINING-CORPUS-INITIALIZED-BY-EXTERNAL-TAGGER"
    )
    print(
        "\nExample: python ExtRDRPOSTagger.py train ../data/goldTrain ../data/initTrain"
    )
    print(
        "\n#2: To use the trained model for POS tagging on a test corpus tagged by the external initial tagger:"
    )
    print(
        "\npython ExtRDRPOSTagger.py tag PATH-TO-TRAINED-MODEL PATH-TO-TEST-CORPUS-INITIALIZED-BY-EXTERNAL-TAGGER"
    )
    print(
        "\nExample: python ExtRDRPOSTagger.py tag ../data/initTrain.RDR ../data/initTest"
    )
    print("\n#3: Find the full usage at http://rdrpostagger.sourceforge.net !")


# def run(args=sys.argv[1:]):
def run(system_arguments):
    args =  system_arguments[1:]
    if len(args) == 0:
        printHelp()
    elif args[0].lower() == "train":
        try:
            # print("\n===== Start =====")
            # print(
            #     "\nLearn a tree model of rules for POS tagging from {} and {} ".format(
            #         args[1], args[2]
            #     )
            # )
            THRESHOLD = args[3]
            rdrTree = SCRDRTreeLearner(THRESHOLD[0], THRESHOLD[1])
            rdrTree.learnRDRTree(args[2], args[1])
            print("\nWrite the learned tree model to file " + args[2] + ".RDR")
            rdrTree.writeToFile(args[2] + ".RDR")
            print("\nDone!")
        except Exception as e:
            print("\nERROR ==> ", e)
            printHelp()
    elif args[0].lower() == "tag":
        try:
            r = ExtRDRPOSTagger()
            print("\n=> Read a POS tagging model from " + args[1])
            r.constructSCRDRtreeFromRDRfile(args[1])
            print("\n=> Perform POS tagging on " + args[2])
            r.tagInitializedCorpus(args[2])
        except Exception as e:
            print("\nERROR ==> ", e)
            printHelp()
    else:
        printHelp()


if __name__ == "__main__":
    # run()
    pass 
