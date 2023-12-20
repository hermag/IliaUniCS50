from pathlib import Path
def check_if_file_exists(file_path):
    path = Path(file_path)
    if path.is_file():
        print(f'The file "{file_path}" exists.')
    else:
        print(f'The file "{file_path}" does not exist.')