class data_prep():
    def __init__(self, url, target):

        #import packages
        import pandas as pd
        import numpy as np
        from sklearn.model_selection import train_test_split
        
        #load and separate data
        self.data=pd.read_csv(f'{url}')
        self.target=self.data[f'{target}']
        self.input=pd.read_csv(f'{url}').drop(f'{target}', axis=1)

        #divide into train/test
        self.X_train, self.X_test, self.y_train, self.y_test=train_test_split(self.input, self.target)