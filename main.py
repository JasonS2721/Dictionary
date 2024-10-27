meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "WEIRDO": "ejekan",
            "GOOFY": "Bodoh"
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("Makna kata",word,"adalah",meme_dict[word])
else:
    print('kata tidak ditemukan')
