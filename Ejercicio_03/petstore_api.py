import requests

# URL base de la API
base_url = "https://petstore.swagger.io/v2"

# Función para crear usuario
def create_user(user_data):
    create_user_endpoint = "/user"
    response = requests.post(base_url + create_user_endpoint, json=user_data)
    if response.status_code == 200:
        print("Usuario creado exitosamente \n")
    else:
        print("Error al crear el usuario:", response.status_code)

# Función para obtener información de un usuario por su "username"
def get_user_data(username):
    get_user_endpoint = "/user/" + username 
    response = requests.get(base_url + get_user_endpoint) 
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos del usuario:", response.status_code)
        return None

# Función para encontrar mascotas por su "status"
def find_pets_by_status(status):
    find_pets_endpoint = "/pet/findByStatus"
    params = {
        "status": status # sold, pending, available
    }
    response = requests.get(base_url + find_pets_endpoint, params=params)
    if response.status_code == 200:
        pet_data = response.json()
        pets = []
        for pet in pet_data:
            pet_id = pet.get("id")
            pet_name = pet.get("name")

            # Esta validación se implementó porque habian registros que no tenian la propiedad "name"
            if pet_id and pet_name:
                pets.append((pet_id, pet_name))
        return pets
    else:
        print("Error al obtener las mascotas:", response.status_code)
        return []

