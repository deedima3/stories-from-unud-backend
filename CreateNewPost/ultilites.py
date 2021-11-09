from DATABASE.models import BlogMainDatabase

# FUNGSI-FUNGSI SISTEM MENU

# Hash Function
def hashfunction(word):
    temp = 0
    for i, j in zip(word, range(1, len(word)+1)):
        temp += ord(i) * j
        temp = temp % 300
    return temp   # Return Integer

# Collission
def cekLinearCollision(keyNumber):
    newIndex = keyNumber
    while True:
        try:
            BlogMainDatabase.objects.get(HashNumber=newIndex)
            newIndex += 1 # Terjadi Collision maka index naik/di-increment 1
        except:
            return newIndex # Jika Error berarti key tersebut tersedia dan return key (integer)

        if (newIndex == 300):
            newIndex = 0
        if (newIndex == keyNumber):
            return "Sudah Penuh" # return string bahwa data penuh

def cekSearchLinearCollision(keyword):
    keyNumber = hashfunction(keyword)
    newIndex = keyNumber
    while True:
        try:
            data = BlogMainDatabase.objects.get(HashNumber=newIndex)
            if(data.title == keyword):
                return data
            else:
                newIndex += 1  # Terjadi Collision maka index naik/di-increment 1
        except:
            return None # Jika Error berarti key tersebut tersedia dan return key (integer)

        if (newIndex == 300):
            newIndex = 0
        if (newIndex == keyNumber):
            return "Sudah Penuh" # re