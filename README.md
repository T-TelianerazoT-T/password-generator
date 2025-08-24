
# 🔐 Generador de Contraseñas Seguras - Proyecto de Ciberseguridad

## 📖 Tabla de Contenidos
- 🎯 [Objetivo del Proyecto](#-objetivo-del-proyecto)
- ✨ [Características Principales](#-características-principales)
- 🛡️ [Aspectos de Seguridad](#-aspectos-de-seguridad)
- 📋 [Requisitos del Sistema](#-requisitos-del-sistema)
- 🚀 [Instalación y Ejecución](#-instalación-y-ejecución)
- 🎮 [Guía de Uso](#-guía-de-uso)
- 📊 [Diagramas del Sistema](#-diagramas-del-sistema)
- 🐛 [Troubleshooting](#-troubleshooting)
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

## 🛡 Aspectos de Seguridad

### 🔐 Algoritmo de Generación
```python
# Utiliza secrets para criptografía segura
password_chars.append(secrets.choice(conjunto))

# Mezcla con SystemRandom ( /dev/urandom o CryptGenRandom )
_sysrand.shuffle(password_chars) 
```
## 📋 Requisitos del Sistema

### ✅ Requisitos Mínimos
- Python: 3.6 o superior
- Sistema Operativo: Windows 7+, macOS 10.9+, o Linux moderno
- Memoria RAM: 512 MB mínimo
- Espacio en disco: 10 MB disponibles

### 📧 Para Envío de Correos
- Conexión a Internet temporal
- Cuenta Gmail con verificación en 2 pasos activada
- Contraseña de aplicación generada

## 🚀 Instalación y Ejecución

### 📥 Clonación del Repositorio
```bash
git clone https://github.com/T-TelianerazoT-T/password-generator.git
```
```bash
cd password-generator/src
```

### 🐍 Ejecución Directa
```bash
# Método 1: Ejecutar directamente****
python generador.py
```
```bash
# Método 2: Hacer ejecutable (Unix/macOS)
chmod +x generador.py
./generador.py
```
```bash
# Método 3: Desde cualquier ubicación
python /ruta/completa/generador.py
```
### 🔧 Dependencias
No se requieren instalaciones adicionales — solo Python estándar:
```python
import secrets, string, random, os, subprocess, sys
import smtplib, datetime, email
```

## 🎮 Guía de Uso
### 1. 🏁 Inicio del Programa
```bash
python generador.py
```

### ⚙️ Configuración de Parámetros
- Longitud: Ingresa número ≥ 8
- Caracteres especiales: Responde s o n

### 🔄 Generación y Opciones
1. 📋 Copiar al portapapeles
2. 💾 Guardar en archivo
3. 📧 Enviar por correo
4. 🛡️ Mostrar análisis de fortaleza
5. 🔄 Generar nueva contraseña
6. 🚪 Salir del programa

## 📊 Diagramas del Sistema
### 📌 Diagrama de Caso de Uso
El sistema permite generar contraseñas personalizadas, donde el usuario define la longitud y el tipo de caracteres (incluyendo opciones para incluir o excluir símbolos). Además, ofrece funcionalidades avanzadas como validación automática de seguridad, copiado al portapapeles, almacenamiento en archivo, envío por correo y reinicio del proceso.

<img width="1538" height="1463" alt="Diagrama de caso de uso" src="https://github.com/user-attachments/assets/28393b7e-11fd-4d9b-ac59-e3aa3186aa48" />

### 📌 Diagrama de Arquitectura
La aplicación sigue una estructura por capas: la presentación maneja la interfaz gráfica, la lógica contiene el generador y validador de contraseñas, la capa de servicios gestiona utilidades como el portapapeles y formateo de datos, mientras que la persistencia se encarga del guardado en archivo y envío por correo electrónico.

<img width="1391" height="3743" alt="Diagrama de arquitectura" src="https://github.com/user-attachments/assets/6e1d78e2-6894-4f75-bcf4-e9b8265e8cbb" />

## 🐛 Troubleshooting
### ❌ Problemas Comunes y Soluciones
Error al copiar al portapapeles:
```bash
# Linux: Instalar xclip
sudo apt-get install xclip
```
- macOS: Funciona nativo
- Windows: Funciona nativo

### ❌ Error de autenticación SMTP:
- ✅ Activar verificación en 2 pasos en Google
- ✅ Generar contraseña de aplicación
- ✅ Usar ESA contraseña, no la normal

### ❌ Problemas de encoding:
```bash 
PYTHONUTF8=1 python generador_contrasenas.py
```

## 📜 Licencia

Este proyecto fue desarrollado como parte de un deber universitario.  
Puedes utilizarlo y modificarlo libremente bajo la licencia MIT.  

Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Elian Erazo** - Estudiante de Ingeniería en Ciberseguridad

- 📧 Email: elerazom@uide.edu.ec  
- 🌐 GitHub: [@elianerazo](https://github.com/T-TelianerazoT-T)  
- 🔗 LinkedIn: [Elian Erazo]

### 🙏 Agradecimientos
- Profesores de la carrera de Ingeniería en Ciberseguridad por su guía y apoyo.  
- Comunidad Python por las excelentes librerías y documentación.  
- OWASP y NIST por los estándares de seguridad que inspiraron el proyecto.  
- Testers que ayudaron a mejorar la calidad y robustez del software.  

⭐ Si este proyecto te fue útil, ¡dale una estrella en GitHub!
