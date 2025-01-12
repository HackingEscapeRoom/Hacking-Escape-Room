import os

def create_folder_structure():
    base_path = "ALS_KI_Unternehmen"
    
    # Definiere die Ordnerstruktur
    folders = [
        f"{base_path}/Modelle/[Modellname]/Weights/Checkpoints",
        f"{base_path}/Modelle/[Modellname]/Weights/Backup",
        f"{base_path}/Modelle/[Modellname]/Model_Architecture",
        f"{base_path}/Modelle/[Modellname]/Training_Data",
        f"{base_path}/Modelle/[Modellname]/Performance",
        f"{base_path}/Modelle/[Modellname]/Deployment",
        f"{base_path}/Projekte/Laufende_Projekte",
        f"{base_path}/Projekte/Abgeschlossene_Projekte",
        f"{base_path}/Dokumentation/Unternehmensstrategie",
        f"{base_path}/Support/Kundenbetreuung",
        f"{base_path}/Entwicklung/Forschung",
        f"{base_path}/Entwicklung/Infrastruktur"
    ]
    
    # Erstelle alle Ordner
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

# Ausführen der Funktion
create_folder_structure()