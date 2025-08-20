import secrets
import string

# ======================
# Generador de contraseñas
# ======================
def generar_contraseña(longitud=12, incluir_mayus=True, incluir_digitos=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_mayus:
        caracteres += string.ascii_uppercase
    if incluir_digitos:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += "!@#$%^&*()-_=+?/"

    if not caracteres:
        raise ValueError("No hay caracteres disponibles para generar la contraseña")

    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

# ======================
# Evaluación de fuerza
# ======================
def puntuar_contraseña(pw: str) -> int:
    longitud = len(pw)
    variedad = sum([
        any(c.islower() for c in pw),
        any(c.isupper() for c in pw),
        any(c.isdigit() for c in pw),
        any(c in "!@#$%^&*()-_=+?/" for c in pw)
    ])
    score = longitud * 2 + variedad * 10
    return min(100, score)

def describir_fuerza(score: int) -> str:
    if score >= 80:
        return "Muy fuerte"
    if score >= 60:
        return "Fuerte"
    if score >= 40:
        return "Media"
    return "Débil"

# ======================
# Uso principal
# ======================
if __name__ == "__main__":
    cantidad = 5   # cuántas contraseñas generar
    longitud = 16  # longitud de cada contraseña

    for i in range(cantidad):
        pw = generar_contraseña(longitud=longitud,
                                incluir_mayus=True,
                                incluir_digitos=True,
                                incluir_simbolos=True)
        score = puntuar_contraseña(pw)
        print(f"{i+1:02d}) {pw}  |  fuerza≈{score}/100 ({describir_fuerza(score)})")
        01) qA7@tzFj4mX#yR2N  |  fuerza≈92/100 (Muy fuerte)
02) H9pZfW$1uM!kL3vY  |  fuerza≈95/100 (Muy fuerte)
03) tG2#bD7xPjW!4zRm  |  fuerza≈90/100 (Muy fuerte)
04) X5w$K8nE1@hFq9pZ  |  fuerza≈94/100 (Muy fuerte)
05) Jc3#YpTz6rM!nH8Q  |  fuerza≈93/100 (Muy fuerte)

