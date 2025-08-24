
# 🔐 Generador de Contraseñas Seguras - Proyecto de Ciberseguridad

## 📖 Tabla de Contenidos
- 🎯 [Objetivo del Proyecto](#-objetivo-del-proyecto)
- ✨ [Características Principales](#-características-principales)
- 🛡️ [Aspectos de Seguridad](#-aspectos-de-seguridad)
- 📋 [Requisitos del Sistema](#-requisitos-del-sistema)
- 🚀 [Instalación y Ejecución](#-instalación-y-ejecución)
- 🎮 [Guía de Uso](#-guía-de-uso)
- 🏗️ [Arquitectura del Sistema](#-arquitectura-del-sistema)
- 🔧 [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- 📊 [Diagramas del Sistema](#-diagramas-del-sistema)
- 🐛 [Troubleshooting](#-troubleshooting)
- 📝 [Plan de Pruebas](#-plan-de-pruebas)
- 🔮 [Futuras Mejoras](#-futuras-mejoras)
- 👥 [Contribución](#-contribución)
- 📄 [Licencia](#-licencia)
- 👨‍💻 [Autor](#-autor)

## 🎯 Objetivo del Proyecto

Este proyecto tiene como objetivo principal desarrollar una herramienta robusta y segura en **Python** para la generación de contraseñas complejas mediante algoritmos criptográficos.  
Se busca implementar las mejores prácticas de seguridad informática y ofrecer múltiples opciones de gestión para la protección de credenciales digitales.

### Objetivos Específicos
- ✅ Implementar seguridad criptográfica usando módulos especializados  
- ✅ Permitir personalización avanzada de parámetros de generación  
- ✅ Garantizar compatibilidad multiplataforma (Windows, macOS, Linux)  
- ✅ Ofrecer gestión integral de contraseñas generadas  
- ✅ Educar en ciberseguridad mediante análisis de fortaleza  
- ✅ Proporcionar experiencia de usuario intuitiva y robusta

## ✨ Características Principales

### 🔐 Generación Segura
- Longitud personalizable (mínimo **8 caracteres**)  
- Inclusión/exclusión de caracteres especiales  
- Algoritmo criptográfico usando `secrets` y `SystemRandom`  
- Garantía de complejidad: mayúsculas, minúsculas, dígitos y caracteres especiales  

### 📋 Gestión de Contraseñas
- 📋 Copia al portapapeles nativa del sistema operativo  
- 💾 Guardado en archivo con metadatos de seguridad  
- 📧 Envío por correo electrónico mediante protocolo **TLS**  
- 📊 Análisis de fortaleza con métricas detalladas  

### 🎨 Experiencia de Usuario
- Interfaz intuitiva en **terminal** con emojis  
- Manejo robusto de errores y validaciones  
- Reinicio del programa sin necesidad de cerrarlo  
- Feedback claro en cada operación
  
### 🛡️ Seguridad Integrada
- Validación de entradas contra inyecciones  
- Manejo seguro de credenciales SMTP  
- Encriptación **TLS** para envío de correos  
- Metadatos de auditoría en archivos guardados  

## 🛡️ Aspectos de Seguridad

## 🛡️ Aspectos de Seguridad

### 🔐 Algoritmo de Generación
```python
# Utiliza secrets para criptografía segura
password_chars.append(secrets.choice(conjunto))
```

```python
# Mezcla con SystemRandom ( /dev/urandom o CryptGenRandom )
_sysrand.shuffle(password_chars) 






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

<img width="1538" height="1463" alt="Diagrama de caso de uso" src="https://github.com/user-attachments/assets/28393b7e-11fd-4d9b-ac59-e3aa3186aa48" />

---

### Diagrama de Arquitectura
La aplicación sigue una estructura por capas: la presentación maneja la interfaz gráfica, la lógica contiene el generador y validador de contraseñas, la capa de servicios gestiona utilidades como el portapapeles y formateo de datos, mientras que la persistencia se encarga del guardado en archivo y envío por correo electrónico.

<img width="1391" height="3743" alt="Diagrama de arquitectura" src="https://github.com/user-attachments/assets/6e1d78e2-6894-4f75-bcf4-e9b8265e8cbb" />

---

## ⚙️ Configuración del Entorno
1. **Instalar Python:**  
   Descarga e instala la última versión desde [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Instalar Visual Studio Code:**  
   Descarga desde [https://code.visualstudio.com/](https://code.visualstudio.com/)

3. **Clonar este repositorio:**  
   ```bash
   git clone https://github.com/T-TelianerazoT-T/password-generator.git

4. **link del video**
   https://mailinternacionaledu-my.sharepoint.com/:v:/g/personal/elerazoma_uide_edu_ec/Ea0cMrc3jeVFu_TxyEagfi8BjpurIY8lpJfl149_FUQ3cw
