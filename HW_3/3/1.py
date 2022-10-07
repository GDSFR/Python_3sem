import pandas as pd
from sklearn.feature_extraction import DictVectorizer
scale_mapper=[{"XS":1,"X":2,"XL":3,"XXL":4},{"X":1,"XXL":1,"XS":4},{"XS":2,"X":3,"XXL":3,"XL":1},{"XXL":3}]
dict_vectorizer=DictVectorizer(sparse=False)
foot_size=dict_vectorizer.fit_transform(scale_mapper)
print(foot_size)