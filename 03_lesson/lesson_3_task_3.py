from Address import Address
from Mailing import Mailing

# Создаем адреса
to_addr = Address("625042", "Тюмень", "Федюнинского", "58", "174")
from_addr = Address("640015", "Курган", "Тюменская", "24", "1")

# Создаем почтовое отправление
mail = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=300,
    track="RU123456789"
)

# Форматируем вывод
output = (
    f"Отправление {mail.track} из "
    f"{mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
    f"Стоимость {mail.cost} рублей."
)

print(output)
