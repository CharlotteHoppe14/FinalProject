def create_profile():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    gender = input("Your gender (m/f/d)? ")
    interests = input("Choose 3 interests, split with comma: ").split(",")
    concert = input("Which concert do you visit? ")
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "interests": interests,
        "concert": concert
