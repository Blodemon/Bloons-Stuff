import os
import re
import pyautogui
import time
from pynput.keyboard import Controller, Key
import pytesseract
from PIL import Image
import PIL.Image
import cv2
import functions as fu
import maps
import customtkinter
import bonus_image



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("250x950")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Select", font=('arial',25))
label.pack(pady=12, padx=10)

button_dd = customtkinter.CTkButton(master=frame, text="Dark Dungons", command=maps.dark_dungons)
button_dd.pack(pady=12, padx=10)
button_sanctuary = customtkinter.CTkButton(master=frame, text="Sanctuary", command=maps.heli_Sanctuary)
button_sanctuary.pack(pady=12, padx=10)
button_ravine = customtkinter.CTkButton(master=frame, text="Ravine", command=maps.ravine)
button_ravine.pack(pady=12, padx=10)
button_flood = customtkinter.CTkButton(master=frame, text="Flooded Valley", command=maps.flooded_valleey)
button_flood.pack(pady=12, padx=10)
button_infernal = customtkinter.CTkButton(master=frame, text="Infernal", command=maps.infernal)
button_infernal.pack(pady=12, padx=10)
button_bloody = customtkinter.CTkButton(master=frame, text="Bloody Puddles", command=maps.bloody_puddles)
button_bloody.pack(pady=12, padx=10)
button_work = customtkinter.CTkButton(master=frame, text="Workshop", command=maps.workshop)
button_work.pack(pady=12, padx=10)
button_quad = customtkinter.CTkButton(master=frame, text="Quad", command=maps.quad)
button_quad.pack(pady=12, padx=10)
button_dc = customtkinter.CTkButton(master=frame, text="Dark Castle", command=maps.dark_castle)
button_dc.pack(pady=12, padx=10)
button_muddy = customtkinter.CTkButton(master=frame, text="Muddy Puddles", command=maps.muddy_puddles)
button_muddy.pack(pady=12, padx=10)
button_ouch = customtkinter.CTkButton(master=frame, text="#Ouch", command=maps.ouch)
button_ouch.pack(pady=12, padx=10)

Auoplay = customtkinter.CTkLabel(master=frame, text="Autoplay", font=('arial',25)).pack(pady=12, padx=10)
global rounds
rounds = customtkinter.CTkEntry(master=frame, placeholder_text="Rounds to play")
rounds.pack(pady=12, padx=10)

button_auto = customtkinter.CTkButton(master=frame, text="auto", command=lambda: fu.start_autopaly(rounds.get())).pack(pady=12, padx=10)


    
root.mainloop()

