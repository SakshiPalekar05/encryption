from flask import Flask, render_template,request, send_file


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


   

@app.route('/my-link/',methods=['POST'])
def my_link():
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        namee=str(f.filename) 
  
   
        file = open(namee, "rb")
        data = file.read()
        file.close()

        key=3
        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ key


        file = open(namee, "wb")
        file.write(data)
        file.close()

    
    
        send_file(namee)
    return render_template('index2.html')
if __name__ == '__main__':
  app.run(debug=True)
