# 🔑 Generador de Contraseñas Seguras en Python

Este proyecto es un **generador de contraseñas seguras** hecho en Python.  
Permite crear contraseñas aleatorias con letras, números y símbolos, además de evaluar su **fuerza** (Débil, Media, Fuerte, Muy fuerte).

## ⚙️ Configuración

Dentro del código puedes modificar:

```python
cantidad = 5    # Número de contraseñas a generar
longitud = 16   # Longitud de cada contraseña
generar_contraseña(longitud=16,
                   incluir_mayus=True,
                   incluir_digitos=True,
                   incluir_simbolos=True)
01) qA7@tzFj4mX#yR2N  |  fuerza≈92/100 (Muy fuerte)
02) H9pZfW$1uM!kL3vY  |  fuerza≈95/100 (Muy fuerte)
03) tG2#bD7xPjW!4zRm  |  fuerza≈90/100 (Muy fuerte)
04) X5w$K8nE1@hFq9pZ  |  fuerza≈94/100 (Muy fuerte)
05) Jc3#YpTz6rM!nH8Q  |  fuerza≈93/100 (Muy fuerte)
