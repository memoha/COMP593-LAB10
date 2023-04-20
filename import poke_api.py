import poke_api
import requests
import image_lib
from tkinter import *
from tkinter import ttk
import os
import ctypes

# Get the path of the script and its parent directory
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cache_dir = os.path.join(script_dir, 'images')

if not os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir)

#Create the main window
root = Tk()
root.title("Pokemon image viewer")
root.minsize(600, 700)

# Set the window icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.Pokemonimageviewer')
icon_path = os.path.join(script_dir , 'Poke-Ball.ico')
root.iconbitmap(icon_path)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Create the Frame
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

#Add the image to Frame
img_pokemon = PhotoImage(file=os.path.join(script_dir, 'logo1.png'))
lbl_pokemon_img = ttk.Label(frame, image=img_pokemon)
lbl_pokemon_img.grid(row=0, column=0)

pokemon_names = poke_api.get_pokemon_names()
cbox_pokemon_names = ttk.Combobox(frame, values=pokemon_names, state='readonly')
cbox_pokemon_names.set("Select a Pokemon")
cbox_pokemon_names.grid(row=1, column=0, padx=10, pady=10)

def handle_pokemon_selection(event):
    pokemon_name = cbox_pokemon_names.get()

    image_path = poke_api.download_pokemon_image(pokemon_name, image_cache_dir)

    if image_path is not None:
        img_pokemon['file'] = image_path
    
cbox_pokemon_names.bind('<<ComoboboxSelected>>', handle_pokemon_selection)

btn_set_wallpaper = ttk.Button(frame, text='Set as Desktop Wallpaper')
btn_set_wallpaper.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()