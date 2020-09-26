from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from tensorflow.keras.models import load_model
import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model(
    '/home/k4u5h4l/mystuff/toxic-comments/toxicity_model.h5')

with open('/home/k4u5h4l/mystuff/toxic-comments/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def home(request):
    return HttpResponse(json.dumps({'message': 'Homepage', 'status': 200}))


@csrf_exempt
def api(request):
    # request_body = request.body.decode("utf-8")if request.method == 'POST':
    if request.method == 'POST':
        request_body = json.loads(request.body.decode("utf-8"))
        print(request_body)

        sentence = [request_body['review']]
        sequences = tokenizer.texts_to_sequences(sentence)
        padded = pad_sequences(sequences, maxlen=100,
                               padding='post', truncating='post')
        pred_temp = model.predict(padded)
        pred = np.round(pred_temp[0][0])
        print(pred)

        return HttpResponse(json.dumps({'route': 'api route POST', 'message': int(pred)}))
    else:
        return HttpResponse(json.dumps({'message': 'api route GET'}))
