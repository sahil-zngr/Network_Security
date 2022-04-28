from flask import Flask, request, render_template

from elgamal import ElGamal

app = Flask(__name__)

# flask home function
@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    enc_text = None
    dec_text = None
    print(request.form)
    if request.method == 'POST':
        print(request.form)
        pk = int(request.form.get('pk'))
        if pk == None:
            print("here")
            return
        EG = ElGamal(pk)
        if request.form.get('encpt')!= None:
            enc_text = int(request.form['encpt'])
            print(enc_text)
            dec_text = EG.Encrypt(enc_text)
            dec_text = str(dec_text[0]) + "," + str(dec_text[1])
            print(dec_text)
            return render_template('index.html', encpt = enc_text, encct = dec_text, pk = pk)
        
        elif request.form.get('decct') != None:
            dec_text = request.form['decct']
            dec_text = dec_text.split(',')
            C1 = int(dec_text[0])
            C2 = int(dec_text[1])
            enc_text = EG.Decrypt(C1, C2)
        return render_template('index.html', decpt = enc_text, decct = dec_text, pk = pk)


if __name__=='__main__':
    app.run()
