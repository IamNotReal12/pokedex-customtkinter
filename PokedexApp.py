import customtkinter as kc
import requests as rq
import PIL
import io
import random
import sqlalchemy



class ventanacombate(kc.CTkToplevel):
    def __init__(self, parent, *args, fg_color=None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self.pokedex = parent

        self.after(0, lambda: self.state("zoomed  "))
        self.title("Sistema Combate")
        self.attributes("-topmost", True)
        self.configure(fg_color="#1E1E1E")
        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.frame_pokemon_jugador = kc.CTkFrame(
            self,
            width=420,
            height=500,
            fg_color="#2B2B2B",
            corner_radius=20,
            border_width=3,
            border_color="#4CAF50",
        )
        self.frame_pokemon_jugador.grid(row=0, column=0, padx=20, pady=20)
        self.frame_pokemon_jugador.grid_propagate(False)
        self.frame_pokemon_jugador.grid_columnconfigure(0, weight=1)

        self.label_titulo_jugador = kc.CTkLabel(
            self.frame_pokemon_jugador,
            text="TU POKÉMON",
            font=("Roboto", 20, "bold"),
            text_color="#4CAF50",
        )
        self.label_titulo_jugador.grid(row=0, column=0, pady=(15, 5))

        self.frame_imagen_jugador = kc.CTkFrame(
            self.frame_pokemon_jugador,
            width=180,
            height=180,
            fg_color="white",
            corner_radius=10,
            border_width=2,
            border_color="#4CAF50",
        )
        self.frame_imagen_jugador.grid(row=1, column=0, pady=10)
        self.frame_imagen_jugador.pack_propagate(False)

        self.label_imagen_jugador = kc.CTkLabel(
            self.frame_imagen_jugador,
            text="[ Selecciona ]",
            width=180,
            height=180,
            text_color="gray",
        )
        self.label_imagen_jugador.pack()

        self.label_nombre_jugador = kc.CTkLabel(
            self.frame_pokemon_jugador,
            text="---",
            font=("Roboto", 24, "bold"),
            text_color="white",
        )
        self.label_nombre_jugador.grid(row=2, column=0, pady=5)

        self.barra_vida_jugador = kc.CTkProgressBar(
            self.frame_pokemon_jugador,
            width=300,
            height=20,
            fg_color="#404040",
            progress_color="#4CAF50",
            border_width=2,
            border_color="#1E1E1E",
        )
        self.barra_vida_jugador.grid(row=3, column=0, pady=10)
        self.barra_vida_jugador.set(1.0)

        self.label_hp_jugador = kc.CTkLabel(
            self.frame_pokemon_jugador,
            text="HP: 0 / 0",
            font=("Consolas", 16, "bold"),
            text_color="white",
        )
        self.label_hp_jugador.grid(row=4, column=0, pady=5)

        self.pokemonjugador = kc.CTkEntry(
            self.frame_pokemon_jugador,
            placeholder_text="Escribe tu Pokémon del inventario...",
            width=280,
            height=40,
            font=("Roboto", 14),
            fg_color="#1E1E1E",
            text_color="white",
            border_width=2,
            border_color="#4CAF50",
            corner_radius=8,
        )
        self.pokemonjugador.grid(row=5, column=0, pady=(10, 5))
        self.pokemonjugador.bind("<Return>", self.escogerpokemon)

        self.boton_atacar = kc.CTkButton(
            self.frame_pokemon_jugador,
            text="Iniciar combate...",
            width=200,
            height=45,
            font=("Roboto", 18, "bold"),
            fg_color="#2FD332",
            hover_color="#2CB71C",
            command=self.escogerpokemonenemigo,
        )
        self.boton_atacar.grid(row=6, column=0, pady=(10, 15))

        self.frame_pokemon_enemigo = kc.CTkFrame(
            self,
            width=420,
            height=500,
            fg_color="#2B2B2B",
            corner_radius=20,
            border_width=3,
            border_color="#D32F2F",
        )
        self.frame_pokemon_enemigo.grid(row=0, column=1, padx=20, pady=20)
        self.frame_pokemon_enemigo.grid_propagate(False)
        self.frame_pokemon_enemigo.grid_columnconfigure(0, weight=1)

        self.label_titulo_enemigo = kc.CTkLabel(
            self.frame_pokemon_enemigo,
            text="ENEMIGO SALVAJE",
            font=("Roboto", 20, "bold"),
            text_color="#D32F2F",
        )
        self.label_titulo_enemigo.grid(row=0, column=0, pady=(15, 5))

        self.frame_imagen_enemigo = kc.CTkFrame(
            self.frame_pokemon_enemigo,
            width=180,
            height=180,
            fg_color="white",
            corner_radius=10,
            border_width=2,
            border_color="#D32F2F",
        )
        self.frame_imagen_enemigo.grid(row=1, column=0, pady=10)
        self.frame_imagen_enemigo.pack_propagate(False)

        self.label_imagen_enemigo = kc.CTkLabel(
            self.frame_imagen_enemigo,
            text="[ Buscando... ]",
            width=180,
            height=180,
            text_color="gray",
        )
        self.label_imagen_enemigo.pack()

        self.label_nombre_enemigo = kc.CTkLabel(
            self.frame_pokemon_enemigo,
            text="---",
            font=("Roboto", 24, "bold"),
            text_color="white",
        )
        self.label_nombre_enemigo.grid(row=2, column=0, pady=5)

        self.barra_vida_enemigo = kc.CTkProgressBar(
            self.frame_pokemon_enemigo,
            width=300,
            height=20,
            fg_color="#404040",
            progress_color="#D32F2F",
            border_width=2,
            border_color="#1E1E1E",
        )
        self.barra_vida_enemigo.grid(row=3, column=0, pady=10)
        self.barra_vida_enemigo.set(1.0)

        self.label_hp_enemigo = kc.CTkLabel(
            self.frame_pokemon_enemigo,
            text="HP: 0 / 0",
            font=("Consolas", 16, "bold"),
            text_color="white",
        )
        self.label_hp_enemigo.grid(row=4, column=0, pady=5)

        self.label_estado_combate = kc.CTkLabel(
            self.frame_pokemon_enemigo,
            text="¡Prepárate para la batalla!",
            font=("Roboto", 16, "italic"),
            text_color="#AAAAAA",
        )
        self.label_estado_combate.grid(row=5, column=0, pady=(35, 10))
        self.caja_registro_combate = kc.CTkTextbox(
            self,
            width=450,
            height=500,
            font=("Consolas", 16, "bold"),
            fg_color="#121212",
            text_color="#FBC02D",
            corner_radius=20,
            border_width=4,
            border_color="#1976D2",
            wrap="word",
        )
        self.caja_registro_combate.grid(row=0, column=1, padx=20, pady=20)
        self.caja_registro_combate.insert(
            "0.0", "\n  ⚔️ REGISTRO DE COMBATE ⚔️\n  ─────────────────────────\n\n"
        )

        self.frame_pokemon_enemigo.grid(row=0, column=2, padx=20, pady=20)

    def escogerpokemon(self, event=None):
        Pokemon_referencia = self.pokemonjugador.get().lower()

        if Pokemon_referencia:
            url = f"https://pokeapi.co/api/v2/pokemon/{Pokemon_referencia}"
            respuesta = rq.get(url)

            if respuesta.status_code == 200:
                datos = respuesta.json()
                Nombre_pokemon = datos["name"]
                url_imagen = datos["sprites"]["other"]["home"]["front_default"]

                self.vida_max_jugador = datos["stats"][0]["base_stat"] * 3
                self.vida_actual_jugador = self.vida_max_jugador
                self.ataque_jugador = datos["stats"][1]["base_stat"] * 0.7

                self.label_nombre_jugador.configure(text=Nombre_pokemon.capitalize())
                self.label_hp_jugador.configure(
                    text=f"HP: {self.vida_actual_jugador} / {self.vida_max_jugador}"
                )

                porcentaje_vida = self.vida_actual_jugador / self.vida_max_jugador
                self.barra_vida_jugador.set(porcentaje_vida)

                if url_imagen:
                    respuesta_img = rq.get(url_imagen)
                    imagen_pil = PIL.Image.open(io.BytesIO(respuesta_img.content))

                    imagen_kc = kc.CTkImage(
                        light_image=imagen_pil, dark_image=imagen_pil, size=(150, 150)
                    )

                    self.label_imagen_jugador.configure(text="", image=imagen_kc)

                self.pokemonjugador.delete(0, "end")
                self.pokemonjugador.destroy()

    def escogerpokemonenemigo(self):
        Numeroid = random.randint(1, 1025)
        url = f"https://pokeapi.co/api/v2/pokemon/{Numeroid}"

        respuesta = rq.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()

            Nombre_pokemon = datos["name"]
            url_imagen = datos["sprites"]["other"]["home"]["front_default"]

            self.vida_max_enemigo = datos["stats"][0]["base_stat"] * 3
            self.vida_actual_enemigo = self.vida_max_enemigo
            self.ataque_enemigo = datos["stats"][1]["base_stat"] * 0.6

            self.label_nombre_enemigo.configure(text=Nombre_pokemon.capitalize())
            self.label_hp_enemigo.configure(
                text=f"HP: {self.vida_actual_enemigo} / {self.vida_max_enemigo}"
            )

            porcentaje_vida = self.vida_actual_enemigo / self.vida_max_enemigo
            self.barra_vida_enemigo.set(porcentaje_vida)

            if url_imagen:
                respuesta_img = rq.get(url_imagen)
                imagen_pil = PIL.Image.open(io.BytesIO(respuesta_img.content))

                imagen_kc = kc.CTkImage(
                    light_image=imagen_pil, dark_image=imagen_pil, size=(150, 150)
                )

                self.label_imagen_enemigo.configure(text="", image=imagen_kc)

            self.boton_atacar.destroy()

            self.frame_menu_combate = kc.CTkFrame(
                self.frame_pokemon_jugador, fg_color="transparent"
            )
            self.frame_menu_combate.grid(row=6, column=0, pady=(10, 15))

            self.boton_rapido = kc.CTkButton(
                self.frame_menu_combate,
                text="🗡️ Rápido",
                width=90,
                height=30,
                font=("Roboto", 12, "bold"),
                fg_color="#1976D2",
                hover_color="#1565C0",
                command=self.funcion_rapido,
            )
            self.boton_rapido.grid(row=0, column=0, padx=2)

            self.boton_pesado = kc.CTkButton(
                self.frame_menu_combate,
                text="💥 Pesado",
                width=90,
                height=30,
                font=("Roboto", 12, "bold"),
                fg_color="#D32F2F",
                hover_color="#B71C1C",
                command=self.funcion_pesado,
            )
            self.boton_pesado.grid(row=0, column=1, padx=2)

            self.boton_curar = kc.CTkButton(
                self.frame_menu_combate,
                text="🧪 Curar",
                width=90,
                height=30,
                font=("Roboto", 12, "bold"),
                fg_color="#388E3C",
                hover_color="#2E7D32",
                command=self.curarjugador,
            )
            self.boton_curar.grid(row=0, column=2, padx=2)

    def turno_enemigo(self):
        daño_enemigo = 0
        nombre_pokemon = self.label_nombre_jugador.cget("text")
        nombre_enemigo = self.label_nombre_enemigo.cget("text")

        if random.randint(1, 100) <= 50:
            daño_enemigo = self.ataque_enemigo * 1.3
            self.caja_registro_combate.insert(
                "end",
                f"\n> ¡GOLPE FUERTE! {nombre_enemigo} atacó con furia.\n> Daño recibido: {int(daño_enemigo)}\n",
            )
        else:
            daño_enemigo = self.ataque_enemigo
            self.caja_registro_combate.insert(
                "end",
                f"\n> {nombre_enemigo} usó un ataque normal.\n> Daño recibido: {int(daño_enemigo)}\n",
            )

        self.vida_actual_jugador -= daño_enemigo

        if self.vida_actual_jugador < 0:
            self.vida_actual_jugador = 0

        self.label_hp_jugador.configure(
            text=f"HP: {int(self.vida_actual_jugador)} / {self.vida_max_jugador}"
        )
        self.barra_vida_jugador.set(self.vida_actual_jugador / self.vida_max_jugador)
        self.caja_registro_combate.see("end")

        if self.vida_actual_jugador > 0:
            self.label_estado_combate.configure(
                text="¡Es tu turno!", text_color="#4CAF50"
            )
            self.boton_rapido.configure(state="normal")
            self.boton_pesado.configure(state="normal")
            self.boton_curar.configure(state="normal")
        else:
            self.label_estado_combate.configure(
                text="¡Combate Finalizado!", text_color="#AAAAAA"
            )
            self.caja_registro_combate.insert(
                "end", "\n> Has muerto... combate finalizado.\n"
            )

    def funcion_rapido(self):
        nombre_pokemon = self.label_nombre_jugador.cget("text")
        nombre_enemigo = self.label_nombre_enemigo.cget("text")

        self.boton_rapido.configure(state="disabled")
        self.boton_pesado.configure(state="disabled")
        self.boton_curar.configure(state="disabled")

        self.vida_actual_enemigo -= self.ataque_jugador

        if self.vida_actual_enemigo < 0:
            self.vida_actual_enemigo = 0

        self.label_hp_enemigo.configure(
            text=f"HP: {int(self.vida_actual_enemigo)} / {self.vida_max_enemigo}"
        )
        self.barra_vida_enemigo.set(self.vida_actual_enemigo / self.vida_max_enemigo)

        self.caja_registro_combate.insert(
            "end",
            f"\n> {nombre_pokemon} usó Ataque Rápido.\n> Daño infligido: {int(self.ataque_jugador)}\n",
        )
        self.caja_registro_combate.see("end")

        if self.vida_actual_enemigo > 0:
            self.label_estado_combate.configure(
                text="El enemigo está atacando...", text_color="#FBC02D"
            )
            self.after(1000, self.turno_enemigo)
        else:
            self.label_estado_combate.configure(
                text="¡Combate Finalizado!", text_color="#AAAAAA"
            )
            self.caja_registro_combate.insert(
                "end", f"\n🏆 ¡Has derrotado a {nombre_enemigo}!\n"
            )

    def funcion_pesado(self):
        daño_jugador = 0
        nombre_pokemon = self.label_nombre_jugador.cget("text")
        nombre_enemigo = self.label_nombre_enemigo.cget("text")

        self.boton_rapido.configure(state="disabled")
        self.boton_pesado.configure(state="disabled")
        self.boton_curar.configure(state="disabled")

        if random.randint(1, 100) <= 60:
            daño_jugador = self.ataque_jugador * 2

            self.vida_actual_enemigo -= daño_jugador

            if self.vida_actual_enemigo < 0:
                self.vida_actual_enemigo = 0

            self.caja_registro_combate.insert(
                "end",
                f"\n> ¡ÉXITO! {nombre_pokemon} acertó el ataque pesado.\n> Daño crítico: {int(daño_jugador)}\n",
            )
        else:
            self.caja_registro_combate.insert(
                "end",
                f"\n> {nombre_pokemon} falló el ataque cargado...\n> Turno desperdiciado.\n",
            )

        self.label_hp_enemigo.configure(
            text=f"HP: {int(self.vida_actual_enemigo)} / {self.vida_max_enemigo}"
        )
        self.barra_vida_enemigo.set(self.vida_actual_enemigo / self.vida_max_enemigo)

        self.caja_registro_combate.see("end")

        if self.vida_actual_enemigo > 0:
            self.label_estado_combate.configure(
                text="El enemigo está atacando...", text_color="#FBC02D"
            )
            self.after(1000, self.turno_enemigo)
        else:
            self.label_estado_combate.configure(
                text="¡Combate Finalizado!", text_color="#AAAAAA"
            )
            self.caja_registro_combate.insert(
                "end", f"\n🏆 ¡Has derrotado a {nombre_enemigo}!\n"
            )

    def curarjugador(self):
        nombre_pokemon = self.label_nombre_jugador.cget("text")

        self.boton_rapido.configure(state="disabled")
        self.boton_pesado.configure(state="disabled")
        self.boton_curar.configure(state="disabled")

        if self.vida_actual_jugador >= self.vida_max_jugador:
            self.caja_registro_combate.insert(
                "end",
                f"\n> {nombre_pokemon} ya tiene la vida al máximo. Turno desperdiciado.\n",
            )
        else:
            curacion_teorica = self.vida_max_jugador * 0.3
            vida_faltante = self.vida_max_jugador - self.vida_actual_jugador

            if curacion_teorica > vida_faltante:
                curacion_real = vida_faltante
            else:
                curacion_real = curacion_teorica

            self.vida_actual_jugador += curacion_real
            self.caja_registro_combate.insert(
                "end", f"\n> {nombre_pokemon} se ha curado {int(curacion_real)} HP.\n"
            )

        self.label_hp_jugador.configure(
            text=f"HP: {int(self.vida_actual_jugador)} / {self.vida_max_jugador}"
        )

        self.barra_vida_jugador.set(self.vida_actual_jugador / self.vida_max_jugador)
        self.caja_registro_combate.see("end")

        if self.vida_actual_enemigo > 0:
            self.label_estado_combate.configure(
                text="El enemigo está atacando...", text_color="#FBC02D"
            )
            self.after(1000, self.turno_enemigo)


class PokedexApp(kc.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("Pokédex")
        self.after(0, lambda: self.state("zoomed"))
        self.ventanasecundaria = None
        self.engine = sqlalchemy.create_engine("sqlite:///inventariopokemon.db")

     
        self.configure(fg_color="#D91414")

        self.titulo = kc.CTkLabel(
            self, text="🔴 POKÉDEX ⚪", font=("Roboto", 34, "bold"), text_color="white"
        )
        self.titulo.pack(pady=(30, 15))

        self.frame_buscador = kc.CTkFrame(self, fg_color="transparent")
        self.frame_buscador.pack(pady=5)

        self.entrada_pokemon = kc.CTkEntry(
            self.frame_buscador,
            placeholder_text="Nombre del Pokémon...",
            width=220,
            height=40,
            font=("Roboto", 14),
            fg_color="white",
            text_color="black",
        )
        self.entrada_pokemon.pack(side="left", padx=5)

        self.boton_buscar = kc.CTkButton(
            self.frame_buscador,
            text="🔍 Buscar",
            width=100,
            height=40,
            font=("Roboto", 14, "bold"),
            fg_color="#1976D2",
            hover_color="#1565C0",
            command=self.BuscarPokemon,
        )
        self.boton_buscar.pack(side="left", padx=5)

        self.boton_gacha = kc.CTkButton(
            self.frame_buscador,
            text="🎲 Sorpresa",
            width=120,
            height=40,
            font=("Roboto", 14, "bold"),
            fg_color="#FBC02D",
            text_color="black",
            hover_color="#F9A825",
            command=self.LanzarDados,
        )
        self.boton_gacha.pack(side="left", padx=5)

        self.botoninventario = kc.CTkButton(
            self.frame_buscador,
            text="Crear BD",
            width=100,
            height=40,
            font=("Roboto", 14, "bold"),
            fg_color="#7B1FA2",
            hover_color="#6A1B9A",
            command=self.crearinventario,
        )
        self.botoninventario.pack(side="left", padx=5)

        self.boton_ver_inv = kc.CTkButton(
            self.frame_buscador,
            text="Ver Caja",
            width=100,
            height=40,
            font=("Roboto", 14, "bold"),
            fg_color="#388E3C",
            hover_color="#2E7D32",
            command=self.MostrarInventario,
        )
        self.boton_ver_inv.pack(side="left", padx=5)

        self.botonIniciar = kc.CTkButton(
            self.frame_buscador,
            width=100,
            height=40,
            text="Iniciar combate",
            fg_color="#E0E0E0",
            text_color="black",
            hover_color="#BDBDBD",
            font=("Roboto", 12, "bold"),
            command=self.AbrirVentana,
        )
        self.botonIniciar.pack(side="left", padx=5)
        self.botonBorrarInventario = kc.CTkButton(
            self.frame_buscador,
            width=100,
            height=40,
            text="Borrar caja...",
            fg_color="#0BEA0E",
            text_color="black",
            hover_color="#033F07",
            font=("Roboto", 12, "bold"),
            command=self.borrarinventario,
        )
        self.botonBorrarInventario.pack(side="left", padx=5)

        self.pantalla = kc.CTkFrame(
            self,
            width=380,
            height=430,
            fg_color="#F0F0F0",
            corner_radius=15,
            border_width=4,
            border_color="#262626",
        )
        self.pantalla.pack(pady=15, padx=20)
        self.pantalla.pack_propagate(False)

        self.frame_imagen = kc.CTkFrame(
            self.pantalla,
            width=200,
            height=200,
            fg_color="white",
            corner_radius=10,
            border_width=2,
            border_color="#BDBDBD",
        )
        self.frame_imagen.pack(pady=(20, 10))
        self.frame_imagen.pack_propagate(False)

        self.label_imagen = kc.CTkLabel(
            self.frame_imagen,
            text="[ Imagen del Pokémon ]",
            width=200,
            height=200,
            text_color="gray",
        )
        self.label_imagen.pack()

        self.caja_datos = kc.CTkTextbox(
            self.pantalla,
            width=320,
            height=150,
            font=("Consolas", 16, "bold"),
            fg_color="#98D8A0",
            text_color="black",
            corner_radius=8,
            border_width=2,
            border_color="#262626",
        )
        self.caja_datos.pack(pady=10)
        self.caja_datos.insert(
            "0.0",
            "Esperando datos...\n\n- ID:\n- Nombre:\n- Altura:\n- Peso:\n- Tipo:\n- Rareza:\n- Vida:",
        )
        self.caja_datos.configure(state="disabled")

        self.boton_borrar = kc.CTkButton(
            self,
            text="Limpiar Pantalla",
            fg_color="#E0E0E0",
            text_color="black",
            hover_color="#BDBDBD",
            font=("Roboto", 12, "bold"),
            command=self.Borrar,
        )
        self.boton_borrar.pack(pady=(10, 15))

        self.caja_inventario = kc.CTkTextbox(
            self,
            width=750,
            height=220,
            font=("Consolas", 15),
            fg_color="#1E272E",
            text_color="#4BCFFA",
            corner_radius=10,
            border_width=3,
            border_color="#00A8FF",
        )
        self.caja_inventario.pack(pady=(0, 20))
        self.caja_inventario.insert("0.0", "Tu inventario aparecerá aquí...")
        self.caja_inventario.configure(state="disabled")

    def Borrar(self):
        self.entrada_pokemon.delete(0, "end")
        self.caja_datos.configure(state="normal")
        self.caja_datos.delete("0.0", "end")
        self.caja_datos.insert(
            "0.0",
            "Esperando datos...\n\n- ID:\n- Nombre:\n- Altura:\n- Peso:\n- Tipo:\n- Rareza:\n- Vida:",
        )
        self.label_imagen.configure(image="", text="[ Imagen del Pokémon ]")
        self.caja_datos.configure(state="disabled")

        self.caja_inventario.configure(state="normal")
        self.caja_inventario.delete("0.0", "end")
        self.caja_inventario.insert("0.0", "Tu inventario aparecerá aquí...")
        self.caja_inventario.configure(state="disabled")

    def borrarinventario(self):
        with self.engine.begin() as conexion:
            query = """
            DELETE FROM invepoke;
            """
            conexion.execute(sqlalchemy.text(query))

    def BuscarPokemon(self):
        Nombre_referencia = self.entrada_pokemon.get().lower()

        if Nombre_referencia:
            url = f"https://pokeapi.co/api/v2/pokemon/{Nombre_referencia}"
            respuesta = rq.get(url)

            if respuesta.status_code == 200:
                datos = respuesta.json()

                Nombre_pokemon = datos["name"]
                id_pokemon = datos["id"]
                typo_pokemon = datos["types"][0]["type"]["name"]

                altura_pokemon = datos["height"] / 10
                peso_pokemon = datos["weight"] / 10
                url_imagen = datos["sprites"]["other"]["home"]["front_default"]

                vida = datos["stats"][0]["base_stat"]
                ataque = datos["stats"][1]["base_stat"]

                url_especie = f"https://pokeapi.co/api/v2/pokemon-species/{id_pokemon}/"
                respuesta_especie = rq.get(url_especie)
                datos_especie = respuesta_especie.json()

                es_legendario = datos_especie["is_legendary"]
                es_mitico = datos_especie["is_mythical"]

                calidad = "Común"
                if es_legendario:
                    calidad = "⭐ LEGENDARIO ⭐"
                elif es_mitico:
                    calidad = "✨ MÍTICO ✨"

                info_pokedex = f"""
{Nombre_pokemon.upper()}
  
- ID: #{id_pokemon}
- Nombre: {Nombre_pokemon.capitalize()}
- Altura: {altura_pokemon} m
- Peso: {peso_pokemon} kg
- Tipo: {typo_pokemon.capitalize()}
- HP (Vida): {vida} ❤️
- Ataque: {ataque} ⚔️
- Calidad: {calidad}
"""
                self.caja_datos.configure(state="normal")
                self.caja_datos.delete("0.0", "end")
                self.caja_datos.insert("0.0", info_pokedex)
                self.caja_datos.configure(state="disabled")

                if url_imagen:
                    respuesta_img = rq.get(url_imagen)
                    imagen_pil = PIL.Image.open(io.BytesIO(respuesta_img.content))

                    mi_ctk_image = kc.CTkImage(
                        light_image=imagen_pil, dark_image=imagen_pil, size=(180, 180)
                    )

                    self.label_imagen.configure(image=mi_ctk_image, text="")
                    self.InsertarInventario(
                        id_pokemon,
                        Nombre_pokemon,
                        altura_pokemon,
                        peso_pokemon,
                        typo_pokemon,
                        ataque,
                        vida,
                    )

            elif respuesta.status_code == 404:
                self.caja_datos.configure(state="normal")
                self.caja_datos.delete("0.0", "end")
                self.caja_datos.insert("0.0", "\n  ❌ Pokémon no\n  encontrado.")
                self.caja_datos.configure(state="disabled")
                self.label_imagen.configure(image="", text="[ Sin datos ]")

    def LanzarDados(self):
        Numeroid = random.randint(1, 1025)
        url = f"https://pokeapi.co/api/v2/pokemon/{Numeroid}"

        respuesta = rq.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()

            Nombre_pokemon = datos["name"]
            id_pokemon = datos["id"]
            typo_pokemon = datos["types"][0]["type"]["name"]

            altura_pokemon = datos["height"] / 10
            peso_pokemon = datos["weight"] / 10
            url_imagen = datos["sprites"]["other"]["home"]["front_default"]

            vida = datos["stats"][0]["base_stat"]
            ataque = datos["stats"][1]["base_stat"]

            url_especie = f"https://pokeapi.co/api/v2/pokemon-species/{Numeroid}/"
            respuesta_especie = rq.get(url_especie)
            datos_especie = respuesta_especie.json()

            es_legendario = datos_especie["is_legendary"]
            es_mitico = datos_especie["is_mythical"]

            calidad = "Común"
            if es_legendario:
                calidad = "⭐ LEGENDARIO ⭐"
            elif es_mitico:
                calidad = "✨ MÍTICO ✨"

            info_pokedex = f"""
{Nombre_pokemon.upper()}
          
- ID: #{id_pokemon}
- Nombre: {Nombre_pokemon.capitalize()}
- Altura: {altura_pokemon} m
- Peso: {peso_pokemon} kg
- Tipo: {typo_pokemon.capitalize()}
- HP (Vida): {vida} ❤️
- Ataque: {ataque} ⚔️
- Calidad: {calidad} 
"""
            self.caja_datos.configure(state="normal")
            self.caja_datos.delete("0.0", "end")
            self.caja_datos.insert("0.0", info_pokedex)
            self.caja_datos.configure(state="disabled")

            if url_imagen:
                respuesta_img = rq.get(url_imagen)
                imagen_pil = PIL.Image.open(io.BytesIO(respuesta_img.content))

                mi_ctk_image = kc.CTkImage(
                    light_image=imagen_pil, dark_image=imagen_pil, size=(180, 180)
                )

                self.label_imagen.configure(image=mi_ctk_image, text="")
                self.InsertarInventario(
                    id_pokemon,
                    Nombre_pokemon,
                    altura_pokemon,
                    peso_pokemon,
                    typo_pokemon,
                    ataque,
                    vida,
                )

        elif respuesta.status_code == 404:
            self.caja_datos.configure(state="normal")
            self.caja_datos.delete("0.0", "end")
            self.caja_datos.insert("0.0", "\n  ❌ Pokémon no\n  encontrado.")
            self.caja_datos.configure(state="disabled")
            self.label_imagen.configure(image="", text="[ Sin datos ]")

    def crearinventario(self):
        with self.engine.begin() as conexion:
            conexion.execute(sqlalchemy.text("""
                                             CREATE TABLE IF NOT EXISTS invepoke(
                                                 id INTEGER PRIMARY KEY,
                                                 nombre_pokemon TEXT NOT NULL,
                                                 altura INTEGER NOT NULL,
                                                 peso INTEGER NOT NULL,
                                                 Tipo_pokemon TEXT NOT NULL,
                                                 ataque_pokemon INTEGER NOT NULL,
                                                 vida_pokemon INTEGER NOT NULL
                                             );
                                             """))

    def InsertarInventario(self, id, nombrep, altura, peso, tipo_pokemon, cp, hp):
        with self.engine.connect() as conexion:
            query = """
            INSERT INTO invepoke(id,nombre_pokemon,altura,peso,Tipo_pokemon,ataque_pokemon,vida_pokemon)
            VALUES(:ID,:Nombre,:Altura,:Peso,:Tipo_pokemon,:cp,:hp);
            """
            conexion.execute(
                sqlalchemy.text(query),
                {
                    "ID": id,
                    "Nombre": nombrep,
                    "Altura": altura,
                    "Peso": peso,
                    "Tipo_pokemon": tipo_pokemon,
                    "cp": cp,
                    "hp": hp,
                },
            )
            conexion.commit()

    def MostrarInventario(self):
        with self.engine.begin() as conexion:
            query = "SELECT * FROM invepoke ORDER BY id ASC"
            resultado = conexion.execute(sqlalchemy.text(query))
            MostrarResultado = resultado.fetchall()

        self.caja_inventario.configure(state="normal")
        self.caja_inventario.delete("0.0", "end")

        if not MostrarResultado:
            self.caja_inventario.insert("0.0", "Aún no has capturado ningún Pokémon.")
        else:
            self.caja_inventario.insert("end", "🏆 TU COLECCIÓN POKÉMON 🏆\n")
            self.caja_inventario.insert(
                "end",
                "─────────────────────────────────────────────────────────────────────────\n",
            )

            for dato in MostrarResultado:
                id_pokemon, nombre, altura, peso, tipo, ataque, vida = dato
                linea_formateada = f"#{id_pokemon:03d} | 🟢 {nombre.capitalize():<12} | ❤️ HP: {vida:<4} | ⚔️ Ataque: {ataque:<4} | 🧬 {tipo.capitalize():<10} | 📏 {altura}m\n"
                self.caja_inventario.insert("end", linea_formateada)

        self.caja_inventario.configure(state="disabled")
        return MostrarResultado

    def AbrirVentana(self):
        if self.ventanasecundaria is None or not self.ventanasecundaria.winfo_exists():
            self.ventanasecundaria = ventanacombate(self)
        else:
            self.ventanasecundaria.focus()


if __name__ == "__main__":
    app = PokedexApp()
    app.mainloop()
