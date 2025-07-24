import customtkinter as ctk
from tkinter import filedialog, simpledialog
import subprocess
import os
import threading
import datetime
import webbrowser
import time

# =================================================================================
# SECTION: CONFIGURATION DU LANGAGE (Internationalization - i18n)
# =================================================================================
LANGUAGES = {
    "fr": {
        "window_title": "ADB Control Center",
        "tab_device": "Appareil & Connexion",
        "tab_apps": "Gestion des Apps",
        "tab_utilities": "Utilitaires",
        "tab_advanced": "Commandes Avancées",
        "tab_about": "À Propos",
        "connected_device": "Appareil Connecté :",
        "no_device": "Aucun appareil",
        "refresh": "Rafraîchir",
        "get_detailed_info": "Obtenir les Informations Détaillées de l'Appareil",
        "wireless_connection": "Connexion sans fil :",
        "enter_ip": "Entrez l'adresse IP de l'appareil",
        "connect": "Connecter",
        "list_user_apps": "Lister Apps Utilisateur",
        "list_system_apps": "Lister Apps Système",
        "installed_apps": "Applications Installées",
        "app_package_placeholder": "Cliquez sur une app dans la liste pour remplir son nom de package ici",
        "uninstall": "Désinstaller",
        "clear_data": "Vider les données",
        "extract_apk": "Extraire l'APK",
        "install_apk": "Installer un APK",
        "force_stop": "Forcer l'arrêt",
        "launch_scrcpy": "Lancer Scrcpy (miroir de l'écran)",
        "scrcpy_not_found": "Erreur: 'scrcpy' introuvable. Assurez-vous qu'il est installé et dans votre PATH.",
        "open_url_on_device": "Ouvrir une URL sur l'appareil :",
        "send_text_to_device": "Envoyer du texte à l'appareil :",
        "send": "Envoyer",
        "reboot_device": "Redémarrer l'Appareil",
        "reboot_recovery": "Redémarrer en Mode Recovery",
        "reboot_bootloader": "Redémarrer en Mode Bootloader",
        "take_screenshot": "Prendre une Capture d'écran (sur le bureau)",
        "created_by": "Créé par : fufu",
        "version": "Version: 2.0",
        "log_searching_devices": "Recherche des appareils...",
        "log_error": "Erreur:",
        "log_no_authorized_device": "Aucun appareil autorisé trouvé.",
        "log_devices_found": "Appareils trouvés:",
        "log_device_selected": "Appareil '{device}' sélectionné.",
        "uninstall_confirm_title": "Confirmation de désinstallation",
        "uninstall_confirm_text": "Êtes-vous sûr de vouloir désinstaller '{package}' ?\nTapez 'oui' pour confirmer.",
        "uninstall_cancelled": "Désinstallation annulée.",
        "push_file_folder": "Pousser (Push) Fichier/Dossier",
        "pull_file_folder": "Tirer (Pull) Fichier/Dossier",
        "path_on_device": "Chemin sur l'appareil :",
        "local_path": "Chemin local :",
        "browse": "Parcourir...",
        "list_dir_content": "Lister le contenu d'un dossier",
        "delete_file_folder": "Supprimer Fichier/Dossier",
        "create_folder": "Créer Dossier",
        "enter_device_path": "Entrez le chemin sur l'appareil (ex: /sdcard/mon_dossier)",
        "enter_local_path": "Entrez le chemin local (ex: C:\\Users\\MonUser\\Downloads)",
        "enter_file_or_dir_to_delete": "Entrez le chemin du fichier ou dossier à supprimer sur l'appareil",
        "enter_folder_to_create": "Entrez le chemin du dossier à créer sur l'appareil",
        "delete_confirm": "Êtes-vous sûr de vouloir supprimer '{path}' de l'appareil ?\nTapez 'oui' pour confirmer.",
        "delete_cancelled": "Suppression annulée.",
        "sim_key_event": "Simuler une touche/un swipe",
        "key_event_type": "Type d'événement :",
        "key_event_value": "Valeur (code touche ou coords x1 y1 x2 y2) :",
        "send_event": "Envoyer Événement",
        "key_home": "ACCUEIL", "key_back": "RETOUR", "key_power": "MARCHE/ARRÊT", "key_volume_up": "VOLUME_HAUT", "key_volume_down": "VOLUME_BAS", "key_menu": "MENU",
        "swipe_example": "Ex: 100 500 100 200 (swipe vertical)",
        "toggle_wifi": "Basculer Wi-Fi",
        "toggle_mobile_data": "Basculer Données Mobiles",
        "toggle_airplane_mode": "Basculer Mode Avion",
        "toggle_dev_options": "Basculer Mode Développeur",
        "get_logcat": "Obtenir les Logs du Système (logcat)",
        "get_accounts": "Obtenir la liste des comptes",
        "get_app_permissions": "Obtenir les permissions d'une app",
        "list_running_processes": "Lister les processus en cours",
        "kill_process": "Tuer un processus",
        "process_id_or_name": "ID du processus ou Nom :",
        "kill": "Tuer",
        "wifi_on": "Wi-Fi activé.",
        "wifi_off": "Wi-Fi désactivé.",
        "mobile_data_on": "Données mobiles activées.",
        "mobile_data_off": "Données mobiles désactivées.",
        "airplane_mode_on": "Mode avion activé.",
        "airplane_mode_off": "Mode avion désactivé.",
        "dev_options_on": "Mode développeur activé.",
        "dev_options_off": "Mode développeur désactivé.",
        "logcat_saved": "Logs sauvegardés dans '{path}'",
        "accounts_list": "Comptes sur l'appareil :",
        "no_accounts": "Aucun compte trouvé.",
        "permissions_for": "Permissions pour '{package}' :",
        "no_permissions_found": "Aucune permission trouvée pour '{package}'.",
        "processes_list": "Processus en cours :",
        "process_killed": "Processus '{process}' terminé.",
        "kill_failed": "Échec de la terminaison du processus '{process}'.",
        "push_success": "Fichier/dossier '{source}' poussé vers '{dest}' avec succès.",
        "pull_success": "Fichier/dossier '{source}' tiré vers '{dest}' avec succès.",
        "list_dir_empty": "Dossier vide ou introuvable.",
        "file_dir_deleted": "Fichier/dossier '{path}' supprimé avec succès.",
        "folder_created": "Dossier '{path}' créé avec succès.",
        "path_required": "Un chemin sur l'appareil est requis.",
        "local_path_required": "Un chemin local est requis.",
        "select_file_or_folder": "Veuillez sélectionner un fichier ou un dossier local.",
        "source_dest_required": "Chemin source et destination requis.",
        "select_destination_folder": "Sélectionnez un dossier de destination",
        "screenshot_saved": "Capture d'écran sauvegardée sur votre bureau: {path}",
        # Nouveaux titres pour les cadres
        "file_transfer_title": "Transfert de Fichiers",
        "file_mgt_title": "Gestion Fichiers/Dossiers (Appareil)",
        "sim_key_event_title": "Simuler Événement Touche/Swipe",
        "device_control_title": "Contrôle de l'Appareil",
        "info_adv_title": "Informations Avancées",
        "process_mgt_title": "Gestion des Processus",
    },
    "en": {
        "window_title": "ADB Control Center",
        "tab_device": "Device & Connection",
        "tab_apps": "App Management",
        "tab_utilities": "Utilities",
        "tab_advanced": "Advanced Commands",
        "tab_about": "About",
        "connected_device": "Connected Device:",
        "no_device": "No device",
        "refresh": "Refresh",
        "get_detailed_info": "Get Detailed Device Information",
        "wireless_connection": "Wireless Connection:",
        "enter_ip": "Enter the device's IP address",
        "connect": "Connect",
        "list_user_apps": "List User Apps",
        "list_system_apps": "List System Apps",
        "installed_apps": "Installed Applications",
        "app_package_placeholder": "Click an app in the list to fill its package name here",
        "uninstall": "Uninstall",
        "clear_data": "Clear Data",
        "extract_apk": "Extract APK",
        "install_apk": "Install APK",
        "force_stop": "Force Stop",
        "launch_scrcpy": "Launch Scrcpy (Screen Mirroring)",
        "scrcpy_not_found": "Error: 'scrcpy' not found. Make sure it is installed and in your PATH.",
        "open_url_on_device": "Open URL on device:",
        "send_text_to_device": "Send text to device:",
        "send": "Send",
        "reboot_device": "Reboot Device",
        "reboot_recovery": "Reboot to Recovery Mode",
        "reboot_bootloader": "Reboot to Bootloader Mode",
        "take_screenshot": "Take a Screenshot (to Desktop)",
        "created_by": "Created by: fufu",
        "version": "Version: 2.0",
        "log_searching_devices": "Searching for devices...",
        "log_error": "Error:",
        "log_no_authorized_device": "No authorized device found.",
        "log_devices_found": "Devices found:",
        "log_device_selected": "Device '{device}' selected.",
        "uninstall_confirm_title": "Uninstall Confirmation",
        "uninstall_confirm_text": "Are you sure you want to uninstall '{package}'?\nType 'yes' to confirm.",
        "uninstall_cancelled": "Uninstall cancelled.",
        "push_file_folder": "Push File/Folder",
        "pull_file_folder": "Pull File/Folder",
        "path_on_device": "Path on Device :",
        "local_path": "Local Path :",
        "browse": "Browse...",
        "list_dir_content": "List Directory Content",
        "delete_file_folder": "Delete File/Folder",
        "create_folder": "Create Folder",
        "enter_device_path": "Enter device path (ex: /sdcard/my_folder)",
        "enter_local_path": "Enter local path (ex: C:\\Users\\MyUser\\Downloads)",
        "enter_file_or_dir_to_delete": "Enter path of file or folder to delete on device",
        "enter_folder_to_create": "Enter path of folder to create on device",
        "delete_confirm": "Are you sure you want to delete '{path}' from the device?\nType 'yes' to confirm.",
        "delete_cancelled": "Deletion cancelled.",
        "sim_key_event": "Simulate Key/Swipe Event",
        "key_event_type": "Event Type :",
        "key_event_value": "Value (key code or x1 y1 x2 y2 coords) :",
        "send_event": "Send Event",
        "key_home": "HOME", "key_back": "BACK", "key_power": "POWER", "key_volume_up": "VOLUME_UP", "key_volume_down": "VOLUME_DOWN", "key_menu": "MENU",
        "swipe_example": "Ex: 100 500 100 200 (vertical swipe)",
        "toggle_wifi": "Toggle Wi-Fi",
        "toggle_mobile_data": "Toggle Mobile Data",
        "toggle_airplane_mode": "Toggle Airplane Mode",
        "toggle_dev_options": "Toggle Developer Options",
        "get_logcat": "Get System Logs (logcat)",
        "get_accounts": "Get Accounts List",
        "get_app_permissions": "Get App Permissions",
        "list_running_processes": "List Running Processes",
        "kill_process": "Kill Process",
        "process_id_or_name": "Process ID or Name :",
        "kill": "Kill",
        "wifi_on": "Wi-Fi turned on.",
        "wifi_off": "Wi-Fi turned off.",
        "mobile_data_on": "Mobile data turned on.",
        "mobile_data_off": "Mobile data turned off.",
        "airplane_mode_on": "Airplane mode turned on.",
        "airplane_mode_off": "Airplane mode turned off.",
        "dev_options_on": "Developer options turned on.",
        "dev_options_off": "Developer options turned off.",
        "logcat_saved": "Logs saved to '{path}'",
        "accounts_list": "Accounts on device :",
        "no_accounts": "No accounts found.",
        "permissions_for": "Permissions for '{package}' :",
        "no_permissions_found": "No permissions found for '{package}'.",
        "processes_list": "Running Processes :",
        "process_killed": "Process '{process}' killed.",
        "kill_failed": "Failed to kill process '{process}'.",
        "push_success": "File/folder '{source}' pushed to '{dest}' successfully.",
        "pull_success": "File/folder '{source}' pulled to '{dest}' successfully.",
        "list_dir_empty": "Directory empty or not found.",
        "file_dir_deleted": "File/folder '{path}' deleted successfully.",
        "folder_created": "Folder '{path}' created successfully.",
        "path_required": "A device path is required.",
        "local_path_required": "A local path is required.",
        "select_file_or_folder": "Please select a local file or folder.",
        "source_dest_required": "Source and destination paths are required.",
        "select_destination_folder": "Select Destination Folder",
        "screenshot_saved": "Screenshot saved to your desktop: {path}",
        # New frame titles
        "file_transfer_title": "File Transfer",
        "file_mgt_title": "File/Folder Management (Device)",
        "sim_key_event_title": "Simulate Key/Swipe Event",
        "device_control_title": "Device Control",
        "info_adv_title": "Advanced Information",
        "process_mgt_title": "Process Management",
    }
}

class AdbControlCenter(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.current_lang = "fr"  # Langue par défaut

        # --- Variables d'état ---
        self.selected_device = None
        self.devices_list = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.title(self.get_string("window_title"))
        self.geometry("1000x800")

        # --- Création des onglets ---
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Create tabs directly with their translated names to avoid initial '...' duplicate error
        self.tab_device = self.tab_view.add(self.get_string("tab_device"))
        self.tab_apps = self.tab_view.add(self.get_string("tab_apps"))
        self.tab_utilities = self.tab_view.add(self.get_string("tab_utilities"))
        self.tab_advanced = self.tab_view.add(self.get_string("tab_advanced"))
        self.tab_about = self.tab_view.add(self.get_string("tab_about"))

        # --- Zone de Log partagée ---
        self.log_textbox = ctk.CTkTextbox(self, height=150, wrap="word", font=("Courier New", 12))
        self.log_textbox.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # --- Peupler chaque onglet ---
        self.create_device_tab()
        self.create_apps_tab()
        self.create_utilities_tab()
        self.create_advanced_tab()
        self.create_about_tab()
        
        # Update other UI text elements after creating them
        self.update_ui_text() 
        
        # --- Rafraîchir la liste des appareils au démarrage ---
        self.refresh_devices()
        
    def get_string(self, key):
        """Récupère une chaîne de caractères dans la langue actuelle."""
        return LANGUAGES[self.current_lang].get(key, key)

    def update_ui_text(self):
        """Met à jour tout le texte de l'UI avec la langue sélectionnée."""
        self.title(self.get_string("window_title"))
        
        # Define the list of tab widgets
        tab_widgets = [
            self.tab_device, self.tab_apps, self.tab_utilities, 
            self.tab_advanced, self.tab_about
        ]

        # Get the new translated names
        new_tab_strings = [
            self.get_string("tab_device"), 
            self.get_string("tab_apps"), 
            self.get_string("tab_utilities"),
            self.get_string("tab_advanced"), 
            self.get_string("tab_about")
        ]

        # Iterate through the tabs and rename ONLY if the name has changed
        for i, tab_widget in enumerate(tab_widgets):
            current_tab_name = tab_widget._name # Get the current internal name of the tab
            desired_new_name = new_tab_strings[i]

            if current_tab_name != desired_new_name:
                try:
                    self.tab_view.rename(current_tab_name, desired_new_name)
                    # Update the internal _name attribute after successful rename
                    tab_widget._name = desired_new_name 
                except ValueError as e:
                    # This should ideally not happen with the check, but good for debugging
                    self.log(f"Error renaming tab '{current_tab_name}' to '{desired_new_name}': {e}")
            # If names are the same, do nothing to avoid the ValueError

        # --- Update other UI elements ---
        # Onglet Appareil
        self.label_connected_device.configure(text=self.get_string("connected_device"))
        self.btn_refresh_devices.configure(text=self.get_string("refresh"))
        self.btn_get_info.configure(text=self.get_string("get_detailed_info"))
        self.label_wireless_connection.configure(text=self.get_string("wireless_connection"))
        self.wifi_ip_entry.configure(placeholder_text=self.get_string("enter_ip"))
        self.btn_connect_wifi.configure(text=self.get_string("connect"))
        
        # Onglet Apps
        self.btn_list_apps_user.configure(text=self.get_string("list_user_apps"))
        self.btn_list_apps_system.configure(text=self.get_string("list_system_apps"))
        self.app_list_frame.configure(label_text=self.get_string("installed_apps"))
        self.app_package_entry.configure(placeholder_text=self.get_string("app_package_placeholder"))
        self.btn_uninstall.configure(text=self.get_string("uninstall"))
        self.btn_clear_data.configure(text=self.get_string("clear_data"))
        self.btn_extract_apk.configure(text=self.get_string("extract_apk"))

        # Onglet Utilitaires
        self.btn_install_apk.configure(text=self.get_string("install_apk"))
        self.btn_force_stop.configure(text=self.get_string("force_stop"))
        self.btn_launch_scrcpy.configure(text=self.get_string("launch_scrcpy"))
        self.label_open_url.configure(text=self.get_string("open_url_on_device"))
        self.btn_open_url.configure(text=self.get_string("send"))
        self.label_send_text.configure(text=self.get_string("send_text_to_device"))
        self.btn_send_text.configure(text=self.get_string("send"))
        
        # Nouvelles fonctionnalités utilitaires - titres des cadres
        self.file_transfer_frame_label.configure(text=self.get_string("file_transfer_title"))
        self.label_device_path.configure(text=self.get_string("path_on_device"))
        self.device_path_entry.configure(placeholder_text=self.get_string("enter_device_path"))
        self.label_local_path.configure(text=self.get_string("local_path"))
        self.local_path_entry.configure(placeholder_text=self.get_string("enter_local_path"))
        self.btn_browse_local_path.configure(text=self.get_string("browse"))
        self.btn_push.configure(text=self.get_string("push_file_folder"))
        self.btn_pull.configure(text=self.get_string("pull_file_folder"))
        
        self.file_mgt_frame_label.configure(text=self.get_string("file_mgt_title"))
        self.btn_list_dir_content.configure(text=self.get_string("list_dir_content"))
        self.btn_delete_file_folder.configure(text=self.get_string("delete_file_folder"))
        self.btn_create_folder.configure(text=self.get_string("create_folder"))

        self.input_event_frame_label.configure(text=self.get_string("sim_key_event_title"))
        self.label_key_event_type.configure(text=self.get_string("key_event_type"))
        self.key_event_menu.configure(values=[
            self.get_string("key_home"), self.get_string("key_back"), 
            self.get_string("key_power"), self.get_string("key_volume_up"), 
            self.get_string("key_volume_down"), self.get_string("key_menu")
        ])
        self.label_key_event_value.configure(text=self.get_string("key_event_value"))
        self.key_event_value_entry.configure(placeholder_text=self.get_string("swipe_example"))
        self.btn_send_event.configure(text=self.get_string("send_event"))

        self.device_control_frame_label.configure(text=self.get_string("device_control_title"))
        self.btn_toggle_wifi.configure(text=self.get_string("toggle_wifi"))
        self.btn_toggle_mobile_data.configure(text=self.get_string("toggle_mobile_data"))
        self.btn_toggle_airplane_mode.configure(text=self.get_string("toggle_airplane_mode"))
        self.btn_toggle_dev_options.configure(text=self.get_string("toggle_dev_options"))

        # Onglet Avancé (mise à jour pour les nouvelles fonctions ici)
        self.btn_reboot.configure(text=self.get_string("reboot_device"))
        self.btn_reboot_recovery.configure(text=self.get_string("reboot_recovery"))
        self.btn_reboot_bootloader.configure(text=self.get_string("reboot_bootloader"))
        self.btn_screenshot.configure(text=self.get_string("take_screenshot"))
        
        self.info_adv_frame_label.configure(text=self.get_string("info_adv_title"))
        self.btn_get_logcat.configure(text=self.get_string("get_logcat"))
        self.btn_get_accounts.configure(text=self.get_string("get_accounts"))
        self.btn_get_app_permissions.configure(text=self.get_string("get_app_permissions"))
        
        self.process_mgt_frame_label.configure(text=self.get_string("process_mgt_title"))
        self.btn_list_running_processes.configure(text=self.get_string("list_running_processes"))
        self.label_process_id_name.configure(text=self.get_string("process_id_or_name"))
        self.process_entry.configure(placeholder_text=self.get_string("process_id_or_name"))
        self.btn_kill_process.configure(text=self.get_string("kill"))


        # Onglet À Propos
        self.label_created_by.configure(text=self.get_string("created_by"))
        self.label_version.configure(text=self.get_string("version"))
        # Le message de prévention sera configuré plus tard

    def switch_language(self, lang):
        self.current_lang = lang
        self.update_ui_text()
        
    def open_link(self, url):
        webbrowser.open_new(url)
        
    # =================================================================================
    # SECTION: CRÉATION DES INTERFACES (ONGLETS)
    # =================================================================================
    def create_device_tab(self):
        self.tab_device.grid_columnconfigure(0, weight=1)
        conn_frame = ctk.CTkFrame(self.tab_device)
        conn_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        conn_frame.grid_columnconfigure(1, weight=1)
        self.label_connected_device = ctk.CTkLabel(conn_frame, text="")
        self.label_connected_device.grid(row=0, column=0, padx=10, pady=10)
        self.device_menu = ctk.CTkOptionMenu(conn_frame, values=[""], command=self.on_device_select)
        self.device_menu.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.btn_refresh_devices = ctk.CTkButton(conn_frame, text="", width=100, command=self.refresh_devices)
        self.btn_refresh_devices.grid(row=0, column=2, padx=10, pady=10)
        info_frame = ctk.CTkFrame(self.tab_device)
        info_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        info_frame.grid_columnconfigure(0, weight=1)
        self.btn_get_info = ctk.CTkButton(info_frame, text="", command=self.get_device_info)
        self.btn_get_info.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        wifi_frame = ctk.CTkFrame(self.tab_device, fg_color="transparent")
        wifi_frame.grid(row=2, column=0, padx=10, pady=20, sticky="ew")
        wifi_frame.grid_columnconfigure(1, weight=1)
        self.label_wireless_connection = ctk.CTkLabel(wifi_frame, text="")
        self.label_wireless_connection.grid(row=0, column=0)
        self.wifi_ip_entry = ctk.CTkEntry(wifi_frame, placeholder_text="")
        self.wifi_ip_entry.grid(row=0, column=1, padx=10, sticky="ew")
        self.btn_connect_wifi = ctk.CTkButton(wifi_frame, text="", width=100, command=self.connect_wifi)
        self.btn_connect_wifi.grid(row=0, column=2, padx=10)

    def create_apps_tab(self):
        self.tab_apps.grid_columnconfigure(0, weight=1)
        self.tab_apps.grid_rowconfigure(1, weight=1)
        app_control_frame = ctk.CTkFrame(self.tab_apps)
        app_control_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.btn_list_apps_user = ctk.CTkButton(app_control_frame, text="", command=lambda: self.list_apps(mode="user"))
        self.btn_list_apps_user.pack(side="left", padx=5, pady=5)
        self.btn_list_apps_system = ctk.CTkButton(app_control_frame, text="", command=lambda: self.list_apps(mode="system"))
        self.btn_list_apps_system.pack(side="left", padx=5, pady=5)
        self.progress_bar = ctk.CTkProgressBar(app_control_frame, orientation="horizontal")
        self.progress_bar.pack(side="left", fill="x", expand=True, padx=10, pady=5)
        self.progress_bar.set(0)
        self.app_list_frame = ctk.CTkScrollableFrame(self.tab_apps, label_text="")
        self.app_list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        app_action_frame = ctk.CTkFrame(self.tab_apps)
        app_action_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        app_action_frame.grid_columnconfigure(0, weight=1)
        self.app_package_entry = ctk.CTkEntry(app_action_frame, placeholder_text="")
        self.app_package_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.btn_uninstall = ctk.CTkButton(app_action_frame, text="", command=self.uninstall_app)
        self.btn_uninstall.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.btn_clear_data = ctk.CTkButton(app_action_frame, text="", command=self.clear_app_data)
        self.btn_clear_data.grid(row=1, column=0, padx=(120,5), pady=5, sticky="w")
        self.btn_extract_apk = ctk.CTkButton(app_action_frame, text="", command=self.extract_apk)
        self.btn_extract_apk.grid(row=1, column=0, padx=(260,5), pady=5, sticky="w")
        
    def create_utilities_tab(self):
        self.tab_utilities.grid_columnconfigure(0, weight=1)
        
        # --- Section 1: Commandes basiques (Install APK, Force Stop, Scrcpy, URL, Text) ---
        basic_commands_frame = ctk.CTkFrame(self.tab_utilities)
        basic_commands_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        basic_commands_frame.grid_columnconfigure(0, weight=1)
        
        self.btn_install_apk = ctk.CTkButton(basic_commands_frame, text="", command=self.install_apk)
        self.btn_install_apk.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.btn_force_stop = ctk.CTkButton(basic_commands_frame, text="", command=self.force_stop_app)
        self.btn_force_stop.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.btn_launch_scrcpy = ctk.CTkButton(basic_commands_frame, text="", command=self.launch_scrcpy)
        self.btn_launch_scrcpy.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
        self.label_open_url = ctk.CTkLabel(basic_commands_frame, text="")
        self.label_open_url.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.url_entry = ctk.CTkEntry(basic_commands_frame, placeholder_text="https://www.google.com")
        self.url_entry.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        self.btn_open_url = ctk.CTkButton(basic_commands_frame, text="", width=100, command=self.open_url)
        self.btn_open_url.grid(row=4, column=1, padx=10, pady=5)
        
        self.label_send_text = ctk.CTkLabel(basic_commands_frame, text="")
        self.label_send_text.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.text_entry = ctk.CTkEntry(basic_commands_frame, placeholder_text="Bonjour le monde")
        self.text_entry.grid(row=6, column=0, padx=10, pady=5, sticky="ew")
        self.btn_send_text = ctk.CTkButton(basic_commands_frame, text="", width=100, command=self.send_text)
        self.btn_send_text.grid(row=6, column=1, padx=10, pady=5)

        # --- Section 2: Transfert de Fichiers ---
        self.file_transfer_frame = ctk.CTkFrame(self.tab_utilities) # Removed text argument
        self.file_transfer_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.file_transfer_frame.grid_columnconfigure(1, weight=1)
        
        # Add a label for the frame title
        self.file_transfer_frame_label = ctk.CTkLabel(self.file_transfer_frame, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.file_transfer_frame_label.grid(row=0, column=0, columnspan=3, padx=5, pady=(5, 10), sticky="ew")

        self.label_device_path = ctk.CTkLabel(self.file_transfer_frame, text="")
        self.label_device_path.grid(row=1, column=0, padx=5, pady=5, sticky="w") # Adjusted row
        self.device_path_entry = ctk.CTkEntry(self.file_transfer_frame, placeholder_text="/sdcard/Download/")
        self.device_path_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew") # Adjusted row

        self.label_local_path = ctk.CTkLabel(self.file_transfer_frame, text="")
        self.label_local_path.grid(row=2, column=0, padx=5, pady=5, sticky="w") # Adjusted row
        self.local_path_entry = ctk.CTkEntry(self.file_transfer_frame, placeholder_text=os.path.expanduser("~\\Downloads"))
        self.local_path_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew") # Adjusted row
        self.btn_browse_local_path = ctk.CTkButton(self.file_transfer_frame, text="", command=self.browse_local_path, width=80)
        self.btn_browse_local_path.grid(row=2, column=2, padx=5, pady=5) # Adjusted row

        self.btn_push = ctk.CTkButton(self.file_transfer_frame, text="", command=self.push_file_folder)
        self.btn_push.grid(row=3, column=0, padx=5, pady=5, sticky="ew") # Adjusted row
        self.btn_pull = ctk.CTkButton(self.file_transfer_frame, text="", command=self.pull_file_folder)
        self.btn_pull.grid(row=3, column=1, padx=5, pady=5, sticky="ew") # Adjusted row

        # --- Section 3: Gestion de Fichiers/Dossiers sur l'appareil ---
        file_mgt_frame = ctk.CTkFrame(self.tab_utilities) # Removed text argument
        file_mgt_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        file_mgt_frame.grid_columnconfigure(0, weight=1)

        # Add a label for the frame title
        self.file_mgt_frame_label = ctk.CTkLabel(file_mgt_frame, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.file_mgt_frame_label.grid(row=0, column=0, padx=5, pady=(5, 10), sticky="ew")

        self.btn_list_dir_content = ctk.CTkButton(file_mgt_frame, text="", command=self.list_directory_content)
        self.btn_list_dir_content.grid(row=1, column=0, padx=5, pady=5, sticky="ew") # Adjusted row
        self.btn_delete_file_folder = ctk.CTkButton(file_mgt_frame, text="", command=self.delete_file_folder)
        self.btn_delete_file_folder.grid(row=2, column=0, padx=5, pady=5, sticky="ew") # Adjusted row
        self.btn_create_folder = ctk.CTkButton(file_mgt_frame, text="", command=self.create_folder_on_device)
        self.btn_create_folder.grid(row=3, column=0, padx=5, pady=5, sticky="ew") # Adjusted row

        # --- Section 4: Événements d'entrée ---
        self.input_event_frame = ctk.CTkFrame(self.tab_utilities) # Removed text argument
        self.input_event_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.input_event_frame.grid_columnconfigure(1, weight=1)

        # Add a label for the frame title
        self.input_event_frame_label = ctk.CTkLabel(self.input_event_frame, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.input_event_frame_label.grid(row=0, column=0, columnspan=2, padx=5, pady=(5, 10), sticky="ew")

        self.label_key_event_type = ctk.CTkLabel(self.input_event_frame, text="")
        self.label_key_event_type.grid(row=1, column=0, padx=5, pady=5, sticky="w") # Adjusted row
        self.key_event_menu = ctk.CTkOptionMenu(self.input_event_frame, values=[
            "HOME", "BACK", "POWER", "VOLUME_UP", "VOLUME_DOWN", "MENU"
        ])
        self.key_event_menu.grid(row=1, column=1, padx=5, pady=5, sticky="ew") # Adjusted row

        self.label_key_event_value = ctk.CTkLabel(self.input_event_frame, text="")
        self.label_key_event_value.grid(row=2, column=0, padx=5, pady=5, sticky="w") # Adjusted row
        self.key_event_value_entry = ctk.CTkEntry(self.input_event_frame, placeholder_text="Ex: 100 500 100 200 (swipe vertical)")
        self.key_event_value_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew") # Adjusted row
        self.btn_send_event = ctk.CTkButton(self.input_event_frame, text="", command=self.send_key_or_swipe_event)
        self.btn_send_event.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="ew") # Adjusted row

        # --- Section 5: Contrôle de l'appareil (Wi-Fi, Données, Mode Avion, Dev Options) ---
        self.device_control_frame = ctk.CTkFrame(self.tab_utilities) # Removed text argument
        self.device_control_frame.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.device_control_frame.grid_columnconfigure(0, weight=1)

        # Add a label for the frame title
        self.device_control_frame_label = ctk.CTkLabel(self.device_control_frame, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.device_control_frame_label.pack(fill="x", padx=5, pady=(5, 10))

        self.btn_toggle_wifi = ctk.CTkButton(self.device_control_frame, text="", command=lambda: self.toggle_setting("wifi"))
        self.btn_toggle_wifi.pack(fill="x", padx=5, pady=3)
        self.btn_toggle_mobile_data = ctk.CTkButton(self.device_control_frame, text="", command=lambda: self.toggle_setting("mobile_data"))
        self.btn_toggle_mobile_data.pack(fill="x", padx=5, pady=3)
        self.btn_toggle_airplane_mode = ctk.CTkButton(self.device_control_frame, text="", command=lambda: self.toggle_setting("airplane_mode"))
        self.btn_toggle_airplane_mode.pack(fill="x", padx=5, pady=3)
        self.btn_toggle_dev_options = ctk.CTkButton(self.device_control_frame, text="", command=lambda: self.toggle_setting("dev_options"))
        self.btn_toggle_dev_options.pack(fill="x", padx=5, pady=3)


    def create_advanced_tab(self):
        self.tab_advanced.grid_columnconfigure(0, weight=1)
        
        # Section Reboot/Screenshot
        adv_basic_frame = ctk.CTkFrame(self.tab_advanced)
        adv_basic_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        adv_basic_frame.grid_columnconfigure(0, weight=1)

        self.btn_reboot = ctk.CTkButton(adv_basic_frame, text="", command=lambda: self.reboot_device("reboot"))
        self.btn_reboot.pack(fill="x", padx=5, pady=5)
        self.btn_reboot_recovery = ctk.CTkButton(adv_basic_frame, text="", command=lambda: self.reboot_device("reboot recovery"))
        self.btn_reboot_recovery.pack(fill="x", padx=5, pady=5)
        self.btn_reboot_bootloader = ctk.CTkButton(adv_basic_frame, text="", command=lambda: self.reboot_device("reboot bootloader"))
        self.btn_reboot_bootloader.pack(fill="x", padx=5, pady=5)
        self.btn_screenshot = ctk.CTkButton(adv_basic_frame, text="", command=self.take_screenshot)
        self.btn_screenshot.pack(fill="x", padx=5, pady=15) # Increased pady for separation

        # Section Informations Avancées
        info_adv_frame = ctk.CTkFrame(self.tab_advanced) # Removed text argument
        info_adv_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        info_adv_frame.grid_columnconfigure(0, weight=1)

        # Add a label for the frame title
        self.info_adv_frame_label = ctk.CTkLabel(info_adv_frame, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.info_adv_frame_label.pack(fill="x", padx=5, pady=(5, 10))

        self.btn_get_logcat = ctk.CTkButton(info_adv_frame, text="", command=self.get_logcat)
        self.btn_get_logcat.pack(fill="x", padx=5, pady=5)
        self.btn_get_accounts = ctk.CTkButton(info_adv_frame, text="", command=self.get_accounts_list)
        self.btn_get_accounts.pack(fill="x", padx=5, pady=5)
        self.btn_get_app_permissions = ctk.CTkButton(info_adv_frame, text="", command=self.get_app_permissions)
        self.btn_get_app_permissions.pack(fill="x", padx=5, pady=5)

        # Section Gestion des Processus
        process_mgt_frame = ctk.CTkFrame(self.tab_advanced) # Removed text argument
        process_mgt_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        process_mgt_frame.grid_columnconfigure(0, weight=1)

        # Add a label for the frame title
        self.process_mgt_frame_label = ctk.CTkLabel(process_mgt_frame, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.process_mgt_frame_label.pack(fill="x", padx=5, pady=(5, 10))

        self.btn_list_running_processes = ctk.CTkButton(process_mgt_frame, text="", command=self.list_running_processes)
        self.btn_list_running_processes.pack(fill="x", padx=5, pady=5)

        process_kill_frame = ctk.CTkFrame(process_mgt_frame, fg_color="transparent")
        process_kill_frame.pack(fill="x", padx=5, pady=5)
        process_kill_frame.grid_columnconfigure(0, weight=1)
        self.label_process_id_name = ctk.CTkLabel(process_kill_frame, text="")
        self.label_process_id_name.grid(row=0, column=0, padx=5, sticky="w")
        self.process_entry = ctk.CTkEntry(process_kill_frame, placeholder_text="PID ou com.package.name")
        self.process_entry.grid(row=0, column=1, padx=5, sticky="ew")
        self.btn_kill_process = ctk.CTkButton(process_kill_frame, text="", command=self.kill_process_by_id_or_name, width=80)
        self.btn_kill_process.grid(row=0, column=2, padx=5)


        # Empty space to push content to top if window is large
        self.tab_advanced.grid_rowconfigure(3, weight=1)


    def create_about_tab(self):
        self.tab_about.grid_columnconfigure(0, weight=1)

        # --- Frame des crédits ---
        credits_frame = ctk.CTkFrame(self.tab_about)
        credits_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.label_created_by = ctk.CTkLabel(credits_frame, text="", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_created_by.pack(pady=10)
        
        self.label_version = ctk.CTkLabel(credits_frame, text="")
        self.label_version.pack()

        # --- Liens cliquables ---
        link_font = ctk.CTkFont(size=12, underline=True)
        xda_link = ctk.CTkLabel(credits_frame, text="XDA Forums", font=link_font, text_color="#1E90FF", cursor="hand2")
        xda_link.pack(pady=5)
        xda_link.bind("<Button-1>", lambda e: self.open_link("https://xdaforums.com/m/fufu25yt.13209688/"))
        
        website_link = ctk.CTkLabel(credits_frame, text="romscustom.blogspot.com", font=link_font, text_color="#1E90FF", cursor="hand2")
        website_link.pack()
        website_link.bind("<Button-1>", lambda e: self.open_link("https://romscustom.blogspot.com/"))
        
        # --- Sélecteur de langue ---
        lang_frame = ctk.CTkFrame(self.tab_about, fg_color="transparent")
        lang_frame.grid(row=1, column=0, pady=20)
        lang_selector = ctk.CTkSegmentedButton(lang_frame, values=["fr", "en"], command=self.switch_language)
        lang_selector.set(self.current_lang)
        lang_selector.pack()

        # Empty space to push content to top if window is large
        self.tab_about.grid_rowconfigure(3, weight=1)


    # =================================================================================
    # SECTION: LOGIQUE ADB (les fonctions existantes sont conservées et de nouvelles ajoutées)
    # =================================================================================
    def install_apk(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return

        filepath = filedialog.askopenfilename(
            title="Sélectionner un fichier APK",
            filetypes=(("Fichiers APK", "*.apk"), ("Tous les fichiers", "*.*"))
        )
        if not filepath:
            return

        self.log(f"Installation de {os.path.basename(filepath)}...")
        def task():
            stdout, stderr = self.run_adb_command(["install", "-r", filepath])
            if "Success" in stdout:
                self.log(f"SUCCÈS: {os.path.basename(filepath)} installé.")
            else:
                self.log(f"{self.get_string('log_error')}: {stderr or stdout}")
        self.run_in_thread(task)
        
    def force_stop_app(self):
        package = self.app_package_entry.get()
        if not package:
            self.log(f"{self.get_string('log_error')} Aucun package sélectionné.")
            return
        self.log(f"Arrêt forcé de {package}...")
        self.run_in_thread(lambda: self.log(self.run_adb_command(["shell", "am", "force-stop", package])[1] or f"'{package}' arrêté."))

    def launch_scrcpy(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        self.log("Lancement de scrcpy...")
        def task():
            try:
                # Popen est non-bloquant, il lance scrcpy dans son propre processus
                # Assurez-vous que scrcpy est dans le PATH ou spécifiez le chemin complet
                subprocess.Popen(["scrcpy", "-s", self.selected_device])
                self.log("Scrcpy lancé avec succès.")
            except FileNotFoundError:
                self.log(self.get_string("scrcpy_not_found"))
            except Exception as e:
                self.log(f"{self.get_string('log_error')} Scrcpy: {e}")
        self.run_in_thread(task)
            
    def open_url(self):
        url = self.url_entry.get()
        if not url:
            self.log(f"{self.get_string('log_error')} URL vide.")
            return
        self.log(f"Ouverture de {url} sur l'appareil...")
        self.run_in_thread(lambda: self.run_adb_command(["shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", url]))
        
    def send_text(self):
        text = self.text_entry.get()
        if not text:
            self.log(f"{self.get_string('log_error')} Texte vide.")
            return
        # Remplace les espaces par %s pour la commande adb
        # NOTE: Certaines versions d'ADB peuvent nécessiter d'échapper les espaces différemment ou d'utiliser des guillemets
        formatted_text = text.replace(" ", "%s") 
        self.log(f"Envoi du texte '{text}'...")
        self.run_in_thread(lambda: self.run_adb_command(["shell", "input", "text", formatted_text]))

    def run_in_thread(self, func, *args):
        thread = threading.Thread(target=func, args=args)
        thread.daemon = True
        thread.start()

    def run_adb_command(self, command_list, check=True):
        if self.selected_device:
            base_command = ["adb", "-s", self.selected_device]
        else:
            base_command = ["adb"]
        full_command = base_command + command_list
        try:
            # Désactiver la fenêtre de console pour les processus subprocess.run
            startupinfo = None
            if os.name == 'nt': # Pour Windows
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE

            result = subprocess.run(full_command, capture_output=True, text=True, check=check, 
                                    encoding='utf-8', errors='ignore', startupinfo=startupinfo)
            return result.stdout.strip(), result.stderr.strip()
        except FileNotFoundError:
            return None, f"{self.get_string('log_error')} 'adb' not found. Ensure ADB is installed and in your system's PATH."
        except subprocess.CalledProcessError as e:
            return e.stdout.strip(), e.stderr.strip()
        except Exception as e:
            return None, f"{self.get_string('log_error')} An unexpected error occurred: {e}"


    def log(self, message):
        self.log_textbox.insert("end", f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {message}\n")
        self.log_textbox.see("end")

    def refresh_devices(self):
        self.log(self.get_string("log_searching_devices"))
        stdout, stderr = self.run_adb_command(["devices"], check=False)
        if stderr and "List of devices attached" not in stdout: # filter common "not found" stderr
             self.log(f"{self.get_string('log_error')} {stderr}")
             return

        self.devices_list = [line.split('\t')[0] for line in stdout.splitlines()[1:] if '\tdevice' in line]
        if self.devices_list:
            self.device_menu.configure(values=self.devices_list)
            self.device_menu.set(self.devices_list[0])
            self.selected_device = self.devices_list[0]
            self.log(f"{self.get_string('log_devices_found')} {self.devices_list}")
        else:
            self.device_menu.configure(values=[self.get_string("no_device")])
            self.device_menu.set(self.get_string("no_device"))
            self.selected_device = None
            self.log(self.get_string("log_no_authorized_device"))
            
    def on_device_select(self, device):
        if device == self.get_string("no_device"):
            self.selected_device = None
            return
        self.selected_device = device
        self.log(self.get_string("log_device_selected").format(device=device))

    def get_device_info(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        self.log(f"Récupération des informations pour {self.selected_device}...")
        def task():
            model, _ = self.run_adb_command(["shell", "getprop", "ro.product.model"])
            version, _ = self.run_adb_command(["shell", "getprop", "ro.build.version.release"])
            sdk, _ = self.run_adb_command(["shell", "getprop", "ro.build.version.sdk"])
            
            # Use grep for better filtering battery level
            battery_raw, _ = self.run_adb_command(["shell", "dumpsys", "battery"])
            battery_level = "N/A"
            for line in battery_raw.splitlines():
                if "level:" in line:
                    battery_level = line.strip()
                    break

            resolution, _ = self.run_adb_command(["shell", "wm", "size"])
            
            info_text = f"\n--- INFOS APPAREIL ({self.selected_device}) ---\n" \
                        f"Modèle: {model}\n" \
                        f"Version Android: {version} (SDK: {sdk})\n" \
                        f"Batterie: {battery_level}\n" \
                        f"Résolution: {resolution.replace('Physical size:', '').strip()}\n" \
                        f"--------------------\n"
            self.log(info_text)
        self.run_in_thread(task)

    def list_apps(self, mode="user"):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        self.log(f"Chargement des applications ({mode})...")
        self.progress_bar.start()
        # Clear existing app list
        for widget in self.app_list_frame.winfo_children():
            widget.destroy()
        def task():
            # -3 for third-party (user) apps, -s for system apps
            cmd = ["shell", "pm", "list", "packages", "-3"] if mode == "user" else ["shell", "pm", "list", "packages", "-s"]
            stdout, stderr = self.run_adb_command(cmd)
            self.progress_bar.stop()
            self.progress_bar.set(0) # Reset progress bar
            if stderr:
                self.log(f"{self.get_string('log_error')} {stderr}")
                return
            packages = sorted([line.replace("package:", "") for line in stdout.splitlines()])
            self.log(f"{len(packages)} applications trouvées.")
            if not packages:
                self.log("Aucune application trouvée pour ce filtre.")

            # Create labels for each package
            for pkg in packages:
                label = ctk.CTkLabel(self.app_list_frame, text=pkg, anchor="w")
                label.pack(fill="x", padx=5)
                # Bind click event to populate entry field
                label.bind("<Button-1>", lambda e, p=pkg: self.on_app_select(p))
        self.run_in_thread(task)


    def on_app_select(self, package_name):
        self.app_package_entry.delete(0, "end")
        self.app_package_entry.insert(0, package_name)
        self.log(f"Package '{package_name}' sélectionné.")

    def uninstall_app(self):
        package = self.app_package_entry.get()
        if not package:
            self.log(f"{self.get_string('log_error')} Aucun package sélectionné.")
            return
        dialog = ctk.CTkInputDialog(text=self.get_string('uninstall_confirm_text').format(package=package), title=self.get_string('uninstall_confirm_title'))
        confirmation = dialog.get_input()
        if confirmation and (confirmation.lower() == 'oui' or confirmation.lower() == 'yes'):
            self.log(f"Désinstallation de {package}...")
            # Use get_string for success/error messages directly from run_adb_command output
            stdout, stderr = self.run_adb_command(["uninstall", package])
            if "Success" in stdout:
                self.log(f"'{package}' désinstallé avec succès.")
            else:
                self.log(f"{self.get_string('log_error')}: {stderr or stdout}")
        else:
            self.log(self.get_string("uninstall_cancelled"))

    def clear_app_data(self):
        package = self.app_package_entry.get()
        if not package:
            self.log(f"{self.get_string('log_error')} Aucun package sélectionné.")
            return
        self.log(f"Nettoyage des données de {package}...")
        stdout, stderr = self.run_adb_command(["shell", "pm", "clear", package])
        if "Success" in stdout:
            self.log(f"Données de '{package}' nettoyées.")
        else:
            self.log(f"{self.get_string('log_error')}: {stderr or stdout}")

    def extract_apk(self):
        package = self.app_package_entry.get()
        if not package:
            self.log(f"{self.get_string('log_error')} Aucun package sélectionné.")
            return
        self.log(f"Extraction de l'APK pour {package}...")
        def task():
            path_stdout, err = self.run_adb_command(["shell", "pm", "path", package])
            if err or not path_stdout:
                self.log(f"Erreur: Impossible de trouver le chemin de l'APK pour {package}. {err}")
                return
            apk_path_on_device = path_stdout.replace("package:", "").strip()
            downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
            local_path = os.path.join(downloads_path, f"{package}.apk")
            self.log(f"Chemin de l'APK: {apk_path_on_device}")
            self.log(f"Sauvegarde dans: {local_path}")
            
            _, pull_err = self.run_adb_command(["pull", apk_path_on_device, local_path])
            if pull_err:
                self.log(f"Erreur durant l'extraction: {pull_err}")
            else:
                self.log(f"SUCCÈS: APK extrait dans votre dossier Téléchargements.")
        self.run_in_thread(task)

    def reboot_device(self, mode):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        self.log(f"Envoi de la commande de redémarrage ({mode})...")
        stdout, stderr = self.run_adb_command(mode.split())
        if stderr:
            self.log(f"{self.get_string('log_error')}: {stderr}")
        else:
            self.log(f"Appareil redémarré en mode '{mode}'.")


    def take_screenshot(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        self.log("Prise de la capture d'écran...")
        self.run_in_thread(lambda: self._take_screenshot_task())

    def _take_screenshot_task(self):
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        device_path = f"/sdcard/screenshot_{timestamp}.png" # Unique name on device
        local_path = os.path.join(desktop_path, f"screenshot_{timestamp}.png")
        
        stdout_cap, err_cap = self.run_adb_command(["shell", "screencap", "-p", device_path])
        if err_cap and "No such file or directory" not in err_cap: # Filter common stderr for success
            self.log(f"{self.get_string('log_error')} capture: {err_cap}")
            return
        
        stdout_pull, err_pull = self.run_adb_command(["pull", device_path, local_path])
        if err_pull:
            self.log(f"{self.get_string('log_error')} transfert: {err_pull}")
            return

        # Clean up screenshot on device
        self.run_adb_command(["shell", "rm", device_path])
        self.log(self.get_string("screenshot_saved").format(path=local_path))
        
    def connect_wifi(self):
        ip = self.wifi_ip_entry.get()
        if not ip:
            self.log("Veuillez entrer une adresse IP.")
            return
        if not self.selected_device:
            self.log("Aucun appareil USB sélectionné pour initialiser la connexion TCP/IP.")
            return

        self.log("D'abord, activez le port TCP/IP...")
        self.run_in_thread(self._connect_wifi_task, ip)
        
    def _connect_wifi_task(self, ip):
        tcpip_stdout, tcpip_stderr = self.run_adb_command(["tcpip", "5555"])
        if tcpip_stderr and "multiple" in tcpip_stderr:
            self.log("Erreur: Plusieurs appareils connectés. Gardez seulement celui à connecter en Wi-Fi via USB.")
            return
        elif tcpip_stderr and "error" in tcpip_stderr:
            self.log(f"Erreur lors du passage en mode TCP/IP: {tcpip_stderr}")
            return
        elif "restarting in TCP mode" not in tcpip_stdout:
            self.log(f"Échec de l'activation du mode TCP/IP: {tcpip_stdout}")
            return
        else:
            self.log("Mode TCP/IP activé. Vous pouvez débrancher l'USB (si l'appareil est déjà connecté en USB).")
            # Give device a moment to restart adbd in TCP/IP mode
            time.sleep(3) 

        self.log(f"Tentative de connexion à {ip}:5555...")
        connect_stdout, connect_stderr = self.run_adb_command(["connect", f"{ip}:5555"], check=False) # check=False because connect returns non-zero on already connected or failed
        
        if "already connected" in connect_stdout:
            self.log(f"Appareil déjà connecté en Wi-Fi à {ip}:5555.")
        elif "connected to" in connect_stdout:
            self.log(f"Connexion Wi-Fi à {ip}:5555 réussie.")
            self.refresh_devices() # Refresh device list to show the new connection
        elif connect_stderr:
             self.log(f"{self.get_string('log_error')} Échec de la connexion: {connect_stderr}")
        else:
            self.log(f"{self.get_string('log_error')} Échec de la connexion: {connect_stdout}")


    # --- Nouvelles Fonctions Utilitaires ---

    def browse_local_path(self):
        # Permettre de sélectionner un fichier ou un dossier
        path = filedialog.askopenfilename() or filedialog.askdirectory()
        if path:
            self.local_path_entry.delete(0, ctk.END)
            self.local_path_entry.insert(0, path)

    def push_file_folder(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        source_path = self.local_path_entry.get()
        dest_path = self.device_path_entry.get()

        if not source_path or not dest_path:
            self.log(f"{self.get_string('log_error')} {self.get_string('source_dest_required')}")
            return
        
        if not os.path.exists(source_path):
            self.log(f"{self.get_string('log_error')} Le chemin local source n'existe pas : {source_path}")
            return

        self.log(f"Poussée de '{source_path}' vers '{dest_path}' sur l'appareil...")
        def task():
            stdout, stderr = self.run_adb_command(["push", source_path, dest_path])
            if stderr:
                self.log(f"{self.get_string('log_error')}: {stderr}")
            else:
                self.log(self.get_string("push_success").format(source=os.path.basename(source_path), dest=dest_path))
        self.run_in_thread(task)

    def pull_file_folder(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        source_path = self.device_path_entry.get()
        dest_path = self.local_path_entry.get()

        if not source_path or not dest_path:
            self.log(f"{self.get_string('log_error')} {self.get_string('source_dest_required')}")
            return
        
        # Ensure local destination exists if it's a directory
        if os.path.isdir(dest_path) and not os.path.exists(dest_path):
             os.makedirs(dest_path)

        self.log(f"Tirage de '{source_path}' de l'appareil vers '{dest_path}'...")
        def task():
            stdout, stderr = self.run_adb_command(["pull", source_path, dest_path])
            if stderr:
                self.log(f"{self.get_string('log_error')}: {stderr}")
            else:
                self.log(self.get_string("pull_success").format(source=source_path, dest=dest_path))
        self.run_in_thread(task)

    def list_directory_content(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        device_path = simpledialog.askstring("Lister Contenu Dossier", self.get_string("enter_device_path"))
        if not device_path:
            return
        
        self.log(f"Lister le contenu de '{device_path}' sur l'appareil...")
        def task():
            stdout, stderr = self.run_adb_command(["shell", "ls", "-F", device_path]) # -F adds / for dirs, * for executables etc.
            if stderr and "No such file or directory" not in stderr:
                self.log(f"{self.get_string('log_error')}: {stderr}")
            elif not stdout.strip():
                self.log(self.get_string("list_dir_empty"))
            else:
                self.log(f"Contenu de '{device_path}':\n{stdout}")
        self.run_in_thread(task)

    def delete_file_folder(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        path_to_delete = simpledialog.askstring("Supprimer Fichier/Dossier", self.get_string("enter_file_or_dir_to_delete"))
        if not path_to_delete:
            return
        
        dialog = ctk.CTkInputDialog(text=self.get_string('delete_confirm').format(path=path_to_delete), title=self.get_string('delete_file_folder'))
        confirmation = dialog.get_input()

        if confirmation and (confirmation.lower() == 'oui' or confirmation.lower() == 'yes'):
            self.log(f"Suppression de '{path_to_delete}' sur l'appareil...")
            def task():
                stdout, stderr = self.run_adb_command(["shell", "rm", "-r", path_to_delete]) # -r for recursive delete of folders
                if stderr:
                    self.log(f"{self.get_string('log_error')}: {stderr}")
                else:
                    self.log(self.get_string("file_dir_deleted").format(path=path_to_delete))
            self.run_in_thread(task)
        else:
            self.log(self.get_string("delete_cancelled"))

    def create_folder_on_device(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        folder_path = simpledialog.askstring("Créer Dossier", self.get_string("enter_folder_to_create"))
        if not folder_path:
            return
        
        self.log(f"Création du dossier '{folder_path}' sur l'appareil...")
        def task():
            stdout, stderr = self.run_adb_command(["shell", "mkdir", "-p", folder_path]) # -p creates parent directories as needed
            if stderr:
                self.log(f"{self.get_string('log_error')}: {stderr}")
            else:
                self.log(self.get_string("folder_created").format(path=folder_path))
        self.run_in_thread(task)

    def send_key_or_swipe_event(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return

        event_type_str = self.key_event_menu.get()
        event_value = self.key_event_value_entry.get()

        command = []
        # Map translated key names back to ADB keycodes
        key_map = {
            self.get_string("key_home"): "3",
            self.get_string("key_back"): "4",
            self.get_string("key_power"): "26",
            self.get_string("key_volume_up"): "24",
            self.get_string("key_volume_down"): "25",
            self.get_string("key_menu"): "82"
        }
        
        # Check if it's a key event
        if event_type_str in key_map:
            key_code = key_map[event_type_str]
            command = ["shell", "input", "keyevent", key_code]
            self.log(f"Envoi de l'événement touche : {event_type_str} (Code: {key_code})...")
        elif "swipe" in event_type_str.lower(): # If user selects 'Swipe' or similar, then use text entry as coordinates
            coords = event_value.split()
            if len(coords) == 4:
                try:
                    x1, y1, x2, y2 = map(int, coords)
                    command = ["shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2)]
                    self.log(f"Envoi de l'événement swipe : {x1} {y1} {x2} {y2}...")
                except ValueError:
                    self.log(f"{self.get_string('log_error')} Coordonnées de swipe invalides. Utilisez 4 nombres entiers séparés par des espaces.")
                    return
            else:
                self.log(f"{self.get_string('log_error')} Pour un swipe, veuillez entrer 4 coordonnées (x1 y1 x2 y2) séparées par des espaces.")
                return
        else: # Assume custom key event code or raw text for input (less common but possible)
            if not event_value:
                self.log(f"{self.get_string('log_error')} Veuillez entrer une valeur pour l'événement.")
                return
            command = ["shell", "input", "keyevent", event_value] # Try to send as a keyevent
            self.log(f"Envoi de l'événement touche personnalisé : {event_value}...")
            
        if command:
            self.run_in_thread(lambda: self.run_adb_command(command))
            self.key_event_value_entry.delete(0, ctk.END) # Clear after sending
            self.key_event_value_entry.insert(0, self.get_string("swipe_example")) # Reset placeholder

    def toggle_setting(self, setting_type):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        def task():
            if setting_type == "wifi":
                # Get current state
                state_stdout, _ = self.run_adb_command(["shell", "settings", "get", "global", "wifi_on"])
                current_state = int(state_stdout.strip())
                new_state = 1 if current_state == 0 else 0
                
                self.log(f"Basculement du Wi-Fi à {'ACTIVÉ' if new_state == 1 else 'DÉSACTIVÉ'}...")
                _, stderr = self.run_adb_command(["shell", "svc", "wifi", str(new_state)])
                if stderr:
                    self.log(f"{self.get_string('log_error')}: {stderr}")
                else:
                    self.log(self.get_string("wifi_on") if new_state == 1 else self.get_string("wifi_off"))
            
            elif setting_type == "mobile_data":
                # Get current state (this is more complex, often requires API 23+ for `service call` or `dumpsys` parsing)
                # A simpler approach for toggling without reading state is to just try to toggle.
                # For more reliable state checking, you might need 'dumpsys telephony.registry'
                # Let's use a simpler toggle for now, assuming current state is unknown
                self.log("Tentative de basculement des données mobiles (nécessite Android 5+)...")
                
                # Check current state (API 28+ often uses 'settings get global mobile_data')
                # For older APIs, it's harder to get state via adb shell without root.
                # This command will *toggle* but doesn't tell us the *current* state first.
                # Best effort: Try to toggle, and if it fails, log an error.
                # This is a bit of a hack, a real toggle would read the current state first.
                # However, there's no simple 'adb shell settings get global mobile_data' pre-Android 9.
                # This is an example of a command that *might* work but isn't universal.
                # A more robust solution for mobile data would involve external libraries or root.
                stdout, stderr = self.run_adb_command(["shell", "svc", "data", "disable"])
                if not stderr: # If disabling worked, try enabling
                    self.log(self.get_string("mobile_data_off"))
                    time.sleep(1) # Give it a moment
                    stdout, stderr = self.run_adb_command(["shell", "svc", "data", "enable"])
                    if not stderr:
                        self.log(self.get_string("mobile_data_on"))
                    else:
                        self.log(f"{self.get_string('log_error')} Basculement des données mobiles: {stderr or stdout}")
                else: # If disabling failed, maybe it was already off, try enabling
                    stdout, stderr = self.run_adb_command(["shell", "svc", "data", "enable"])
                    if not stderr:
                        self.log(self.get_string("mobile_data_on"))
                    else:
                        self.log(f"{self.get_string('log_error')} Basculement des données mobiles: {stderr or stdout}")


            elif setting_type == "airplane_mode":
                # Get current state
                state_stdout, _ = self.run_adb_command(["shell", "settings", "get", "global", "airplane_mode_on"])
                current_state = int(state_stdout.strip())
                new_state = 1 if current_state == 0 else 0

                self.log(f"Basculement du mode avion à {'ACTIVÉ' if new_state == 1 else 'DÉSACTIVÉ'}...")
                # Set airplane mode
                self.run_adb_command(["shell", "settings", "put", "global", "airplane_mode_on", str(new_state)])
                # Broadcast intent to apply the change
                self.run_adb_command(["shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "true" if new_state == 1 else "false"])
                self.log(self.get_string("airplane_mode_on") if new_state == 1 else self.get_string("airplane_mode_off"))

            elif setting_type == "dev_options":
                # Get current state (simplified, actual check is more complex)
                # This command attempts to toggle the state of adb over USB, which often reflects dev options.
                # A proper check would involve parsing 'settings get global development_settings_enabled' (API 26+)
                # or 'settings get global adb_enabled'
                self.log("Tentative de basculement du mode développeur (ADB sur USB)...")
                
                # Check current adb_enabled state (common indicator for dev options being active)
                current_adb_state_raw, _ = self.run_adb_command(["shell", "settings", "get", "global", "adb_enabled"])
                current_adb_state = int(current_adb_state_raw.strip()) if current_adb_state_raw.strip().isdigit() else 0

                new_adb_state = 1 if current_adb_state == 0 else 0
                
                stdout, stderr = self.run_adb_command(["shell", "settings", "put", "global", "adb_enabled", str(new_adb_state)])
                if stderr:
                    self.log(f"{self.get_string('log_error')} Basculement mode développeur: {stderr}")
                else:
                    self.log(self.get_string("dev_options_on") if new_adb_state == 1 else self.get_string("dev_options_off"))
                    # Note: Toggling adb_enabled doesn't always reflect the full "Developer options" switch,
                    # but it's the most direct ADB command for that functionality.
                    # A full toggle of "Developer options" requires root or complex UI automation.
        self.run_in_thread(task)


    # --- Nouvelles Fonctions Avancées ---

    def get_logcat(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        self.log("Récupération des logs (logcat)... Cela peut prendre un certain temps.")
        def task():
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = os.path.join(os.path.expanduser('~'), 'Desktop', f"logcat_{timestamp}.txt")
            
            # -d dumps the log and exits, -s filters by tag (optional)
            stdout, stderr = self.run_adb_command(["logcat", "-d"]) 
            
            if stderr:
                self.log(f"{self.get_string('log_error')}: {stderr}")
            else:
                try:
                    with open(log_file, "w", encoding="utf-8") as f:
                        f.write(stdout)
                    self.log(self.get_string("logcat_saved").format(path=log_file))
                except Exception as e:
                    self.log(f"{self.get_string('log_error')} Erreur lors de l'écriture du fichier logcat: {e}")
        self.run_in_thread(task)

    def get_accounts_list(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        self.log("Récupération de la liste des comptes...")
        def task():
            stdout, stderr = self.run_adb_command(["shell", "dumpsys", "account"])
            if stderr:
                self.log(f"{self.get_string('log_error')}: {stderr}")
                return
            
            accounts = []
            for line in stdout.splitlines():
                if "Account {" in line and "type=" in line:
                    # Example: Account {name=user@gmail.com, type=com.google}
                    try:
                        name_start = line.find("name=") + len("name=")
                        name_end = line.find(",", name_start)
                        account_name = line[name_start:name_end]

                        type_start = line.find("type=") + len("type=")
                        type_end = line.find("}", type_start)
                        account_type = line[type_start:type_end]
                        accounts.append(f"  - {account_name} (Type: {account_type})")
                    except Exception:
                        # Fallback for unexpected formats
                        accounts.append(f"  - {line.strip()}")
            
            if accounts:
                self.log(f"{self.get_string('accounts_list')}\n" + "\n".join(accounts))
            else:
                self.log(self.get_string("no_accounts"))
        self.run_in_thread(task)

    def get_app_permissions(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        package = self.app_package_entry.get() # Reuse app package entry from App tab
        if not package:
            self.log(f"{self.get_string('log_error')} Veuillez entrer un nom de package pour obtenir les permissions (ou sélectionnez-en un dans l'onglet Apps).")
            return
        
        self.log(f"Récupération des permissions pour '{package}'...")
        def task():
            stdout, stderr = self.run_adb_command(["shell", "dumpsys", "package", package])
            if stderr:
                self.log(f"{self.get_string('log_error')}: {stderr}")
                return
            
            permissions = []
            in_permissions_section = False
            for line in stdout.splitlines():
                if "Permissions:" in line:
                    in_permissions_section = True
                    continue
                if in_permissions_section:
                    if "User 0:" in line or "gids=" in line: # End of permissions section
                        break
                    if "Permission [" in line or "granted=" in line or "req:" in line:
                        permissions.append(line.strip())
            
            if permissions:
                self.log(self.get_string("permissions_for").format(package=package) + "\n" + "\n".join(permissions))
            else:
                self.log(self.get_string("no_permissions_found").format(package=package))
        self.run_in_thread(task)

    def list_running_processes(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        self.log("Lister les processus en cours...")
        def task():
            # 'ps -A' or 'ps -e' lists all processes, 'ps -Af' for full format
            # Output can be verbose, so we just dump it to the log.
            stdout, stderr = self.run_adb_command(["shell", "ps", "-A"]) 
            
            if stderr:
                self.log(f"{self.get_string('log_error')}: {stderr}")
            elif not stdout.strip():
                self.log("Aucun processus en cours trouvé.")
            else:
                self.log(f"{self.get_string('processes_list')}\n{stdout}")
        self.run_in_thread(task)

    def kill_process_by_id_or_name(self):
        if not self.selected_device:
            self.log(f"{self.get_string('log_error')} {self.get_string('no_device')}")
            return
        
        process_id_or_name = self.process_entry.get().strip()
        if not process_id_or_name:
            self.log(f"{self.get_string('log_error')} {self.get_string('process_id_or_name')} est requis.")
            return

        self.log(f"Tentative de terminer le processus '{process_id_or_name}'...")
        def task():
            # Try to kill by PID first, then by name (package name)
            stdout_kill, stderr_kill = self.run_adb_command(["shell", "kill", process_id_or_name], check=False)
            
            if not stderr_kill and not stdout_kill: # Success if no output
                self.log(self.get_string("process_killed").format(process=process_id_or_name))
            else:
                # If kill by PID failed, try force stop for package
                stdout_am, stderr_am = self.run_adb_command(["shell", "am", "force-stop", process_id_or_name], check=False)
                if not stderr_am:
                    self.log(self.get_string("process_killed").format(process=process_id_or_name))
                else:
                    self.log(f"{self.get_string('log_error')} {self.get_string('kill_failed').format(process=process_id_or_name)}: {stderr_kill or stdout_kill or stderr_am or stdout_am}")
        self.run_in_thread(task)

# =================================================================================
# SECTION: MESSAGE D'AVERTISSEMENT ET LANCEMENT DE L'APPLICATION
# =================================================================================
class WarningDialog(ctk.CTkToplevel):
    def __init__(self, master, title, message):
        super().__init__(master)
        self.master = master
        self.title(title)
        self.geometry("500x300")
        self.resizable(False, False)
        self.transient(master)  # Make dialog appear on top of master window
        self.grab_set()        # Grab focus until dialog is closed

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.label_title = ctk.CTkLabel(self, text=title, font=ctk.CTkFont(size=18, weight="bold"))
        self.label_title.pack(pady=10)

        self.textbox_message = ctk.CTkTextbox(self, wrap="word", height=150, width=450, font=ctk.CTkFont(size=12))
        self.textbox_message.insert("0.0", message)
        self.textbox_message.configure(state="disabled") # Make it read-only
        self.textbox_message.pack(pady=10, padx=20)

        self.ok_button = ctk.CTkButton(self, text="Compris", command=self.destroy)
        self.ok_button.pack(pady=10)

        # Center the dialog on the main window
        self.update_idletasks()
        x = master.winfo_x() + (master.winfo_width() / 2) - (self.winfo_width() / 2)
        y = master.winfo_y() + (master.winfo_height() / 2) - (self.winfo_height() / 2)
        self.geometry(f"+{int(x)}+{int(y)}")

def show_warning_on_startup(app_instance):
    lang_key = app_instance.current_lang
    title = LANGUAGES[lang_key]["prevention_title"]
    message = LANGUAGES[lang_key]["prevention_text"]
    dialog = WarningDialog(app_instance, title, message)
    app_instance.wait_window(dialog)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

    app = AdbControlCenter()
    
    # Message de prévention au démarrage
    LANGUAGES["fr"]["prevention_title"] = "⚠️ Message de Prévention ⚠️"
    LANGUAGES["fr"]["prevention_text"] = "Cet outil exécute des commandes ADB puissantes. Des actions comme la désinstallation ou la suppression de données sont irréversibles. Une mauvaise utilisation peut entraîner une perte de données ou rendre votre appareil instable. Utilisez cet outil à vos propres risques. L'auteur ne peut être tenu responsable des dommages causés."
    LANGUAGES["en"]["prevention_title"] = "⚠️ Prevention Message ⚠️"
    LANGUAGES["en"]["prevention_text"] = "This tool executes powerful ADB commands. Actions like uninstalling or clearing data are irreversible. Misuse can lead to data loss or an unstable device. Use this tool at your own risk. The author cannot be held responsible for any damage."
    
    show_warning_on_startup(app) # Show warning after app is initialized

    app.mainloop()