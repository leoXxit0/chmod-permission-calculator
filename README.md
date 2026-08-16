# 🔐 chmod Permission Calculator

Una aplicación de escritorio moderna y multiplataforma para calcular visualmente los permisos de archivos y carpetas en Linux/Unix. Marca casillas, obtén al instante la notación **octal** (`755`), la notación **simbólica** (`rwxr-xr-x`) y el comando `chmod` listo para copiar y pegar en tu terminal.

Ideal para quienes están aprendiendo administración de sistemas Linux o simplemente quieren evitar calcular permisos "a mano".

![Screenshot](docs/screenshot.png)

---

## ✨ Características

- 🖥️ **Interfaz moderna** construida con `customtkinter`, con esquinas redondeadas y diseño limpio.
- 🌗 **Modo oscuro / claro**: inicia en modo oscuro por defecto, con un interruptor para alternar en tiempo real.
- 🧩 **Tres secciones claras**: Propietario (Owner), Grupo (Group) y Otros (Others), cada una con checkboxes para Lectura, Escritura y Ejecución.
- ⚡ **Cálculo en tiempo real**: el valor octal y simbólico se actualizan automáticamente al marcar o desmarcar casillas.
- 📋 **Comando `chmod` generado al instante**, con campo editable para el nombre del archivo/carpeta.
- 📎 **Copiar al portapapeles** con un solo clic.
- ♻️ **Botón de reinicio** para limpiar todas las selecciones rápidamente.
- 📐 **Ventana redimensionable**, con diseño responsivo basado en `grid`.

---

## 📦 Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/chmod-permission-calculator.git
cd chmod-permission-calculator
```

### 2. (Opcional pero recomendado) Crea un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación

```bash
python main.py
```

---

## 🚀 Cómo usarlo

1. Abre la aplicación; iniciará en **modo oscuro**.
2. En cada columna (**Propietario**, **Grupo**, **Otros**), marca las casillas de **Lectura**, **Escritura** y/o **Ejecución** según los permisos que necesites.
3. Observa cómo se actualizan automáticamente:
   - El valor **octal** (ej. `755`).
   - El valor **simbólico** (ej. `-rwxr-xr-x`).
4. Escribe el nombre del archivo o carpeta al que aplicarás el permiso (por defecto `archivo`).
5. Copia el comando generado (ej. `chmod 755 archivo`) con el botón **"Copiar comando al portapapeles"**.
6. Usa **"Limpiar / Resetear"** para reiniciar todas las casillas.
7. Alterna entre **modo oscuro y claro** con el interruptor en la esquina superior derecha.

---

## 🗂️ Estructura del proyecto

```
chmod-permission-calculator/
├── main.py             # Código fuente de la aplicación
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Este archivo
├── LICENSE              # Licencia MIT
└── .gitignore           # Archivos ignorados por Git
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si quieres colaborar:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`).
4. Sube tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
