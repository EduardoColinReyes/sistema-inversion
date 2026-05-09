# Sistema de Inversiones

Aplicación de escritorio desarrollada en Python con Tkinter que permite
calcular ganancias de distintos tipos de inversión tras autenticarse con un login.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FF6F00?style=for-the-badge&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=for-the-badge&logo=python&logoColor=white)
---

## Funcionalidades

- Autenticación de usuario con credenciales configurables por variables de entorno
- Selección de plazo de inversión: 1 mes, 3 meses, 6 meses o 1 año
- Cálculo automático de ganancias con validación de entradas
- Historial de cálculos visible en pantalla
- Botón de cierre de sesión con confirmación

---

## Estructura del proyecto

```
sistema-inversiones/
├── main.py          # Aplicación principal
├── img/
│   └── login.png    # Imagen del login
├── .gitignore
└── README.md
```

---

## Requisitos

Python 3.8 o superior y la librería Pillow:

```bash
pip install pillow
```

---

## Configuración de credenciales

Las credenciales son muy basicas siendo:

```
USUARIO = "root"
PASSWORD = "root"
```


## Cómo ejecutar

```bash
python main.py
```


