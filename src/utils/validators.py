import re

# Regex anterior (con bug):
#   EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
# Problema: [^@\s]+ acepta '.' como primer caracter del dominio,
# por lo que "usuario@.com" pasaba la validacion incorrectamente.

EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9._%+-]+@"
    r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,}$"
)


def is_valid_email(email: str) -> bool:
    """Valida el formato de una direccion de email.

    Rechaza dominios que comienzan con punto o guion, puntos
    consecutivos, y direcciones sin TLD valido.
    """
    if not email or "@" not in email:
        return False
    return bool(EMAIL_REGEX.match(email))
