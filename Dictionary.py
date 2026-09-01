# collection of key values, it cannot be changeble. ex- adarcard number of me not changable, in previous version it is unordered but now it is oredered

# 14)print element of dictionary
d = {"name": "Aryan", "age": 20, "city": "Pune"}

print(d)
print(d["age"])
print(d["city"])

# 15)changine key value in dict
d = {"name": "Aryan", "age": 20, "city": "Pune"}

d["name"] = "Rahul"
d["city"] = "Nashik"
print(d)

# 16)in value mupletiple dictionary
students = {
    1: {"name": "Aryan", "age": 20},
    2: {"name": "Rahul", "age": 21},
    3: {"name": "Rohit", "age": 22}
}
print(students)


d = {"name": ["Aryan", "Rahul", "Rohit"], "age": [20,30,50], "city": "Pune"}
print(d)


