from tabulate import tabulate

def display_table(data):
    """Muestra los datos en una tabla formateada."""
    if not data:
        print("No se encontraron datos para mostrar.")
        return

    table_data = []
    for entry in data:
        table_data.append([
            entry.get("ciudad", "N/A"),
            entry.get("departamento", "N/A"),
            entry.get("edad", "N/A"),
            entry.get("tipo_contagio", "N/A"),
            entry.get("estado", "N/A")
        ])

    headers = ["Ciudad", "Departamento", "Edad", "Tipo de Contagio", "Estado"]

    print("\n--- Resultados de la Consulta ---\n")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
