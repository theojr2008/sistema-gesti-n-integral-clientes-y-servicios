"""
errores personalizados cuando el servicio no esté disponible y cuando se pasen datos inválidos al servicio.
todas las excepciones heredan de ErrorSistema para poder atrapar las excepciones de manera más simple.
"""

class ErrorSistema(Exception):
    pass

class ErrorServicioNoDisponible(ErrorSistema):
    """
    cuando un servicio no está disponible
    """
    pass


class ErrorValidacion(ErrorSistema):
    """
    cuando ocurre un error al validar datos, ej: un nombre de cliente vacio.
    """
    pass
