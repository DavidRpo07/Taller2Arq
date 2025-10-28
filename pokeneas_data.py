import random

# Reemplazar las urls de las imágenes con las URLs reales en el bucket de S3
POKENEAS = [
    {
        "id": 1,
        "nombre": "Cacnea",
        "altura": 0.55,
        "habilidad": "Dulzura extrema",
        "imagen": "https://TU_BUCKET.s3.amazonaws.com/arequipeachu.png",
        "frase": "El amor se sirve en porciones pequeñas."
    },
    {
        "id": 2,
        "nombre": "Clemont",
        "altura": 1.80,
        "habilidad": "Carga paisa",
        "imagen": "https://TU_BUCKET.s3.amazonaws.com/silletron.png",
        "frase": "A cada carga, sonrisa y berraquera."
    },
    {
        "id": 3,
        "nombre": "Dawn",
        "altura": 0.35,
        "habilidad": "Desvelar al oponente",
        "imagen": "https://TU_BUCKET.s3.amazonaws.com/tintozo.png",
        "frase": "Con un tintico la vida arranca mejor."
    },
    {
        "id": 4,
        "nombre": "Lysandrae",
        "altura": 0.95,
        "habilidad": "Proteína infinita",
        "imagen": "https://TU_BUCKET.s3.amazonaws.com/bandejairon.png",
        "frase": "Barriga llena, corazón contento."
    },
    {
        "id": 5,
        "nombre": "Poochyneaa",
        "altura": 1.10,
        "habilidad": "Pasos prohibidos",
        "imagen": "https://TU_BUCKET.s3.amazonaws.com/guarobot.png",
        "frase": "El ritmo se lleva en el alma."
    },
    {
        "id": 6,
        "nombre": "Tracey",
        "altura": 2.10,
        "habilidad": "Resistencia de altura",
        "imagen": "https://TU_BUCKET.s3.amazonaws.com/montanius.png",
        "frase": "Quien sube, aprende a mirar distinto."
    },
    {
        "id": 7,
        "nombre": "Xernea",
        "altura": 1.60,
        "habilidad": "Camino seguro",
        "imagen": "https://TU_BUCKET.s3.amazonaws.com/arrierum.png",
        "frase": "Se hace camino con cada paso firme."
    },
]

def random_pokenea():
    return random.choice(POKENEAS)