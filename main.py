meme_dict = {"CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu"}
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Kita belum memiliki kata ini... Tapi kita sedang mengusahakannya!")
