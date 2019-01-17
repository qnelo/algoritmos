sequence = 0
cats = []
dogs = []


def sequencer():
    global sequence
    sequence += 1
    return sequence


def get_first_sequence(list):
    return list[0]["sequence"] if len(list) > 0 else sequence + 1


def add_dog(name):
    dogs.append({"name": name, "sequence": sequencer()})


def add_cat(name):
    cats.append({"name": name, "sequence": sequencer()})


def get_dog():
    return (dogs.pop(0) if len(dogs) > 0 else {"name": "null"})["name"]


def get_cat():
    return (cats.pop(0) if len(cats) > 0 else {"name": "null"})["name"]


def get_pet():
    return get_dog() if get_first_sequence(cats) > get_first_sequence(dogs) else get_cat()


add_dog("dog1")
add_dog("dog2")
add_dog("dog3")
add_cat("cat1")
add_cat("cat2")
add_dog("dog4")
add_cat("cat3")
add_cat("cat4")

print(get_dog(), "deberia ser: dog1")
print(get_cat(), "deberia ser: cat1")
print(get_pet(), "deberia ser: dog2")
print(get_pet(), "deberia ser: dog3")
print(get_pet(), "deberia ser: cat2")
print(get_pet(), "deberia ser: dog4")
print(get_pet(), "deberia ser: cat3")
print(get_dog(), "deberia ser: null")
print(get_cat(), "deberia ser: cat4")
print(get_cat(), "deberia ser: null")
print(get_pet(), "deberia ser: null")
