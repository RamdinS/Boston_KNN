import config
import json
import pickle
import numpy as np

class HousePrice():
    def __init__(self,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
        self.CRIM=CRIM
        self.ZN=ZN
        self.INDUS=INDUS
        self.CHAS=CHAS
        self.NOX=NOX
        self.RM=RM
        self.AGE=AGE
        self.DIS=DIS
        self.RAD=RAD
        self.TAX=TAX
        self.PTRATIO=PTRATIO
        self.B=B
        self.LSTAT=LSTAT

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.SCALAR_FILE_PATH,'rb') as f:
            self.scalar = pickle.load(f)

        with open(config.ENCODER_FILE_PATH,'r') as f:
            self.encoder = json.load(f)

    def pred_price(self):
        self.load_model()
        self.test_arr = np.zeros(len(self.encoder['columns']))

        self.test_arr[0]=self.CRIM
        self.test_arr[1]=self.ZN
        self.test_arr[2]=self.INDUS
        self.test_arr[3]=self.CHAS
        self.test_arr[4]=self.NOX
        self.test_arr[5]=self.RM
        self.test_arr[6]=self.AGE
        self.test_arr[7]=self.DIS
        self.test_arr[8]=self.RAD
        self.test_arr[9]=self.TAX
        self.test_arr[10]=self.PTRATIO
        self.test_arr[11]=self.B
        self.test_arr[12]=self.LSTAT

        #scaling
        self.test_arr = self.scalar.transform([self.test_arr])

        #prediction
        self.price = self.model.predict(self.test_arr)[0]

        return self.price


