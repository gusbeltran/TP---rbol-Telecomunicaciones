# 🌳 Arbol de Decision desde Cero en Python

Este proyecto implementa los fundamentos matematicos y logicos para construir un **Arbol de Decision desde cero** usando Python puro, sin librerias externas de Machine Learning (como Scikit-Learn o Pandas). 

El objetivo es modelar y calcular paso a paso la incertidumbre y la relevancia de los atributos utilizando la **Entropia de Shannon** y la **Ganancia de Informacion ($IG$)** sobre un dataset de clientes de telecomunicaciones.

---

## 📋 ¿Que se hace en este proyecto?
1. **Modelado de Datos:** Se procesa una lista de diccionarios que representa clientes con caracteristicas como `edad`, `uso_datos`, `linea_fija` y una etiqueta objetivo (`acepto_oferta`).
2. **Calculo de Entropia:** Se mide la impureza o incertidumbre inicial del conjunto de datos mediante la formula de Entropia de Shannon.
3. **Particionamiento y Entropia Condicional:** Se evalua que tanto orden aporta separar los datos basandose en un atributo especifico (por ejemplo, `linea_fija`).
4. **Ganancia de Informacion:** Se calcula la diferencia entre la entropia inicial y la condicional para determinar que tan util es un atributo para tomar decisiones en el arbol.

---

## 💡 ¿Por que no uso Pandas ni librerias externas?
No se utiliza `pandas` ni librerias de terceros **deliberadamente**. Hacerlo todo con estructuras nativas de Python (listas y diccionarios) permite:
- **Entender el motor por debajo:** Ver exactamente como se recorren los datos, como se agrupan con diccionarios y como operan las matematicas sin "magia negra" o funciones ocultas.
- **Ejemplo simple y didactico:** Sirve como base ligera y directa para cualquier persona que quiera aprender la logica pura de los algoritmos de clasificacion.

---

## ⭐ ¿Por que construir esto desde cero es una buena practica?
- **Dominio real del algoritmo:** Entender la entropia y la particion a nivel de codigo afianza los conceptos teoricos mucho mejor que solo importar una funcion ya hecha.
- **Independencia tecnologica:** Te da la capacidad de trasladar esta misma logica a cualquier otro lenguaje de programacion si fuera necesario.
- **Mejora de la habilidad logica:** Trabajar con bucles, condicionales y manipulacion de diccionarios puros fortalece la resolucion de problemas complejos en programacion.

---

## ⚙️ Requisitos para ver la demostracion
Para ejecutar este script y ver los resultados en tu computadora, solo necesitas:
- **Python 3.x** instalado (el proyecto utiliza unicamente la libreria estandar `math`, por lo que **no** requiere instalaciones adicionales ni `pip install`).

---

## 🚀 Como ejecutar la demostracion
1. Clona este repositorio o descarga el archivo con el codigo fuente.
2. Abre tu terminal o consola en la carpeta del archivo.
3. Ejecuta el siguiente comando:

```bash
python decision_tree.py
