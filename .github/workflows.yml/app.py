from flask import Flask, render_template

app = Flask("DKVee")

# DATA MATA PELAJARAN DKV
# Kamu bisa dengan mudah menambah, mengubah, atau menghapus mapel di bagian ini!
daftar_mapel = [
    {
        "nama": "Dasar-Dasar Desain Grafis",
        "kelas": "Kelas X",
        "ikon": "🎨",
        "deskripsi": "Mempelajari unsur tata letak, prinsip desain, teori warna, dan tipografi dasar.",
        "software": "CorelDRAW, Adobe Illustrator"
    },
    {
        "nama": "Fotografi & Videografi",
        "kelas": "Kelas XI",
        "ikon": "📸",
        "deskripsi": "Teknik pengambilan gambar, pengaturan kamera (segitiga exposure), pencahayaan, dan editing.",
        "software": "Adobe Lightroom, Premiere Pro"
    },
    {
        "nama": "Desain Publikasi & Percetakan",
        "kelas": "Kelas XI",
        "ikon": "📰",
        "deskripsi": "Merancang layout majalah, poster, kemasan (packaging), dan persiapan pra-cetak.",
        "software": "Adobe InDesign, Illustrator"
    },
    {
        "nama": "Komputer Grafis & Digital Imaging",
        "kelas": "Kelas XI",
        "ikon": "✨",
        "deskripsi": "Manipulasi foto, ilustrasi digital, dan pembuatan aset visual berbasis vektor maupun bitmap.",
        "software": "Adobe Photoshop, Illustrator"
    },
    {
        "nama": "Desain Media Interaktif (UI/UX)",
        "kelas": "Kelas XII",
        "ikon": "💻",
        "deskripsi": "Merancang tampilan antarmuka aplikasi/web yang estetik dan ramah pengguna.",
        "software": "Figma, Adobe XD"
    },
    {
        "nama": "Produk Kreatif & Kewirausahaan",
        "kelas": "Kelas XI & XII",
        "ikon": "🛍️",
        "deskripsi": "Membangun brand sendiri, menghitung HPP desain, dan memasarkan karya kreatif.",
        "software": "Canva, Sosial Media, Marketplace"
    }
]

@app.route('/')
def home():
    # Mengirim data 'daftar_mapel' ke halaman index.html
    return render_template('index.html', mapel_list=daftar_mapel)

if __name__ == '__main__':
    app.run(debug=True)
