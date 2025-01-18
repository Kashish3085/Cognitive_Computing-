#5  Rename a Key in Dictionary 

d= {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "Ney York"
}
print("Original Dictionary:",d)
d["location"]=d.pop("city")
print("New Dictionary:",d)