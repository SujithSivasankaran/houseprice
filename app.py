from flask import Flask,render_template,request
import requests,json,urllib
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/', methods=['POST','GET'])
def predict():
    features_names = [x for x in request.form.keys()]
    features = [x for x in request.form.values()]
    n = {}
    for i in range(0, len(features_names)):
        n[features_names[i]] = (features[i])
    l = [n]
    data = {'Inputs': {"WebServiceInput0": l}}
    body = str.encode(json.dumps(data))
    url = 'http://d7977875-b663-4cfe-aeaf-5405e4b37640.centralus.azurecontainer.io/score'
    api_key = 'K1jnb1ejnd0cWWXqG4rjRbwwFkvfMmvZ' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers)
    response = urllib.request.urlopen(req)
    result = response.read()
    data = int(json.loads(result)['Results']['WebServiceOutput0'][0]['Scored Labels'])
    return render_template('index.html', output= data)
# if __name__ == "__main__":
#     app.run()
