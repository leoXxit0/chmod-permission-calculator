"""
chmod Permission Calculator
============================
Aplicación de escritorio para calcular visualmente los permisos de Linux
(notación octal y simbólica) y generar el comando `chmod` correspondiente.

Autor: (tu nombre aquí)
Licencia: MIT
"""

import customtkinter as ctk
import tkinter.messagebox as messagebox

# ---------------------------------------------------------------------------
# Configuración global de apariencia
# ---------------------------------------------------------------------------
ctk.set_appearance_mode("dark")          # Modo oscuro por defecto
ctk.set_default_color_theme("blue")      # Paleta de color base


class PermissionSection(ctk.CTkFrame):
    """
    Widget reutilizable que representa una sección de permisos
    (Propietario, Grupo u Otros) con sus tres checkboxes:
    Lectura (4), Escritura (2) y Ejecución (1).
    """

    def __init__(self, master, title: str, accent_color: str, on_change_callback, **kwargs):
        super().__init__(master, corner_radius=14, fg_color=("gray90", "gray17"), **kwargs)

        self.on_change_callback = on_change_callback

        # Variables booleanas para cada permiso
        self.var_read = ctk.BooleanVar(value=False)
        self.var_write = ctk.BooleanVar(value=False)
        self.var_execute = ctk.BooleanVar(value=False)

        # --- Título de la sección -------------------------------------------------
        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=accent_color,
        )
        title_label.pack(pady=(16, 4), padx=16)

        # --- Valor octal parcial de esta sección (0-7) -----------------------------
        self.octal_label = ctk.CTkLabel(
            self,
            text="0",
            font=ctk.CTkFont(size=32, weight="bold"),
        )
        self.octal_label.pack(pady=(0, 12))

        # --- Checkboxes -------------------------------------------------------------
        checks_frame = ctk.CTkFrame(self, fg_color="transparent")
        checks_frame.pack(pady=(0, 16), padx=16, fill="x")

        self.chk_read = ctk.CTkCheckBox(
            checks_frame,
            text="Lectura (r) — 4",
            variable=self.var_read,
            command=self._notify_change,
            checkbox_width=22,
            checkbox_height=22,
        )
        self.chk_read.pack(anchor="w", pady=6, padx=8)

        self.chk_write = ctk.CTkCheckBox(
            checks_frame,
            text="Escritura (w) — 2",
            variable=self.var_write,
            command=self._notify_change,
            checkbox_width=22,
            checkbox_height=22,
        )
        self.chk_write.pack(anchor="w", pady=6, padx=8)

        self.chk_execute = ctk.CTkCheckBox(
            checks_frame,
            text="Ejecución (x) — 1",
            variable=self.var_execute,
            command=self._notify_change,
            checkbox_width=22,
            checkbox_height=22,
        )
        self.chk_execute.pack(anchor="w", pady=6, padx=8)

    def _notify_change(self):
        """Recalcula el valor octal propio y avisa al padre para refrescar todo."""
        self.octal_label.configure(text=str(self.get_octal_value()))
        if self.on_change_callback:
            self.on_change_callback()

    def get_octal_value(self) -> int:
        """Devuelve el valor octal (0-7) resultante de esta sección."""
        value = 0
        if self.var_read.get():
            value += 4
        if self.var_write.get():
            value += 2
        if self.var_execute.get():
            value += 1
        return value

    def get_symbolic_value(self) -> str:
        """Devuelve la representación simbólica de 3 caracteres, ej. 'rwx', 'r-x'."""
        r = "r" if self.var_read.get() else "-"
        w = "w" if self.var_write.get() else "-"
        x = "x" if self.var_execute.get() else "-"
        return f"{r}{w}{x}"

    def reset(self):
        """Desmarca todas las casillas de la sección."""
        self.var_read.set(False)
        self.var_write.set(False)
        self.var_execute.set(False)
        self.octal_label.configure(text="0")


class ChmodCalculatorApp(ctk.CTk):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()

        # --- Configuración de la ventana ------------------------------------------
        self.title("chmod Permission Calculator")
        self.geometry("880x640")
        self.minsize(720, 560)

        # Grid principal responsivo
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self._build_sections()
        self._build_results()
        self._build_footer_buttons()

        # Cálculo inicial (todo en 0)
        self._update_results()

    # -----------------------------------------------------------------------
    # Construcción de la interfaz
    # -----------------------------------------------------------------------
    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", padx=24, pady=(20, 10))
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="🔐 Calculadora de Permisos chmod",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        title.grid(row=0, column=0, sticky="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Genera visualmente los permisos de Linux para tus archivos y carpetas",
            font=ctk.CTkFont(size=13),
            text_color=("gray30", "gray70"),
        )
        subtitle.grid(row=1, column=0, sticky="w", pady=(2, 0))

        # --- Switch de tema (oscuro/claro) -----------------------------------------
        theme_frame = ctk.CTkFrame(header, fg_color="transparent")
        theme_frame.grid(row=0, column=1, rowspan=2, sticky="e", padx=(10, 0))

        self.theme_label = ctk.CTkLabel(theme_frame, text="🌙 Oscuro", font=ctk.CTkFont(size=13))
        self.theme_label.pack(side="left", padx=(0, 8))

        self.theme_switch = ctk.CTkSwitch(
            theme_frame,
            text="",
            command=self._toggle_theme,
            width=46,
        )
        self.theme_switch.pack(side="left")
        # El switch inicia apagado porque arrancamos en modo oscuro
        self.theme_switch.deselect()

    def _build_sections(self):
        """Crea las tres columnas: Propietario, Grupo, Otros."""
        sections_container = ctk.CTkFrame(self, fg_color="transparent")
        sections_container.grid(row=1, column=0, sticky="nsew", padx=24, pady=10)
        sections_container.grid_columnconfigure((0, 1, 2), weight=1, uniform="col")
        sections_container.grid_rowconfigure(0, weight=1)

        self.owner_section = PermissionSection(
            sections_container,
            title="👤 Propietario (Owner)",
            accent_color="#3B8ED0",
            on_change_callback=self._update_results,
        )
        self.owner_section.grid(row=0, column=0, sticky="nsew", padx=8)

        self.group_section = PermissionSection(
            sections_container,
            title="👥 Grupo (Group)",
            accent_color="#2FA572",
            on_change_callback=self._update_results,
        )
        self.group_section.grid(row=0, column=1, sticky="nsew", padx=8)

        self.others_section = PermissionSection(
            sections_container,
            title="🌐 Otros (Others)",
            accent_color="#D0703B",
            on_change_callback=self._update_results,
        )
        self.others_section.grid(row=0, column=2, sticky="nsew", padx=8)

    def _build_results(self):
        """Sección inferior con los resultados en tiempo real."""
        results_frame = ctk.CTkFrame(self, corner_radius=14)
        results_frame.grid(row=2, column=0, sticky="ew", padx=24, pady=10)
        results_frame.grid_columnconfigure((0, 1), weight=1)

        # --- Valor Octal -------------------------------------------------------
        octal_box = ctk.CTkFrame(results_frame, fg_color="transparent")
        octal_box.grid(row=0, column=0, sticky="nsew", padx=20, pady=16)

        ctk.CTkLabel(
            octal_box, text="Notación Octal", font=ctk.CTkFont(size=13, weight="bold")
        ).pack(anchor="w")

        self.octal_result_label = ctk.CTkLabel(
            octal_box, text="000", font=ctk.CTkFont(size=40, weight="bold")
        )
        self.octal_result_label.pack(anchor="w")

        # --- Valor Simbólico -----------------------------------------------------
        symbolic_box = ctk.CTkFrame(results_frame, fg_color="transparent")
        symbolic_box.grid(row=0, column=1, sticky="nsew", padx=20, pady=16)

        ctk.CTkLabel(
            symbolic_box, text="Notación Simbólica", font=ctk.CTkFont(size=13, weight="bold")
        ).pack(anchor="w")

        self.symbolic_result_label = ctk.CTkLabel(
            symbolic_box, text="----------", font=ctk.CTkFont(size=40, weight="bold", family="Courier")
        )
        self.symbolic_result_label.pack(anchor="w")

        # --- Comando final -------------------------------------------------------
        command_frame = ctk.CTkFrame(self, fg_color="transparent")
        command_frame.grid(row=3, column=0, sticky="ew", padx=24, pady=(4, 10))
        command_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            command_frame, text="Comando listo para usar:", font=ctk.CTkFont(size=13, weight="bold")
        ).grid(row=0, column=0, sticky="w")

        self.filename_var = ctk.StringVar(value="archivo")
        self.filename_var.trace_add("write", lambda *args: self._update_results())

        filename_row = ctk.CTkFrame(command_frame, fg_color="transparent")
        filename_row.grid(row=1, column=0, sticky="ew", pady=(4, 6))
        filename_row.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(filename_row, text="Nombre del archivo/carpeta:").grid(
            row=0, column=0, sticky="w", padx=(0, 8)
        )
        self.filename_entry = ctk.CTkEntry(filename_row, textvariable=self.filename_var)
        self.filename_entry.grid(row=0, column=1, sticky="ew")

        self.command_entry = ctk.CTkEntry(
            command_frame,
            font=ctk.CTkFont(size=15, family="Courier", weight="bold"),
            height=42,
        )
        self.command_entry.grid(row=2, column=0, sticky="ew")

    def _build_footer_buttons(self):
        footer = ctk.CTkFrame(self, fg_color="transparent")
        footer.grid(row=4, column=0, sticky="ew", padx=24, pady=(6, 20))
        footer.grid_columnconfigure((0, 1), weight=1)

        self.copy_button = ctk.CTkButton(
            footer,
            text="📋 Copiar comando al portapapeles",
            command=self._copy_command,
            height=42,
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self.copy_button.grid(row=0, column=0, sticky="ew", padx=(0, 8))

        self.reset_button = ctk.CTkButton(
            footer,
            text="♻️ Limpiar / Resetear",
            command=self._reset_all,
            height=42,
            fg_color="transparent",
            border_width=2,
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self.reset_button.grid(row=0, column=1, sticky="ew", padx=(8, 0))

    # -----------------------------------------------------------------------
    # Lógica de la aplicación
    # -----------------------------------------------------------------------
    def _update_results(self):
        """Recalcula octal, simbólico y comando final; actualiza la GUI."""
        owner_val = self.owner_section.get_octal_value()
        group_val = self.group_section.get_octal_value()
        others_val = self.others_section.get_octal_value()

        octal_string = f"{owner_val}{group_val}{others_val}"
        symbolic_string = (
            f"-{self.owner_section.get_symbolic_value()}"
            f"{self.group_section.get_symbolic_value()}"
            f"{self.others_section.get_symbolic_value()}"
        )

        self.octal_result_label.configure(text=octal_string)
        self.symbolic_result_label.configure(text=symbolic_string)

        filename = self.filename_var.get().strip() or "archivo"
        command = f"chmod {octal_string} {filename}"

        self.command_entry.configure(state="normal")
        self.command_entry.delete(0, "end")
        self.command_entry.insert(0, command)

    def _toggle_theme(self):
        """Alterna entre modo oscuro y claro."""
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("light")
            self.theme_label.configure(text="☀️ Claro")
        else:
            ctk.set_appearance_mode("dark")
            self.theme_label.configure(text="🌙 Oscuro")

    def _copy_command(self):
        """Copia el comando actual al portapapeles del sistema."""
        command = self.command_entry.get()
        self.clipboard_clear()
        self.clipboard_append(command)
        self.update()  # Necesario en algunos sistemas para persistir el portapapeles

        original_text = self.copy_button.cget("text")
        self.copy_button.configure(text="✅ ¡Copiado!")
        self.after(1500, lambda: self.copy_button.configure(text=original_text))

    def _reset_all(self):
        """Reinicia todas las casillas y el nombre de archivo a sus valores por defecto."""
        confirmed = messagebox.askyesno(
            "Confirmar reinicio",
            "¿Seguro que deseas limpiar todos los permisos seleccionados?",
        )
        if not confirmed:
            return

        self.owner_section.reset()
        self.group_section.reset()
        self.others_section.reset()
        self.filename_var.set("archivo")
        self._update_results()


def main():
    app = ChmodCalculatorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
