#create variables of different type

name = "Paul"
age = 34
legal_drinking_age = 18
age_diff = age - legal_drinking_age
old = True
def can_drink():
    if age >= legal_drinking_age:
        print(f"Yes he is! Get the man a beer! {name} is {age}, which is {age_diff} years older than the legal age")
    elif age < legal_drinking_age:
        print(f"Sorry do not serve this boy, {name} is too young for beer.")



print(f"Is {name} old enough to be served?")
print()
can_drink()
print()





