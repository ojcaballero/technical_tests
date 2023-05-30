from petstore_api import create_user, get_user_data, find_pets_by_status
from pet import Pets

## Punto 1: Crear usuario y obtener sus datos

# Diccionario que contiene la información del usuario a crear
user_data = {
    "id": 2305,
    "username": "ocaballero",
    "firstName": "Olenka",
    "lastName": "Caballero",
    "email": "olecb@gmail.com",
    "password": "olenkacaballeroburgos",
    "phone": "949849339",
}

create_user(user_data)

# Recuperamos datos del usuario recién creado
user_info = get_user_data(user_data["username"]) 
print("Usuario creado: ", user_info)

## Punto 2: Obtener nombres de mascotas vendidas
sold_pets = find_pets_by_status("sold")
print("Nombres de mascotas vendidas:")
for pet in sold_pets:
    print(pet)

## Punto 3: Clase para contar mascotas con el mismo nombre

pets = Pets(sold_pets)
count_results = pets.get_pets_by_count()
print("\nCantidad de mascotas con el mismo nombre:", count_results)
