class Rapat:
    def __init__(self, name, availability, unavailability, duration):
        self.name = name
        self.availability = availability
        self.unavailability = unavailability
        self.duration = duration
        self.estimate_of_complete = self.availability + self.duration

def schedule_rapats(rapats):
    # Inisialisasi daftar untuk menyimpan rapat yang telah dijadwalkan
    scheduled_rapats = []
    # Inisialisasi variabel untuk menyimpan waktu selesai terakhir dari rapat yang telah dijadwalkan
    max_complete = 0

    while rapats:
        # Temukan rapat dengan waktu selesai perkiraan terawal yang dapat diselesaikan sebelum menjadi tidak tersedia
        rapat = min((e for e in rapats if max(e.availability, max_complete) + e.duration <= e.unavailability),
                    key=lambda e: max(e.availability, max_complete) + e.duration, default=None)

        # Jika tidak ada rapat seperti itu ditemukan, hentikan loop
        if rapat is None:
            break

        # Perbarui waktu ketersediaan dan perkiraan selesai dari rapat
        rapat.availability = max(rapat.availability, max_complete)
        rapat.estimate_of_complete = rapat.availability + rapat.duration

        # Perbarui max_complete
        max_complete = rapat.estimate_of_complete

        # Jadwalkan rapat dan hapus dari daftar rapat
        scheduled_rapats.append(rapat)
        rapats.remove(rapat)

    return scheduled_rapats
