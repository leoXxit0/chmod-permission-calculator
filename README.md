# 🔐 chmod Permission Calculator

Una calculadora visual de permisos de Linux (`chmod`) con interfaz gráfica de escritorio, construida en Python con [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter).

Permite marcar los permisos de **Lectura**, **Escritura** y **Ejecución** para el **Propietario**, el **Grupo** y **Otros** mediante checkboxes, y genera en tiempo real la notación octal, la notación simbólica y el comando `chmod` listo para copiar y pegar en tu terminal.

También soporta los **permisos especiales** de Linux: **SUID**, **SGID** y **Sticky Bit**.

![Modo](https://img.shields.io/badge/interfaz-customtkinter-3B8ED0)
![Licencia](https://img.shields.io/badge/licencia-MIT-2FA572)

---

## ✨ Características

- Cálculo en tiempo real de los permisos de Propietario, Grupo y Otros.
- Generación automática de la notación octal (`755`, `644`, `4755`, etc.).
- Generación automática de la notación simbólica (`rwxr-xr-x`, `rwSr-Sr-T`, etc.).
- Soporte completo para permisos especiales: **SUID**, **SGID** y **Sticky Bit**.
- Comando `chmod` completo, listo para copiar al portapapeles con un clic.
- Campo editable para el nombre del archivo o carpeta objetivo.
- Modo oscuro / claro intercambiable.
- Botón de reinicio con confirmación para limpiar todos los permisos.

---

## 📋 Requisitos previos

- Python 3.8 o superior.
- La librería [`customtkinter`](https://pypi.org/project/customtkinter/).

Instala la dependencia con:

```bash
pip install customtkinter
```

> `tkinter` (el módulo base sobre el que se apoya `customtkinter`) viene incluido en la mayoría de instalaciones estándar de Python. En algunas distribuciones de Linux es posible que debas instalarlo aparte, por ejemplo:
>
> ```bash
> sudo apt install python3-tk
> ```

---

## 📦 Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/leoXxit0/chmod-permission-calculator.git
cd chmod-permission-calculator
```

### 2. Crea un entorno virtual

```bash
python3 -m venv .venv ; source .venv/bin/activate ; python -m pip install --upgrade pip ; python -m pip install customtkinter
```

### 3. Ejecuta la aplicación

```bash
python3 main.py
```

---

## 🚀 Cómo usarlo

Se abrirá una ventana con tres columnas (**Propietario**, **Grupo**, **Otros**) y una sección de **Permisos Especiales**:

1. Marca los checkboxes de Lectura, Escritura y Ejecución según los permisos que quieras asignar a cada categoría.
2. Si lo necesitas, activa SUID, SGID y/o Sticky Bit en la sección de permisos especiales.
3. Escribe el nombre del archivo o carpeta al que se aplicará el permiso.
4. Observa cómo se actualizan automáticamente:
   - La **notación octal** (ej. `0755` o `4755`).
   - La **notación simbólica** (ej. `rwxr-xr-x` o `rwsr-xr-x`).
   - El **comando `chmod`** completo (ej. `chmod 4755 archivo`).
5. Haz clic en **"📋 Copiar comando al portapapeles"** para copiarlo directamente a tu terminal.
6. Usa **"♻️ Limpiar / Resetear"** para reiniciar todos los permisos a cero.
---

## ⭐ Permisos especiales (SUID, SGID, Sticky Bit)

Además de los permisos básicos de lectura, escritura y ejecución, Linux define tres **permisos especiales** que ocupan un cuarto dígito adicional al principio de la notación octal (por ejemplo, el `4` en `4755`) y que modifican la notación simbólica con las letras `s`, `S`, `t` o `T`.

| Permiso | Valor octal | Se aplica a | Notación simbólica |
|---|---|---|---|
| **SUID** (Set User ID) | `4` | Propietario | `s` (si hay ejecución) / `S` (si no la hay) en la posición de ejecución del propietario |
| **SGID** (Set Group ID) | `2` | Grupo | `s` (si hay ejecución) / `S` (si no la hay) en la posición de ejecución del grupo |
| **Sticky Bit** | `1` | Otros | `t` (si hay ejecución) / `T` (si no la hay) en la posición de ejecución de otros |

### ¿Qué significan?

- **SUID**: cuando se ejecuta un archivo con este bit activo, el proceso se ejecuta con los privilegios del **propietario** del archivo en lugar de los del usuario que lo lanza. Se usa, por ejemplo, en binarios que necesitan privilegios elevados de forma controlada (como `passwd`).
- **SGID**: en un archivo ejecutable, funciona de forma similar a SUID pero con el **grupo** del archivo. Aplicado a un **directorio**, hace que todos los archivos y subdirectorios creados dentro hereden automáticamente el grupo del directorio padre, lo cual es muy útil para carpetas compartidas por equipos de trabajo.
- **Sticky Bit**: aplicado a un directorio, evita que los usuarios puedan eliminar o renombrar archivos que no les pertenecen, aunque tengan permiso de escritura sobre el directorio. Es el mecanismo detrás del comportamiento de carpetas compartidas como `/tmp`.

### Ejemplo de comando generado

Si activas Lectura+Escritura+Ejecución para el Propietario, Lectura+Ejecución para el Grupo, Lectura+Ejecución para Otros, y activas SUID:

```
Octal:     4755
Simbólico: -rwsr-xr-x
Comando:   chmod 4755 archivo
```

---

## 🛠️ Tecnologías utilizadas

- [Python 3](https://www.python.org/)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Si quieres proponer una mejora o corregir un error:

1. Haz un fork del repositorio.
2. Crea una rama para tu cambio (`git checkout -b mejora/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a tu rama (`git push origin mejora/nueva-funcionalidad`).
5. Abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 🔗 Repositorio

[github.com/leoXxit0/chmod-permission-calculator](https://github.com/leoXxit0/chmod-permission-calculator)
