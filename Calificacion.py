class Calificacion:
    def __init__(self, calificacion):
        self.calificacion = calificacion

    def obtener_clasificacion(self):
        if self.calificacion > 9.0:
            return "A"
        elif self.calificacion > 8.0:
            return "B"
        elif self.calificacion >= 7.5:
            return "C"
        else:
            return "R"

    def mostrar_clasificacion(self):
        clasificacion = self.obtener_clasificacion()
        print(f"La calificación es {clasificacion}.")