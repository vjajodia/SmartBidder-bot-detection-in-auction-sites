import numpy as np
import pickle

def predict_human(record: list):
    unit=np.array(list(record))
    unit=unit.reshape(1,-1)

    model=pickle.load(open('model_rf.pkl', 'rb'))
    predictions=model.predict(unit)

    print(predictions)

    return 1

