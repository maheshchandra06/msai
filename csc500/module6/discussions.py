if __name__ == '__main__':
    # creates list of numbers
    numbers_list = [12, 16, 19, 23, 29]                 # [12, 16, 19, 23, 29]
    print(numbers_list)

    # add element to list
    numbers_list[len(numbers_list):] = [30]             # [12, 16, 19, 23, 29, 30]
    print(numbers_list)
    # add element to list
    numbers_list.append(41)                             # [12, 16, 19, 23, 29, 30, 41]
    print(numbers_list)
    # add element to list in specific position
    numbers_list.insert(3,20)            # [12, 16, 19, 20, 23, 29, 30, 41]
    print(numbers_list)
    # add elements from one list to another
    numbers_list.extend([51, 62])                       # [12, 16, 19, 20, 23, 29, 30, 41, 51, 62]
    print(numbers_list)

    # updates elements of list
    numbers_list[2] = 11                                # [12, 16, 11, 20, 23, 29, 30, 41, 51, 62]
    print(numbers_list)

    # remove first elements specified from list
    numbers_list.remove(23)                             # [12, 16, 11, 20, 29, 30, 41, 51, 62]
    print(numbers_list)
    # remove last item
    numbers_list.pop()                                  # [12, 16, 11, 20, 29, 30, 41, 51]
    print(numbers_list)
    # remove specific item in given position
    numbers_list.pop(2)                                 # [12, 16, 20, 29, 30, 41, 51]
    print(numbers_list)


    # creation of dictionary
    profile = {
        "name" : "Shiela",
        "age" : "30",
        "occupation" : "lawyer"
    }

    # retrieve values associated with key
    print(profile["name"])                              # Shiela
    print(profile.get("occupation", "N/A"))             # lawyer
    print(profile.get("mobile","9632587410"))           # 9632587410

    # add new entry
    profile["location"] = "United States"               # {'name': 'Shiela', 'age': '30', 'occupation': 'lawyer', 'location': 'United States'}
    print(profile)

    # updates the entry
    profile["age"] = 29                                 # {'name': 'Shiela', 'age': 29, 'occupation': 'lawyer', 'location': 'United States'}
    print(profile)
    print(profile.update({"height": "5.4 ft"}))         # {'name': 'Shiela', 'age': 29, 'occupation': 'lawyer', 'location': 'United States', 'height': '5.4 ft'}
    print(profile)

    # delete the key entry
    del profile["age"]                                  # {'name': 'Shiela', 'occupation': 'lawyer', 'location': 'United States', 'height': '5.4 ft'}
    print(profile)
    profile.pop("height")                               # {'name': 'Shiela', 'occupation': 'lawyer', 'location': 'United States'}
    print(profile)

    print("Name: {}\nProfession: {}\nLocation: {}".format(profile["name"],profile["occupation"],profile["location"]))
