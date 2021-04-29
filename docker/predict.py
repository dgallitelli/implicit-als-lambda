import os
import json
import pandas as pd
import pickle as pkl

# LOAD MODEL
model = pkl.load(open('model.sav', 'rb'))


def handler(event, context):
    data = event['body']
    # PREDICT
    prediction = model.similar_items(data, 11)
    return {
        'statusCode': 200,
        'body': str(prediction)
    }
