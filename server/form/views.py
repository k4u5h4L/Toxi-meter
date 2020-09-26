from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import scrape

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

        user = [request_body['user']]
        comments = scrape.scrape_comments(user[0])
        # print(f"comments: {comments}")
        sequences = tokenizer.texts_to_sequences(comments)
        padded = pad_sequences(sequences, maxlen=150,
                               padding='post', truncating='post')
        pred_temp = model.predict(padded)
        predictions = []
        for pred in pred_temp:
            predictions.append(np.round(pred[0]))

        result = {}

        result['route'] = 'api route POST'
        result['message'] = np.array(predictions, dtype=int).tolist()

        print(result)
        return HttpResponse(json.dumps(result))
    else:
        testArr = [1.0, 0.0, 1.0, 0.0]
        return HttpResponse(json.dumps({'message': 'api route GET', 'array': testArr}))
