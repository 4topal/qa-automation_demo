from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hesapla', methods=['POST'])
def hesapla():
    data = request.get_json()
    if not data:
        return jsonify({"sonuc": "Geçersiz İstek"}), 400

    try:
        sayi1 = float(data.get('sayi1', 0))
        sayi2 = float(data.get('sayi2', 0))
    except (ValueError, TypeError):
        return jsonify({"sonuc": "Sayı giriniz"}), 400

    islem = data.get('islem')
    sonuc = None

    if islem == 'topla':
        sonuc = sayi1 + sayi2
    elif islem == 'cikar':
        sonuc = sayi1 - sayi2
    elif islem == 'carp':
        sonuc = sayi1 * sayi2
    elif islem == 'bol':
        if sayi2 == 0:
            return jsonify({"sonuc": "Sıfıra bölme hatası"}), 400
        sonuc = sayi1 / sayi2
        print("merhaba")    
    else:
        return jsonify({"sonuc": "Geçersiz İşlem"}), 400
    

    return jsonify({"sonuc": sonuc})

if __name__ == '__main__':
    app.run(debug=False)
