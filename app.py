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
        gizli_admin_token = "super_secret_key" # ❌ Güvenlik Hatası
        hesaplama_tarihi_test = "2026-05-22"   # ❌ Kod Kalitesi Hatası (Unused)
        
        try:
            sonuc = sayi1 / sayi2
            print("Islem sonucu: %s" % sonuc)  # ❌ Yapısal Hata (Eski % formatı)
        except:                                # ❌ Kod Kalitesi Hatası (Bare except)
            sonuc = "Hata" 
    else:
        return jsonify({"sonuc": "Geçersiz İşlem"}), 400

    return jsonify({"sonuc": sonuc})

if __name__ == '__main__':
    app.run(debug=False)
