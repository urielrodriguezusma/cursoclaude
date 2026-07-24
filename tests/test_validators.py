from src.utils.validators import is_valid_email


def test_rejects_leading_dot_domain():
    assert is_valid_email("usuario@.com") is False


def test_rejects_no_tld():
    assert is_valid_email("usuario@com") is False


def test_rejects_consecutive_dots():
    assert is_valid_email("usuario@dominio..com") is False


def test_rejects_leading_hyphen_domain():
    assert is_valid_email("usuario@-dominio.com") is False


def test_rejects_empty_or_no_at():
    assert is_valid_email("") is False
    assert is_valid_email("usuario.dominio.com") is False


def test_accepts_valid_emails():
    assert is_valid_email("usuario@dominio.com") is True
    assert is_valid_email("usuario+tag@dominio.co") is True
    assert is_valid_email("nombre.apellido@sub.dominio.org") is True
