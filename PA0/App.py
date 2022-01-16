from flask import Flask, request, render_template

app = Flask(__name__)

#function to encrypt and decrypt
#both encrypt and decrypt equation is same
# C = E(p) = 27 - p, here c = ciphertext, p = letter/charcter, here a is 1 and z is 26
def encdec(text):
    ans = ""
    for c in text:
        if c >= 'a' and c <= 'z':
            #for lower case letters
            ans += chr( ord('a') + ord('z') - ord(c) )
        elif c >='A' and c <='Z':
            # for upper case letters
            ans += chr( ord('A') + ord('Z') - ord(c) )
        else:
            # for any other charaters
            ans += c
    return ans

# flask home function
@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    enc_text = None
    dec_text = None

    if request.method == 'POST':
        if request.form.get('enc')!= None:
            enc_text = request.form['enc']
            print(enc_text)
            dec_text = encdec(enc_text)
            print(dec_text)
        elif request.form.get('dec') != None:
            dec_text = request.form['dec']
            enc_text = encdec(dec_text)
        return render_template('index.html', enc = enc_text, dec = dec_text)


if __name__=='__main__':
    app.run()
