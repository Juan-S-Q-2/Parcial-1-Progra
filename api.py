from sodapy import Socrata

def create_client():
    return Socrata("www.datos.gov.co", None)

def fetch_raw_data(client, department, limit):
    return client.get("gt2j-8ykr", limit=limit, departamento_nom=department)

def filter_data(raw_data):
    filtered_data = []
    for entry in raw_data:
        filtered_data.append({
            "ciudad": entry.get("ciudad_municipio_nom", "N/A").upper(),
            "departamento": entry.get("departamento_nom", "N/A").upper(),
            "edad": entry.get("edad", "N/A"),
            "tipo_contagio": entry.get("fuente_tipo_contagio", "N/A"),
            "estado": entry.get("estado", "N/A")
        })
    return filtered_data
