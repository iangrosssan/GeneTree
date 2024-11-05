class Miembro():
    def __init__(self, nombre, sexo, padre=None, madre=None, conyuges=None, hijos=None):
        self.nombre = nombre
        self.sexo = sexo
        self.padre = padre
        self.madre = madre
        self.hijos = hijos if hijos is not None else []
        self.conyuges = conyuges if conyuges is not None else []


    def __str__(self):
        return self.nombre
    

    def hijos_con(self, conyuge):
        hijos_comunes = []
        for hijo in self.hijos:
            if hijo in conyuge.hijos:
                hijos_comunes.append(hijo)
        return hijos_comunes


    def agregar_progenitores(self, padre, madre):
        self.padre = padre
        self.madre = madre
        padre.hijos.append(self)
        madre.hijos.append(self)
        padre.conyuges.append(madre)
        madre.conyuges.append(padre)


    def agregar_conyuge(self, conyuge):
        """Establece el conyuge para ambos miembros."""
        self.conyuges.append(conyuge)
        conyuge.conyuges.append(self)


    def agregar_descendiente(self, conyuge, hijo):
        if conyuge not in self.conyuges:
            self.conyuges.append(conyuge)
            conyuge.conyuges.append(self)
        self.hijos.append(hijo)
        conyuge.hijos.append(hijo)
        if self.sexo == "M":
            hijo.padre = self
            hijo.madre = conyuge
        else:
            hijo.padre = conyuge
            hijo.madre = self


    def obtener_parientes(self):
        hermanos_padre = [hermano.nombre for hermano in self.padre.hijos if hermano is not self] if self.padre else []
        hermanos_madre = [hermano.nombre for hermano in self.madre.hijos if hermano is not self] if self.madre else []
        hermanos = list(set(hermanos_padre).intersection(hermanos_madre))
        
        medios_hermanos = []
        if self.padre:
            medios_hermanos.extend([hermano.nombre for hermano in self.padre.hijos if hermano.madre != self.madre and hermano is not self])
        if self.madre:
            medios_hermanos.extend([hermano.nombre for hermano in self.madre.hijos if hermano.padre != self.padre and hermano is not self])
        medios_hermanos = list(set(medios_hermanos))

        hermanastros = []
        if self.padre:
            for conyuge in self.padre.conyuges:
                if conyuge != self.madre:
                    hermanastros.extend([hijos.nombre for hijos in conyuge.hijos])
        if self.madre:
            for conyuge in self.madre.conyuges:
                if conyuge != self.padre:
                    hermanastros.extend([hijos.nombre for hijos in conyuge.hijos])

 
        """Devuelve una lista de relaciones inmediatas para facilitar la visualización."""
        parientes = {
            "Padre": self.padre.nombre if self.padre else None,
            "Madre": self.madre.nombre if self.madre else None,
            "Conyuge": [conyuge.nombre for conyuge in self.conyuges],
            "Hermanos": hermanos,
            "Medios Hermanos": medios_hermanos,
            "Hermanastros": hermanastros,
            "Hijos": [hijo.nombre for hijo in self.hijos]
        }
        return parientes
    

paulina = Miembro("Paulina", "F")
alejandro = Miembro("Alejandro", "M")
marcos = Miembro("Marcos", "M")
semeolvidoelnombre = Miembro("Semeolvidoelnombre", "F")

ian = Miembro("Ian", "M")
alan = Miembro("Alan", "M")
daniela = Miembro("Daniela", "F")

# Establecer relaciones
ian.agregar_progenitores(alejandro, paulina)
alan.agregar_progenitores(alejandro, paulina)
daniela.agregar_progenitores(marcos, semeolvidoelnombre)

paulina.agregar_conyuge(marcos)

print(ian.obtener_parientes())
print(alan.obtener_parientes())
print(daniela.obtener_parientes())