from DATABASE.models import BlogMainDatabase, queueArticle

# FUNGSI-FUNGSI SISTEM MENU

# Hash Function
def hashfunction(word):
    temp = 0
    for i, j in zip(word, range(1, len(word)+1)):
        temp += ord(i) * j
        temp = temp % 300
    return temp   # Return Integer

# Collission
def cekLinearCollision(keyNumber, keyword):
    newIndex = keyNumber
    while True:
        cek = queueArticle.objects.filter(HashNumber=newIndex).exists()
        if (cek):
            data = queueArticle.objects.get(HashNumber=newIndex)
            newIndex += 1  # Terjadi Collision maka index naik/di-increment 1
        else:
            return newIndex  # Jika False berarti key tersebut tersedia dan return key (integer)

        if (newIndex == 300):
            newIndex = 0
        if (newIndex == keyNumber):
            return "Sudah Penuh" # return string bahwa data penuh

def cekSearchLinearCollision(keyword):
    keyNumber = hashfunction(keyword)
    newIndex = keyNumber
    while True:
        cek = BlogMainDatabase.objects.filter(HashNumber=newIndex, acceptByAdmin=True).exists()
        if (cek):
            data = BlogMainDatabase.objects.get(HashNumber=newIndex, acceptByAdmin=True)
            if (data.title == keyword):
                return data
            else:
                newIndex += 1  # Terjadi Collision maka index naik/di-increment 1
        else:
            return None  # Jika False maka ternyata data tidak ada

        if (newIndex == 300):
            newIndex = 0
        if (newIndex == keyNumber):
            return "Tidak ada" # jika Linear kembali lagi ke index awal, berarti data tidak ada