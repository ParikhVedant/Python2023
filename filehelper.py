def read_from_file(file_path: str) -> str:
    """
        Fetches str value from given file 
    """    

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def write_to_file(file_path: str, content: str) -> None:
    """
        Writes str to file 
    """    

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

def appends_to_file(file_path: str, content: str) -> None:
    """
        Appends str to file (creates file if does not exist) 
    """    

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content)

