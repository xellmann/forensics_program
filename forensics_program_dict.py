import json

suspect_dna = ""

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
    "blue": "TTGTGGTGGC",
    "green": "GGGAGGTGGC",
    "brown": "AAGTAGTGAC"
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

#print(eva["hair_color"])

with open("dna.txt", "r") as file_handle:
#    print(file_handle)
    lines = file_handle.read().splitlines()
    for i in lines:
        suspect_dna = i

for key, value in gender.items():
    for v in value:
        if suspect_dna.find(value) != -1:
            print(key)
    #print(element)
    #if suspect_dna.find(element) != -1:
        #suspect_gender = gender.keys(element)
    #    print(element)


#print(suspect_dna)

suspect = suspect_dna.find(hair_color["brown"])
#print(suspect)

#with open("person.json", "r") as file_handle:
#    person_dict = json.loads(file_handle.read())
#    print(person_dict)

#with open("human_characteristics.json", "r") as file_handle:
#    human_characteristics_dict = json.loads(file_handle.read())
#    print(human_characteristics_dict)

#print("\nThe suspect is {0}".format(suspect))
