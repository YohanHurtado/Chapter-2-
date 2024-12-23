famous = ["Sofía", "Doncic", "Santiago", "Carlos"]
print(f"Welcome, {famous[0].title()}, I'm glad to have you here")
print(f"Welcome, {famous[1].title()}, I'm glad to have you here")
print(f"Welcome, {famous[2].title()}, I'm glad to have you here")
print(f"Welcome, {famous[3].title()}, I'm glad to have you here\nOh, it seems that {famous[2].title()} couldn't make it")

print(f"Welcome, {famous[0].title()}, I'm glad to have you here")
print(f"Welcome, {famous[1].title()}, I'm glad to have you here")
print(f"Welcome, {famous[3].title()}, I'm glad to have you here")

print("It seems that the place is bigger that I intented, more guests will be coming to fill up the seats :)")
famous.insert(0, "Juan Diego")
famous.insert(1, "Kya")
famous.insert(2,"dee")

print("\nNow having you all here, I'd like to meet you")
print(f"Welcome, {famous[0].title()}, I'm glad to have you here")
print(f"Welcome, {famous[1].title()}, I'm glad to have you here")
print(f"Welcome, {famous[2].title()}, I'm glad to have you here")
print(f"Welcome, {famous[3].title()}, I'm glad to have you here")
print(f"Welcome, {famous[4].title()}, I'm glad to have you here")
print(f"Welcome, {famous[5].title()}, I'm glad to have you here")
print(f"Welcome, {famous[6].title()}, I'm glad to have you here")

print("\nSorry for this, I'll just have two of you :)")

deinvited_people = famous.pop()
print(f"\n{deinvited_people.title()} I won't be able to have you here")

deinvited_people = famous.pop()
print(f"\n{deinvited_people.title()} I won't be able to have you here")

deinvited_people = famous.pop()
print(f"\n{deinvited_people.title()} I won't be able to have you here")

deinvited_people = famous.pop()
print(f"\n{deinvited_people.title()} I won't be able to have you here")

deinvited_people = famous.pop()
print(f"\n{deinvited_people.title()} I won't be able to have you here")

del famous[0]
del famous[0]
print(famous)