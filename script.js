// Munculkan notifikasi otomatis saat halaman selesai dimuat
window.addEventListener('DOMContentLoaded', () => {
    const toast = document.getElementById('welcome-toast');
    
    // Muncul setelah jeda 0.4 detik
    setTimeout(() => {
        toast.classList.add('show');
    }, 400);

    // Otomatis hilang setelah 5 detik
    setTimeout(() => {
        toast.classList.remove('show');
    }, 5400);
});

// Fungsi tombol close pada notifikasi
function tutupNotif() {
    const toast = document.getElementById('welcome-toast');
    toast.classList.remove('show');
}

// Fungsi filter kartu berdasarkan kelas (X, XI, XII)
function filterMapel(kelasDipilih, tombolAktif) {
    // Atur warna tombol yang sedang aktif
    const semuaTombol = document.querySelectorAll('.filter-btn');
    semuaTombol.forEach(btn => btn.classList.remove('active'));
    tombolAktif.classList.add('active');

    // Tampilkan/sembunyikan kartu mapel
    const semuaKartu = document.querySelectorAll('.card');
    semuaKartu.forEach(kartu => {
        const kelasKartu = kartu.getAttribute('data-kelas');
        
        if (kelasDipilih === 'semua' || kelasKartu.includes(kelasDipilih)) {
            kartu.style.display = 'flex';
        } else {
            kartu.style.display = 'none';
        }
    });
}
