suspect_dna = ""

hair_color_black = "CCAGCAATCGC"
hair_color_brown = "GCCAGTGCCG"
hair_color_blonde = "TTAGCTATCGC"

facial_shape_square = "GCCACGG"
facial_shape_round = "ACCACAA"
facial_shape_oval = "AGGCCTCA"

eye_color_blue = "TTGTGGTGGC"
eye_color_green = "GGGAGGTGGC"
eye_color_brown = "AAGTAGTGAC"

gender_female = "TGAAGGACCTTC"
gender_male = "TGCAGGAACTTC"

race_white = "AAAACCTCA"
race_black = "CGACTACAG"
race_asian = "CGCGGGCCG"

eva_gender = "female"
eva_race = "white"
eva_hair_color = "blonde"
eva_eye_color = "blue"
eva_face_shape = "oval"

larisa_gender = "female"
larisa_race = "white"
larisa_hair_color = "brown"
larisa_eye_color = "brown"
larisa_face_shape = "oval"

matej_gender = "male"
matej_race = "white"
matej_hair_color = "black"
matej_eye_color = "blue"
matej_face_shape = "oval"

miha_gender = "male"
miha_race = "white"
miha_hair_color = "brown"
miha_eye_color = "green"
miha_face_shape = "square"

with open("dna.txt", "r") as file_handle:
    print(file_handle)
    lines = file_handle.read().splitlines()
    for i in lines:
        suspect_dna = i

print(suspect_dna)

suspect = suspect_dna.find(hair_color_brown)
print(suspect)
