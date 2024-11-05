class Miembro():
    def __init__(self, nombre, sexo, padre=None, madre=None, conyuges=None, hijos=None):
        self.nombre = nombre
        self.sexo = sexo
        self.padre = padre
        self.madre = madre
        self.hijos = hijos if hijos is not None else set()
        self.conyuges = conyuges if conyuges is not None else set()

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()      

    def hijos_con(self, conyuge):
        hijos_comunes = set()
        for hijo in self.hijos:
            if hijo in conyuge.hijos:
                hijos_comunes.add(hijo)
        return hijos_comunes

    def agregar_progenitores(self, padre, madre):
        self.padre = padre
        self.madre = madre
        padre.hijos.add(self)
        madre.hijos.add(self)
        if padre not in madre.conyuges:
            madre.conyuges.add(padre)
        if madre not in padre.conyuges:
            padre.conyuges.add(madre)

    def agregar_conyuge(self, conyuge):
        if conyuge not in self.conyuges:
            self.conyuges.add(conyuge)
        if self not in conyuge.conyuges:
            conyuge.conyuges.add(self)

    def agregar_descendiente(self, conyuge, hijo):
        if conyuge not in self.conyuges:
            self.conyuges.add(conyuge)
            conyuge.conyuges.add(self)
        if hijo not in self.hijos:
            self.hijos.add(hijo)
            conyuge.hijos.add(hijo)
        if self.sexo == "M":
            hijo.padre = self
            hijo.madre = conyuge
        else:
            hijo.padre = conyuge
            hijo.madre = self

    def obtener_parientes(self):
        hermanos_padre = [hermano.nombre for hermano in self.padre.hijos if hermano is not self] if self.padre else set()
        hermanos_madre = [hermano.nombre for hermano in self.madre.hijos if hermano is not self] if self.madre else set()
        hermanos = set(hermanos_padre).intersection(hermanos_madre)
        
        medios_hermanos = set()
        if self.padre:
            medios_hermanos.update([hermano.nombre for hermano in self.padre.hijos if hermano.madre != self.madre and hermano is not self])
        if self.madre:
            medios_hermanos.update([hermano.nombre for hermano in self.madre.hijos if hermano.padre != self.padre and hermano is not self])
        medios_hermanos = set(medios_hermanos)

        hermanastros = set()
        if self.padre:
            for conyuge in self.padre.conyuges:
                if conyuge != self.madre:
                    for h in conyuge.hijos:
                        if h not in self.padre.hijos:
                            hermanastros.add(h)
        if self.madre:
            for conyuge in self.madre.conyuges:
                if conyuge != self.padre:
                    for h in conyuge.hijos:
                        if h not in self.madre.hijos:
                            hermanastros.add(h)
 
        """Devuelve una lista de relaciones inmediatas para facilitar la visualización."""
        parientes = {
            "Nombre": self.nombre,
            "Padre": self.padre.nombre if self.padre else None,
            "Madre": self.madre.nombre if self.madre else None,
            "Conyuge": [conyuge.nombre for conyuge in self.conyuges],
            "Hermanos": hermanos,
            "Medios Hermanos": medios_hermanos,
            "Hermanastros": hermanastros,
            "Hijos": [hijo.nombre for hijo in self.hijos]
        }
        return parientes
