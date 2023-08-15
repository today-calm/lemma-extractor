import os
import spacy
from const import articlePathList, wordPath

outputDir = './output'

nlp = spacy.load('en_core_web_sm')

def read(path):
  with open (path, 'r') as f:
    text = f.read()
  return text

def getLemmaDict(text):
  lemmaDict = {}
  doc = nlp(text)
  for token in doc:
    lemma = token.lemma_
    lemmaDict[lemma] = lemmaDict.get(lemma, 0) + 1
  return lemmaDict

# 获取 dict 中 key 在 list 中的所有键值对
def getSubDict(dt, ls):
  # 以下代码使用GPT 生成
  subDict = {key: dt[key] for key in ls if key in dt}
  return subDict

# 将 dict 按值降序排序，返回 list
def descend(dt):
  # 以下代码使用GPT 生成
  sortedList = sorted(dt.items(), key=lambda x: x[1], reverse=True)
  return sortedList

def output(wordList, articlePath, outputDir):
  articleLemmaDict = getLemmaDict(read(articlePath))
  subDict = getSubDict(articleLemmaDict, wordList)
  resultList = descend(subDict)
  resultStr = '\n'.join([f'{value} {key}' for key, value in resultList])

  baseName = os.path.basename(articlePath)
  fileName = os.path.join(outputDir, baseName)
  with open(fileName, 'w') as file:
    file.write(resultStr)

wordList = read(wordPath).split('\n')

for articlePath in articlePathList:
  output(wordList, articlePath, outputDir)
