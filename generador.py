#!/usr/bin/env python3
"""
Generador de Contraseñas Seguras - Versión Completa
Autor: Elian Erazo
Carrera: ING. Ciberseguridad
Materia: Lógica de Programación
"""

import secrets
import string
import random
import os
import subprocess
import sys
import smtplib
from typing import List, Tuple
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Usamos SystemRandom para operaciones de mezcla segura
_sysrand = random.SystemRandom()

class PasswordGenerator:
    def __init__(self):
        self.password = ""
        self.length = 0
        self.use_special_chars = True
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def configurar_parametros(self) -> Tuple[int, bool]:
        print("\n" + "="*50)
        print("🔐 GENERADOR DE CONTRASEÑAS SEGURAS")
        print("="*50)
        
        # Solicitar longitud
        while True:
            try:
                length = int(input("\n📏 Longitud de la contraseña (mínimo 8 caracteres): "))
                if length >= 8:
                    break
                else:
                    print("❌ La longitud mínima debe ser 8 caracteres")
            except ValueError:
                print("❌ Por favor, ingrese un número válido")
        
        # Solicitar si incluir caracteres especiales
        while True:
            especiales = input("✨ ¿Incluir caracteres especiales? (s/n): ").lower().strip()
            if especiales in ['s', 'si', 'sí', 'y', 'yes']:
                use_special = True
                break
            elif especiales in ['n', 'no']:
                use_special = False
                break
            else:
                print("❌ Por favor, responda 's' o 'n'")
        
        return length, use_special
    
    def generar_contrasena(self, length: int, use_special_chars: bool) -> str:        
        # Conjuntos de caracteres básicos
        mayusculas = string.ascii_uppercase
        minusculas = string.ascii_lowercase
        digitos = string.digits
        
        # Caracteres especiales (excluyendo caracteres ambiguos)
        especiales = "!@#$%&*()-_=+[]{};:,.<>?/|~"
        
        # Definir los conjuntos a usar
        conjuntos = [mayusculas, minusculas, digitos]
        if use_special_chars:
            conjuntos.append(especiales)
        
        # Seleccionar al menos un carácter de cada conjunto
        password_chars = []
        for conjunto in conjuntos:
            password_chars.append(secrets.choice(conjunto))
        
        # Combinar todos los conjuntos para llenar el resto
        todos_caracteres = ''.join(conjuntos)
        
        # Añadir caracteres aleatorios hasta alcanzar la longitud
        while len(password_chars) < length:
            password_chars.append(secrets.choice(todos_caracteres))
        
        # Mezclar de forma segura
        _sysrand.shuffle(password_chars)
        
        # Convertir a string
        self.password = ''.join(password_chars)
        self.length = length
        self.use_special_chars = use_special_chars
        
        return self.password
    
    def copiar_portapapeles(self):
        try:
            # Para Windows
            if os.name == 'nt':
                command = 'echo ' + self.password.strip() + '| clip'
                os.system(command)
            
            # Para macOS
            elif os.name == 'posix' and sys.platform == 'darwin':
                process = subprocess.Popen('pbcopy', universal_newlines=True, stdin=subprocess.PIPE)
                process.communicate(self.password)
            
            # Para Linux
            elif os.name == 'posix':
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
                process.communicate(self.password.encode('utf-8'))
            
            print("✅ Contraseña copiada al portapapeles")
            
        except Exception as e:
            print(f"❌ Error al copiar al portapapeles: {e}")
            print("💡 Puede copiar manualmente: ", self.password)
    
    def guardar_archivo(self):
        try:
            filename = "contrasena_segura_DEEM.txt"
            
            # Verificar si el archivo ya existe y agregar número
            counter = 1
            original_filename = filename
            while os.path.exists(filename):
                name, ext = os.path.splitext(original_filename)
                filename = f"{name}_{counter}{ext}"
                counter += 1
            
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("="*50 + "\n")
                file.write("🔐 CONTRASEÑA SEGURA GENERADA\n")
                file.write("="*50 + "\n\n")
                file.write(f"Contraseña: {self.password}\n")
                file.write(f"Longitud: {self.length} caracteres\n")
                file.write(f"Caracteres especiales: {'Sí' if self.use_special_chars else 'No'}\n")
                file.write(f"Fecha de generación: {self.obtener_fecha_actual()}\n\n")
                file.write("Generado por: Elian Erazo\n")
                file.write("Carrera: ING. Ciberseguridad\n")
                file.write("Materia: Lógica de Programación\n")
                file.write("="*50 + "\n")
            
            ruta_completa = os.path.abspath(filename)
            print(f"✅ Contraseña guardada en: {ruta_completa}")
            
            # Abrir el archivo automáticamente (opcional)
            try:
                if os.name == 'nt':  # Windows
                    os.startfile(ruta_completa)
                elif os.name == 'posix':  # macOS/Linux
                    subprocess.call(('open' if sys.platform == 'darwin' else 'xdg-open', ruta_completa))
            except:
                pass  # Si falla abrir el archivo, no es crítico
                
        except Exception as e:
            print(f"❌ Error al guardar archivo: {e}")
    
    def obtener_fecha_actual(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def enviar_correo(self):
        try:
            print("\n📧 ENVÍO POR CORREO ELECTRÓNICO")
            print("=" * 40)
            
            print("Para enviar por correo necesitarás:")
            print("1. Tu email de Gmail")
            print("2. Contraseña de aplicación (no la contraseña normal)")
            print("3. Conexión a internet")
            
            continuar = input("\n¿Deseas continuar? (s/n): ").lower().strip()
            if continuar not in ['s', 'si', 'sí']:
                return
            
            print("\n🔧 CONFIGURACIÓN DE CORREO")
            print("-" * 25)
            
            # Solicitar credenciales
            email_from = input("Tu email de Gmail: ").strip()
            email_password = input("Contraseña de aplicación: ").strip()
            email_to = input("Email destino: ").strip()
            
            # Validar emails
            if not all(['@' in email_from, '@' in email_to]):
                print("❌ Los emails deben ser válidos")
                return
            
            # Configuración Gmail
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            
            # Crear mensaje
            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = email_to
            msg['Subject'] = "🔐 Contraseña Segura Generada"
            
            body = f"""
            ¡Hola!
            
            Se ha generado una nueva contraseña segura para ti.
            
            📋 DETALLES:
            • Contraseña: {self.password}
            • Longitud: {self.length} caracteres
            • Caracteres especiales: {'Sí' if self.use_special_chars else 'No'}
            • Fecha: {self.obtener_fecha_actual()}
            
            🔒 Recomendaciones:
            - No compartas esta contraseña
            - Guárdala en un lugar seguro
            - Cámbiala periódicamente
            
            Generado por: Elian Erazo - ING. Ciberseguridad
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Enviar correo
            print("\n⏳ Enviando correo...")
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email_from, email_password)
            server.sendmail(email_from, email_to, msg.as_string())
            server.quit()
            
            print("✅ Correo enviado exitosamente!")
            print("📨 Revisa la bandeja de entrada del destinatario")
            
        except smtplib.SMTPAuthenticationError:
            print("\n❌ Error de autenticación")
            print("💡 Asegúrate de:")
            print("   - Usar una CONTRASEÑA DE APLICACIÓN (no tu contraseña normal)")
            print("   - Tener verificación en 2 pasos activada en Gmail")
            print("   - Los datos estén correctamente escritos")
            
        except smtplib.SMTPConnectError:
            print("\n❌ Error de conexión")
            print("💡 Verifica tu conexión a internet")
            
        except Exception as e:
            print(f"\n❌ Error al enviar correo: {e}")
            print("💡 Consejos:")
            print("   - Revisa que todos los datos estén correctos")
            print("   - Asegúrate de tener conexión a internet")
            print("   - Verifica la configuración de tu cuenta Gmail")
    
    def mostrar_fortaleza(self):
        print("\n📊 ANÁLISIS DE FORTALEZA:")
        print("-" * 30)
        
        # Calcular complejidad aproximada
        caracteres_unicos = len(set(self.password))
        porcentaje_unicos = (caracteres_unicos / self.length) * 100
        
        print(f"• Longitud: {self.length} caracteres")
        print(f"• Caracteres únicos: {caracteres_unicos} ({porcentaje_unicos:.1f}%)")
        print(f"• Tipos de caracteres incluidos:")
        print(f"  - Mayúsculas: {'Sí' if any(c.isupper() for c in self.password) else 'No'}")
        print(f"  - Minúsculas: {'Sí' if any(c.islower() for c in self.password) else 'No'}")
        print(f"  - Dígitos: {'Sí' if any(c.isdigit() for c in self.password) else 'No'}")
        print(f"  - Especiales: {'Sí' if any(not c.isalnum() for c in self.password) else 'No'}")
        
        # Evaluación simple
        if self.length >= 12 and porcentaje_unicos > 70:
            print("💪 Fortaleza: MUY FUERTE")
        elif self.length >= 10:
            print("👍 Fortaleza: FUERTE")
        else:
            print("⚠️  Fortaleza: MODERADA")
    
    def mostrar_menu_opciones(self):
        while True:
            print("\n" + "="*50)
            print("🎯 OPCIONES DISPONIBLES:")
            print("="*50)
            print("1. 📋 Copiar al portapapeles")
            print("2. 💾 Guardar en archivo")
            print("3. 📧 Enviar por correo")
            print("4. 📊 Mostrar análisis de fortaleza")
            print("5. 🔄 Generar nueva contraseña")
            print("6. 🚪 Salir del programa")
            print("="*50)
            
            opcion = input("Seleccione una opción (1-6): ").strip()
            
            if opcion == "1":
                self.copiar_portapapeles()
            elif opcion == "2":
                self.guardar_archivo()
            elif opcion == "3":
                self.enviar_correo()
            elif opcion == "4":
                self.mostrar_fortaleza()
            elif opcion == "5":
                print("\n🔄 Generando nueva contraseña...")
                return True  # Indicar que se debe reiniciar
            elif opcion == "6":
                print("\n👋 ¡Gracias por usar el Generador de Contraseñas Seguras!")
                print("Elian Erazo - ING. Ciberseguridad")
                return False  # Indicar que se debe salir
            else:
                print("❌ Opción no válida. Intente nuevamente.")
    
    def ejecutar(self):
        reiniciar = True
        
        while reiniciar:
            self.limpiar_pantalla()
            
            # Configurar parámetros
            length, use_special = self.configurar_parametros()
            
            # Generar contraseña
            password = self.generar_contrasena(length, use_special)
            
            # Mostrar resultado
            self.limpiar_pantalla()
            print("\n" + "="*50)
            print("✅ CONTRASEÑA GENERADA EXITOSAMENTE")
            print("="*50)
            print(f"🔑 Contraseña: {password}")
            print(f"📏 Longitud: {length} caracteres")
            print(f"✨ Caracteres especiales: {'Sí' if use_special else 'No'}")
            print("="*50)
            
            # Mostrar menú de opciones
            reiniciar = self.mostrar_menu_opciones()

def main():
    try:
        # Crear instancia del generador
        generador = PasswordGenerator()
        
        # Ejecutar el generador
        generador.ejecutar()
        
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido. ¡Hasta pronto!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
