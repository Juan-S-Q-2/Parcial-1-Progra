from api import create_client, fetch_raw_data, filter_data
from ui import display_table

def get_user_input():
    while True:
        try:
            department = input("Ingrese el nombre del departamento: ").strip().upper()
            if not department:
                print("Error: El departamento no puede estar vacío.")
                continue

            limit = int(input("Ingrese el número de registros a consultar (1-100): "))
            if limit < 1 or limit > 100:
                print("Error: El número debe ser mayor que 0 y menor o igual a 100.")
                continue

            return department, limit
        except ValueError:
            print("Error: Ingrese un número válido.")

def run_app():
    print("=== Consulta de Datos de COVID-19 ===")
    department, limit = get_user_input()

    client = create_client()
    raw_data = fetch_raw_data(client, department, limit)
    filtered_data = filter_data(raw_data)

    display_table(filtered_data)

if __name__ == "__main__":
    run_app()
