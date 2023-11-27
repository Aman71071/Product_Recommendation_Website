from flask import Flask, request, url_for, redirect, render_template
import engine


app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

obj = engine.Engine()

@app.route('/')
@app.route('/home')
def gotohome():
    return render_template('index.html')

@app.route('/recomm')
def gotorecomm():
    global obj
    prolist = obj.product_names
    return render_template('recomm.html', prod = prolist)

@app.route('/receng', methods=['GET', 'POST'])
def recengine():
    global obj
    prolist = obj.product_names
    if request.method == 'POST':
        selected_option = request.form['product']
        if selected_option == '':
            return render_template('recomm.html', prod = prolist, scroll = 'result')
        else:
            recprod = obj.recommend(selected_option)
            return render_template('recomm.html', scroll = 'result', prod = prolist, recpro = recprod)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
