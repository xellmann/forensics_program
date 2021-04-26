import json

suspect_hair_color = ""

with open("dna.txt", "r") as file_handle:
    lines = file_handle.read().splitlines()
    for i in lines:
        suspect_dna = i

with open("human_characteristics.json", "r") as file_handle:
    human_characteristics = json.loads(file_handle.read())

with open("person_v2.json", "r") as file_handle:
    person = json.loads(file_handle.read())

hair_color_list = human_characteristics["hair_color"]
facial_shape_list = human_characteristics["facial_shape"]
eye_color_list = human_characteristics["eye_color"]
gender_list = human_characteristics["gender"]
race_list = human_characteristics["race"]

hair_color_dict = hair_color_list[0]
facial_shape_dict = facial_shape_list[0]
eye_color_dict = eye_color_list[0]
gender_dict = gender_list[0]
race_dict = race_list[0]

for i in hair_color_dict.items():
    if suspect_dna.find(str(i[1])) != -1:
        suspect_hair_color = i[0]

for i in facial_shape_dict.items():
    if suspect_dna.find(str(i[1])) != -1:
        suspect_facial_shape = i[0]

for i in eye_color_dict.items():
    if suspect_dna.find(str(i[1])) != -1:
        suspect_eye_color = i[0]

for i in gender_dict.items():
    if suspect_dna.find(str(i[1])) != -1:
        suspect_gender = i[0]

for i in race_dict.items():
    if suspect_dna.find(str(i[1])) != -1:
        suspect_race = i[0]

suspect_dict = {
    "race": suspect_race,
    "gender": suspect_gender,
    "eye_color": suspect_eye_color,
    "hair_color": suspect_hair_color,
    "facial_shape": suspect_facial_shape
}

print("The suspect human characteristics are:\nHair color: {0}\nFacial shape: {1}\nEye color: {2}\nGender: {3}"
      "\nRace: {4}\n".format(suspect_hair_color, suspect_facial_shape, suspect_eye_color, suspect_gender, suspect_race))

#print(suspect_dict)

eva = person["Eva"][0]
larisa = person["Larisa"][0]
matej = person["Matej"][0]
miha = person["Miha"][0]

counter = 0

for (key, value) in set(suspect_dict.items()) & set(eva.items()):
    counter = counter + 1
    if counter == 4:
        print("The suspect is Eva!")

counter = 0

for (key, value) in set(suspect_dict.items()) & set(larisa.items()):
    counter = counter + 1
    if counter == 4:
        print("The suspect is Larisa!")

counter = 0

for (key, value) in set(suspect_dict.items()) & set(matej.items()):
    counter = counter + 1
    if counter == 4:
        print("The suspect is Matej!")

counter = 0

for (key, value) in set(suspect_dict.items()) & set(miha.items()):
    counter = counter + 1
    if counter == 4:
        print("The suspect is Miha!")
