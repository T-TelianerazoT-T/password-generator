# Generador de Contraseñas Seguras

## 📌 Descripción
Este proyecto es un generador de contraseñas desarrollado en **Python**, como parte del Trabajo Autónomo 2.  
En esta versión inicial, el programa genera automáticamente una contraseña segura compuesta únicamente por **letras, caracteres especiales y números**, con una **longitud fija de 10 caracteres**.

---

## 🎯 Objetivo del Proyecto
Implementar un script básico de generación de contraseñas seguras como parte del proceso de aprendizaje, aplicando:
- Configuración de entorno de desarrollo.
- Uso de estructuras lógicas y repetitivas.
- Documentación y control de versiones con GitHub.

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.13.6
- **Editor de código:** Visual Studio Code
- **Control de versiones:** Git y GitHub

---
## 📂 Diagramas del Sistema
### Diagrama de Caso de Uso
El sistema permite generar contraseñas personalizadas, donde el usuario define la longitud y el tipo de caracteres (incluyendo opciones para incluir o excluir símbolos). Además, ofrece funcionalidades avanzadas como validación automática de seguridad, copiado al portapapeles, almacenamiento en archivo, envío por correo y reinicio del proceso.

---
### Diagrama de Arquitectura
La aplicación sigue una estructura por capas: la presentación maneja la interfaz gráfica, la lógica contiene el generador y validador de contraseñas, la capa de servicios gestiona utilidades como el portapapeles y formateo de datos, mientras que la persistencia se encarga del guardado en archivo y envío por correo electrónico.

---

## ⚙️ Configuración del Entorno
1. **Instalar Python:**  
   Descarga e instala la última versión desde [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Instalar Visual Studio Code:**  
   Descarga desde [https://code.visualstudio.com/](https://code.visualstudio.com/)

3. **Clonar este repositorio:**  
   ```bash
   git clone https://github.com/T-TelianerazoT-T/password-generator.git
