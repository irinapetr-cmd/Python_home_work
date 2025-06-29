from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79111234567"),
    Smartphone("Samsung", "Galaxy S23", "+79219876543"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79335557777"),
    Smartphone("Google", "Pixel 7", "+79441112233"),
    Smartphone("OnePlus", "11 Pro", "+79509998877")
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
