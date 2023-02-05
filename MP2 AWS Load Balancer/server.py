from flask import Flask,  request
app = Flask(__name__)

seed = 0

@app.route('/',methods = ['POST', 'GET'])
def server():
    global seed
    if request.method == 'POST':
        seed = int(request.json['num'])
        return str(seed)
        
    else:
        return str(seed)
      
if __name__ == '__main__':
   app.run(debug=True, port=5000)