import json

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

eva = ["blonde", "oval", "blue", "female", "white"]
eva_gender = "female"
eva_race = "white"
eva_hair_color = "blonde"
eva_eye_color = "blue"
eva_face_shape = "oval"

larisa = ["brown", "oval", "brown", "female", "white"]
larisa_gender = "female"
larisa_race = "white"
larisa_hair_color = "brown"
larisa_eye_color = "brown"
larisa_face_shape = "oval"

matej = ["black", "oval", "blue", "male", "white"]
matej_gender = "male"
matej_race = "white"
matej_hair_color = "black"
matej_eye_color = "blue"
matej_face_shape = "oval"

miha = ["brown", "square", "green", "male", "white"]
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

with open("person.json", "r") as file_handle:
    person_dict = json.loads(file_handle.read())
    print(person_dict)

with open("human_characteristics.json", "r") as file_handle:
    human_characteristics_dict = json.loads(file_handle.read())
    print(human_characteristics_dict)

if suspect_dna.find(hair_color_black) != -1:
    suspect_hair_color = "black"
elif suspect_dna.find(hair_color_brown) != -1:
    suspect_hair_color = "brown"
elif suspect_dna.find(hair_color_blonde) != -1:
    suspect_hair_color = "blonde"
else:
    suspect_hair_color = ""

if suspect_dna.find(facial_shape_square) != -1:
    suspect_facial_shape = "square"
elif suspect_dna.find(facial_shape_round) != -1:
    suspect_facial_shape = "round"
elif suspect_dna.find(facial_shape_oval) != -1:
    suspect_facial_shape = "oval"
else:
    suspect_facial_shape = ""

if suspect_dna.find(eye_color_blue) != -1:
    suspect_eye_color = "blue"
elif suspect_dna.find(eye_color_green) != -1:
    suspect_eye_color = "green"
elif suspect_dna.find(eye_color_brown) != -1:
    suspect_eye_color = "brown"
else:
    suspect_eye_color = ""

if suspect_dna.find(gender_male) != -1:
    suspect_gender = "male"
elif suspect_dna.find(gender_female) != -1:
    suspect_gender = "female"
else:
    suspect_gender = ""

if suspect_dna.find(race_white) != -1:
    suspect_race = "white"
elif suspect_dna.find(race_black) != -1:
    suspect_race = "black"
elif suspect_dna.find(race_asian) != -1:
    suspect_race = "asian"
else:
    suspect_race = ""

suspect_characteristics = [suspect_hair_color, suspect_facial_shape, suspect_eye_color, suspect_gender, suspect_race]
print("The suspects human characteristics are: \nhaircolor: {0}\nfacial shape: {1}\neye color: {2}\ngender: {3}\nrace: "
      "{4}".format(suspect_hair_color, suspect_facial_shape, suspect_eye_color, suspect_gender, suspect_race))


if suspect_characteristics == eva:
    suspect = "Eva"
elif suspect_characteristics == larisa:
    suspect = "Larisa"
elif suspect_characteristics == matej:
    suspect = "Matej"
elif suspect_characteristics == miha:
    suspect = "Miha"

print("\nThe suspect is {0}".format(suspect))
