<h1 align="center">🔴 POKÉDEX & SISTEMA DE COMBATE ⚪</h1>

<p align="center">
  Aplicación de escritorio interactiva desarrollada en Python que consume la <b>PokéAPI</b>, gestiona bases de datos locales con <b>SQLAlchemy</b> y cuenta con un sistema completo de batallas Pokémon por turnos, construida con <b>CustomTkinter</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/CustomTkinter-00599C?style=for-the-badge&logo=python&logoColor=white" alt="CustomTkinter"/>
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"/>
  <img src="https://img.shields.io/badge/PokeAPI-FFCB05?style=for-the-badge&logo=pokemon&logoColor=black" alt="PokeAPI"/>
</p>

---

## ✨ Características Principales

- 🔍 **Búsqueda y Detalles en Vivo:** Consulta cualquier Pokémon por nombre para obtener su ID, dimensiones, tipo, estadísticas de vida (HP), ataque y detección de rareza (Legendario o Mítico).
- 🎲 **Modo Sorpresa (Gacha):** Selecciona de forma aleatoria un Pokémon entre el ID 1 y 1025 de la PokéAPI para descubrir nuevas especies.
- 🗄️ **Inventario Local con SQLAlchemy:** Almacena automáticamente los Pokémon descubiertos en una base de datos SQLite (`inventariopokemon.db`), permitiéndote gestionar tu caja de colección y vaciarla cuando desees.
- ⚔️ **Sistema de Combate por Turnos:** Ventana secundaria independiente (`CTkToplevel`) para enfrentar a tu Pokémon contra enemigos salvajes aleatorios con opciones de ataque rápido, ataque pesado con probabilidad de crítico, curación y registro dinámico de eventos en tiempo real.

---

## 🛠️ Requisitos e Instalación

1. **Asegúrate de tener Python instalado y descarga las dependencias necesarias:**
   ```bash
   pip install customtkinter requests pillow sqlalchemy
