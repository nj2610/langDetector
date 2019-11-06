from langDetector.detect import langDetector
code = '''Put your source code here.'''
lang = langDetector.detect(code)
print("Detected language is: ", lang)
