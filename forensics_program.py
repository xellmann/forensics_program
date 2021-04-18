eva = {
    "gender": "female",
    "race": "white",
    "hair_color": "blonde",
    "eye_color": "blue",
    "face_shape": "oval"
}
larisa = {
    "gender": "female",
    "race": "white",
    "hair_color": "brown",
    "eye_color": "brown",
    "face_shape": "oval"
}
matej = {
    "gender": "male",
    "race": "white",
    "hair_color": "black",
    "eye_color": "blue",
    "face_shape": "oval"
}
miha = {
    "gender": "male",
    "race": "white",
    "hair_color": "brown",
    "eye_color": "green",
    "face_shape": "square"
}
hair_color = {
    "black": "CCAGCAATCGC",
    "brown": "GCCAGTGCCG",
    "blonde": "TTAGCTATCGC"
}
facial_shape = {
    "square": "GCCACGG",
    "round": "ACCACAA",
    "oval": "AGGCCTCA"
}
eye_color = {
    "square": "TTGTGGTGGC",
    "round": "GGGAGGTGGC",
    "oval": "AAGTAGTGAC"
}
gender = {
    "female": "TGAAGGACCTTC",
    "male": "TGCAGGAACTTC"
}
race = {
    "white": "AAAACCTCA",
    "black": "CGACTACAG",
    "asian": "CGCGGGCCG"
}

with open("dna.txt", "r") as file_handle:
    print(str(file_handle))
