import pickle
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import pkg_resources
import warnings
warnings.filterwarnings("ignore")


resource_package = __name__
modelFilePath = pkg_resources.resource_filename(resource_package, 'data/langDetectAllNew.sav')
featureFilePath = pkg_resources.resource_filename(resource_package, 'data/featureAllNew.pkl')

loaded_model = pickle.load(open(modelFilePath, 'rb'))

count_vect = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open(featureFilePath, "rb")))

class langDetector:
    @staticmethod
    def detect(code):
        return loaded_model.predict(count_vect.transform([code]))
