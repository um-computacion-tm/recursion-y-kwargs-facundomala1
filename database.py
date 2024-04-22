import unittest

database = {
    1: {
        "nombre1": "Pablo",
        "nombre2": "Diego",
        "apellido1": "Ruiz",
        "apellido2": "Picasso"
    },
    2: {
        "nombre1": "Elio",
        "apellido1": "Anzi"
    },
    3: {
        "nombre1": "Elias",
        "nombre2": "Marcos",
        "nombre3": "Luciano",
        "apellido1": "Marcelo",
        "apellido2": "Gonzalez"
    },
    4: {
        "nombre1": "Adriano",
        "nombre2": "Salvador",
        "apellido1": "Barbuzza",
        "apellido2": "Martinez"
    },
    5: {
        "nombre1": "Damian",
        "nombre2": "Emiliano",
        "apellido1": "Martinez",
    }
}

def buscar_personas(*args, **kwargs):
    for persona_id, persona_data in kwargs.items():
        found = True
        for arg in args:
            if arg not in persona_data.values():
                found = False
                break
        if found:
            return persona_id
    return None

class TestDatabase(unittest.TestCase):
    def test_buscar_personas_persona1(self):
        result = buscar_personas("Pablo", "Diego", "Ruiz", "Picasso", **{str(k): v for k, v in database.items()})
        self.assertEqual(int(result), 1)

    def test_buscar_personas_persona2(self):
        result = buscar_personas("Elio", "Anzi", **{str(k): v for k, v in database.items()})
        self.assertEqual(int(result), 2)
        
    def test_buscar_personas_persona3(self):
       result = buscar_personas("Elias", "Marcos", "Luciano", "Marcelo", "Gonzalez", **{str(k): v for k, v in database.items()})
       self.assertEqual(int(result), 3) 
       
    def test_buscar_personas_persona4(self):
       result = buscar_personas("Adriano", "Salvador", "Martinez", "Barbuzza", **{str(k): v for k, v in database.items()})
       self.assertEqual(int(result), 4) 
       
    def test_buscar_personas_persona5(self):
       result = buscar_personas("Damian", "Emiliano", "Martinez", **{str(k): v for k, v in database.items()})
       self.assertEqual(int(result), 5)


if __name__ == '__main__':
    unittest.main()
