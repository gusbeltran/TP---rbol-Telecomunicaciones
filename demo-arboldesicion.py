import math


dataset = [
    {"id": 1, "edad": "Adulto", "uso_datos": "Alto", "linea_fija": "Sí", "acepto_oferta": "Sí"},
    {"id": 2, "edad": "Adulto", "uso_datos": "Alto", "linea_fija": "Sí", "acepto_oferta": "Sí"},
    {"id": 3, "edad": "Mayor",  "uso_datos": "Alto", "linea_fija": "Sí", "acepto_oferta": "Sí"},
    {"id": 4, "edad": "Adulto", "uso_datos": "Medio", "linea_fija": "Sí", "acepto_oferta": "Sí"},
    {"id": 5, "edad": "Adulto", "uso_datos": "Medio", "linea_fija": "Sí", "acepto_oferta": "Sí"},
    {"id": 6, "edad": "Adulto", "uso_datos": "Medio", "linea_fija": "No", "acepto_oferta": "No"},
    {"id": 7, "edad": "Adulto", "uso_datos": "Medio", "linea_fija": "No", "acepto_oferta": "No"},
    {"id": 8, "edad": "Joven",  "uso_datos": "Bajo", "linea_fija": "No", "acepto_oferta": "No"},
    {"id": 9, "edad": "Joven",  "uso_datos": "Bajo", "linea_fija": "No", "acepto_oferta": "No"},
    {"id": 10, "edad": "Joven", "uso_datos": "Bajo", "linea_fija": "No", "acepto_oferta": "No"}
]
# 2. Funcion para calcular la Entropia de Shannon general de un conjunto de datos
def calcular_entropia(dataset, etiqueta):
  total = len(dataset)
  if total == 0:
    return 0.0

  # Contar las frecuencias de cada clase según la etiqueta objetivo
  conteo = {}
  for fila in dataset:
    clase = fila[etiqueta]
    conteo[clase] = conteo.get(clase, 0) + 1

  # Calcular la entropiia usando la frmula de Shannon: -sum(p * log2(p))
  entropia = 0.0
  for clase, frecuencia in conteo.items():
    p = frecuencia / total
    if p > 0:
      entropia -= p * math.log2(p)

  return entropia


# 3. Funcion para calcular la entropia condicional ponderada de un atributo
def entropia_condicional(dataset, atributo, etiqueta):
  total_registros = len(dataset)
  if total_registros == 0:
    return 0.0

  # Paso A: Agrupar las filas por los valores unicos del atributo (ej. "Sí" / "No")
  subgrupos = {}
  for fila in dataset:
    valor_atributo = fila[atributo]
    if valor_atributo not in subgrupos:
      subgrupos[valor_atributo] = []
    subgrupos[valor_atributo].append(fila)  # Agregamos toda la fila al subgrupo

  # Paso B: Calcular la entropia de cada subgrupo, ponderarla y sumarla
  entropia_ponderada = 0.0
  for valor_atributo, grupo in subgrupos.items():
    peso = len(grupo) / total_registros
    entropia_grupo = calcular_entropia(
        grupo, etiqueta
    )  # Llamamos a tu funcion anterior
    entropia_ponderada += peso * entropia_grupo

  return entropia_ponderada


# --- PRUEBAS DE EJECUCION ---
if __name__ == "__main__":
  # Definimos que columna queremos predecir  (la etiqueta)
  columna_objetivo = "acepto_oferta"

  # 1. Entropia inicial del dataset completo
  h_inicial = calcular_entropia(dataset, columna_objetivo)
  print(f"Entropía inicial H(S): {h_inicial:.4f}")

  # 2. Entropia condicional usando el atributo "linea_fija"
  h_cond_linea = entropia_condicional(dataset, "linea_fija", columna_objetivo)
  print(f"Entropia condicional H(S | linea_fija): {h_cond_linea:.4f}")

  # 3. Ganancia de Información (Information Gain)
  ganancia_informacion = h_inicial - h_cond_linea
  print(f"Ganancia de Informacion (IG) con 'linea_fija': {ganancia_informacion:.4f}")