__author__ = 'Rene'

from piece import piece
from PIL import Image
from Collection import Collection


PATH = "/Document/msia/16 Winter/Java:python/nyfw/"

# DNKY
def DNKY():
    DNKY_PATH = "./DNKY/dnky"
    JPG = ".jpg"
    DNKY = Collection()
    dnky = [piece(Image.open(DNKY_PATH + str(i) + JPG)) for i in range(1, 13)]
    DNKY.add(dnky)
    dnky_collection = DNKY.getMergePieces()
    dnky_collection.show()
    dnky_collection.save("./DNKY.jpg")
    dnky_avg = DNKY.getMergeAvgPieces()
    dnky_avg.show()
    dnky_avg.save("./DNKYavg.jpg")
    dnky_frequent = DNKY.getMergeFrequentPieces()
    dnky_frequent.show()
    dnky_frequent.save("./DNKYfrequent.jpg")
    dnky_kmeans = DNKY.getKmeansPieces()
    dnky_kmeans.show()
    #dnky_kmeans.save("./DNKYkmeans.jpg")

# CK
def CK():
    CK_PATH = "./CK/ck"
    JPG = ".jpg"
    CK = Collection()
    ck = [piece(Image.open(CK_PATH + str(i) + JPG)) for i in range(1, 13)]
    CK.add(ck)
    ck_collection = CK.getMergePieces()
    ck_collection.show()
    ck_collection.save(CK_PATH + JPG)
    #dnky_avg = DNKY.getMergeAvgPieces()
   # dnky_avg.show()
   # dnky_frequent = DNKY.getMergeFrequentPieces()
   # dnky_frequent.show()
    ck_kmeans = CK.getKmeansPieces()
    ck_kmeans.show()
    ck_kmeans.save(CK_PATH + "kmeans" + JPG)

# AnnaSui
def ANNA():
    ANNA_PATH = "./AnnaSui/anna"
    JPG = ".jpg"
    ANNA = Collection()
    anna = [piece(Image.open(ANNA_PATH + str(i) + JPG)) for i in range(1, 13)]
    ANNA.add(anna)
    anna_collection = ANNA.getMergePieces()
    anna_collection.show()
    anna_collection.save(ANNA_PATH + JPG)
    anna_kmeans = ANNA.getKmeansPieces()
    anna_kmeans.show()
    anna_kmeans.save(ANNA_PATH + "kmeans" + JPG)

# Coach
def COACH():
    COACH_PATH = "./Coach/coach"
    JPG = ".jpg"
    COACH = Collection()
    coach = [piece(Image.open(COACH_PATH + str(i) + JPG)) for i in range(1, 13)]
    COACH.add(coach)
    coach_collection = COACH.getMergePieces()
    coach_collection.show()
    coach_collection.save(COACH_PATH + JPG)
    coach_kmeans = COACH.getKmeansPieces()
    coach_kmeans.show()
    coach_kmeans.save(COACH_PATH + "kmeans" + JPG)

# Delpozo
def DELPOZO():
    DELPOZO_PATH = "./Delpozo/delpozo"
    JPG = ".jpg"
    DELPOZO = Collection()
    delpozo = [piece(Image.open(DELPOZO_PATH + str(i) + JPG)) for i in range(1, 13)]
    DELPOZO.add(delpozo)
    delpozo_collection = DELPOZO.getMergePieces()
    delpozo_collection.show()
    delpozo_collection.save(DELPOZO_PATH + JPG)
    delpozo_kmeans = DELPOZO.getKmeansPieces()
    delpozo_kmeans.show()
    delpozo_kmeans.save(DELPOZO_PATH + "kmeans" + JPG)

# Marchesa
def MARCHESA():
    MARCHESA_PATH = "./Marchesa/marchesa"
    JPG = ".jpg"
    MARCHESA = Collection()
    marchesa = [piece(Image.open(MARCHESA_PATH + str(i) + JPG)) for i in range(1, 13)]
    MARCHESA.add(marchesa)
    marchesa_collection = MARCHESA.getMergePieces()
    marchesa_collection.show()
    marchesa_collection.save(MARCHESA_PATH + JPG)
    marchesa_kmeans = MARCHESA.getKmeansPieces()
    marchesa_kmeans.show()
    marchesa_kmeans.save(MARCHESA_PATH + "kmeans" + JPG)

# RalphLauren
def RALPH():
    RALPH_PATH = "./RalphLauren/ralph"
    JPG = ".jpg"
    RALPH = Collection()
    ralph = [piece(Image.open(RALPH_PATH + str(i) + JPG)) for i in range(1, 13)]
    RALPH.add(ralph)
    ralph_collection = RALPH.getMergePieces()
    ralph_collection.show()
    ralph_collection.save(RALPH_PATH + JPG)
    ralph_kmeans = RALPH.getKmeansPieces()
    ralph_kmeans.show()
    ralph_kmeans.save(RALPH_PATH + "kmeans" + JPG)

# VeraWang
def VERA():
    VERA_PATH = "./VeraWang/vera"
    JPG = ".jpg"
    VERA = Collection()
    vera = [piece(Image.open(VERA_PATH + str(i) + JPG)) for i in range(1, 13)]
    VERA.add(vera)
    vera_collection = VERA.getMergePieces()
    vera_collection.show()
    vera_collection.save(VERA_PATH + JPG)
    vera_kmeans = VERA.getKmeansPieces()
    vera_kmeans.show()
    vera_kmeans.save(VERA_PATH + "kmeans" + JPG)

if __name__ == "__main__":
    #CK()
    #ANNA()
    #COACH()
    #DELPOZO()
    #MARCHESA()
    #RALPH()
    #VERA()
    DNKY()


