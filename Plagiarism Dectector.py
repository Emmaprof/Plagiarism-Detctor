from difflib import SequenceMatcher
from pydoc import plainpager

with open("C:/Users/hp/Desktop/python code/checking plagiarism1.txt") as file1, open("C:/Users/hp/Desktop/python code/checkingplagiarism2.txt") as file2:
    file1data = file1.read()
    file2data = file2.read()
    similarity = SequenceMatcher(None, file1data,file2data).ratio()
    print(f" The level of pliagiarism is {similarity*100}")