

# this is for batch prediction so that both transform and predict can done at a time
class NetworkModel:
    def __init__(self,preprocessor,model):
        self.preprocessor=preprocessor
        self.model=model
    
    def predict(self,df):
        tranform_data=self.preprocessor.transform(df)
        y_pred=self.model.predict(tranform_data)
        return y_pred

