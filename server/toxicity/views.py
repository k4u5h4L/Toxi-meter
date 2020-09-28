from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from tensorflow.keras.models import load_model
import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

import os
import json

from .scrape import Scrape

model = load_model(
    os.getcwd() + '/toxicity_model.h5')

with open(os.getcwd() + '/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


class ViewApi(APIView):
    route = "api route POST"
    predictions = []
    comments = []
    links = []
    status = ""

    def get(self, request):
        print(request.query_params)
        return Response({'message': 'api route GET'})

    def post(self, request):
        # print(request.data)
        user = str(request.data['user'])

        (comments, links) = Scrape(user)

        if comments == 0 or links == 0:
            print(f"User \tu/{user}\t not found!")
            return Response({'status': 'error'})
        else:
            # print(f"comments: {comments}")
            print(f"User \tu/{user}\t found!")
            sequences = tokenizer.texts_to_sequences(comments)
            padded = pad_sequences(sequences, maxlen=150,
                                   padding='post', truncating='post')
            pred_temp = model.predict(padded)
            predictions = []
            for pred in pred_temp:
                predictions.append(np.round(pred[0]))

            result = {}

            result['route'] = 'api route POST'
            result['predictions'] = np.array(predictions, dtype=int).tolist()
            result['comments'] = comments
            result['links'] = links
            result['status'] = 'success'

            # print(result)

            return Response(json.dumps(result))
