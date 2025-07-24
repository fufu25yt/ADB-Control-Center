import tkinter as tk
from PIL import Image, ImageTk
import time
import os
import subprocess
import sys

def run_splash_and_app(splash_image_path, app_script_path, 
                       splash_duration_seconds=3,
                       target_splash_size=(400, 300), # Nouvelle taille cible (largeur, hauteur)
                       fade_steps=20, # Nombre d'étapes pour le fondu
                       fade_interval_ms=20, # Intervalle entre les étapes de fondu en ms
                       pulse_strength=0.05, # Force de l'animation de pulsation (5% de zoom)
                       pulse_steps=10 # Nombre d'étapes pour la pulsation
                      ):
    """
    Affiche un écran de démarrage redimensionné avec des effets de fondu et de pulsation,
    puis lance l'application principale.

    Args:
        splash_image_path (str): Chemin vers le fichier image de l'écran de démarrage.
        app_script_path (str): Chemin vers le script Python de l'application principale (app.py).
        splash_duration_seconds (int): Durée totale d'affichage de l'écran de démarrage en secondes.
        target_splash_size (tuple): Tuple (largeur, hauteur) pour redimensionner l'image.
        fade_steps (int): Nombre d'étapes pour les effets de fondu (plus il y en a, plus c'est fluide).
        fade_interval_ms (int): Délai en millisecondes entre chaque étape de fondu.
        pulse_strength (float): Pourcentage de zoom pour l'effet de pulsation (ex: 0.05 pour 5%).
        pulse_steps (int): Nombre d'étapes pour l'animation de pulsation.
    """
    
    splash_root = tk.Tk()
    splash_root.withdraw() 
    
    splash_window = tk.Toplevel(splash_root)
    splash_window.overrideredirect(True)
    splash_window.attributes("-alpha", 0.0) # Commence complètement transparent pour le fondu
    
    original_image = None
    photo_image = None
    
    try:
        original_image = Image.open(splash_image_path)
        
        # Redimensionner l'image
        original_image = original_image.resize(target_splash_size, Image.LANCZOS)
        
        # Centrer la fenêtre splash
        img_width, img_height = original_image.size
        screen_width = splash_window.winfo_screenwidth()
        screen_height = splash_window.winfo_screenheight()
        
        x = (screen_width // 2) - (img_width // 2)
        y = (screen_height // 2) - (img_height // 2)
        
        splash_window.geometry(f'{img_width}x{img_height}+{x}+{y}')
        
        # Afficher l'image dans un label
        splash_label = tk.Label(splash_window, bg="white")
        splash_label.pack(expand=True, fill="both")

        # --- Fonctions d'animation ---
        def fade_in():
            alpha = splash_window.attributes("-alpha")
            if alpha < 1.0:
                alpha += (1.0 / fade_steps)
                splash_window.attributes("-alpha", alpha)
                splash_window.after(fade_interval_ms, fade_in)
            else:
                # Une fois le fondu terminé, lancez la pulsation
                splash_window.after(100, pulse_animation) # Petit délai avant de pulser

        def fade_out():
            alpha = splash_window.attributes("-alpha")
            if alpha > 0.0:
                alpha -= (1.0 / fade_steps)
                splash_window.attributes("-alpha", alpha)
                splash_window.after(fade_interval_ms, fade_out)
            else:
                splash_window.destroy()
                splash_root.destroy()
        
        def update_image(img_pil):
            nonlocal photo_image
            photo_image = ImageTk.PhotoImage(img_pil)
            splash_label.config(image=photo_image)
            splash_label.image = photo_image # Important pour éviter la suppression par le garbage collector
            splash_window.update_idletasks() # Met à jour immédiatement

        def pulse_animation(step=0, direction=1):
            if not splash_window.winfo_exists(): # Arrêter si la fenêtre est fermée
                return

            # Calculer le facteur de zoom
            zoom_factor_base = 1.0
            zoom_change_per_step = (pulse_strength / pulse_steps) * direction
            current_zoom = zoom_factor_base + (step * zoom_change_per_step)

            # Appliquer le zoom
            new_width = int(img_width * current_zoom)
            new_height = int(img_height * current_zoom)
            
            # Limiter pour éviter un zoom excessif ou trop petit
            if new_width < target_splash_size[0] * (1 - pulse_strength) or new_width > target_splash_size[0] * (1 + pulse_strength):
                direction *= -1 # Inverser la direction
                step += direction # Ajuster l'étape pour le prochain cycle

            resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
            update_image(resized_image)

            # Recentre la fenêtre après le zoom (nécessaire si la taille change)
            current_x = (screen_width // 2) - (new_width // 2)
            current_y = (screen_height // 2) - (new_height // 2)
            splash_window.geometry(f'{new_width}x{new_height}+{current_x}+{current_y}')

            step += direction
            if step > pulse_steps or step < 0: # S'assurer que l'étape reste dans les limites
                direction *= -1
                step += direction * 2 # Ajustement pour le rebond
                
            # Planifier la prochaine étape de l'animation
            # La durée totale des effets est prise en compte ici pour coordonner
            splash_window.after(max(1, int((splash_duration_seconds * 1000 - (fade_steps * fade_interval_ms * 2)) / (pulse_steps * 2))), pulse_animation, step, direction)
        
        # Lancer le fondu d'entrée
        splash_root.after(100, fade_in) # Petit délai initial

        # Planifier la fermeture de la fenêtre splash et le lancement de l'application
        # La durée totale inclut le fondu et l'animation.
        splash_root.after(int(splash_duration_seconds * 1000), fade_out)
        splash_root.after(int(splash_duration_seconds * 1000) + (fade_steps * fade_interval_ms), lambda: launch_main_app(app_script_path))

        splash_root.mainloop()

    except FileNotFoundError:
        print(f"Erreur: L'image d'écran de démarrage '{splash_image_path}' est introuvable.")
        launch_main_app(app_script_path) # Lancer l'appli même si le splash échoue
    except Exception as e:
        print(f"Erreur lors du chargement ou de l'affichage de l'écran de démarrage avec effets: {e}")
        launch_main_app(app_script_path) # Lancer l'appli même si le splash échoue

def launch_main_app(app_script_path):
    """Lance l'application principale."""
    try:
        python_executable = sys.executable
        subprocess.Popen([python_executable, app_script_path])
    except FileNotFoundError:
        print(f"Erreur: L'interpréteur Python ou le script '{app_script_path}' est introuvable.")
    except Exception as e:
        print(f"Erreur lors du lancement de l'application principale: {e}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder = "data"
    
    splash_path = os.path.join(current_dir, data_folder, "splash.png")
    app_path = os.path.join(current_dir, data_folder, "app.py")
    
    run_splash_and_app(splash_path, app_path, splash_duration_seconds=3.5) # Durée légèrement augmentée pour les animations
