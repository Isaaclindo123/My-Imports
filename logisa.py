# logisaac.py ou logisa.py
lazy import logging
lazy import os

__all__ = ["isalog", "isalimp"]

print("(Log Isa 1.1.5) Hello!!! From Two Points Ltda Community!!! See my github to more: https://github.com/Isaaclindo123. (This message is inspired in the pygame (:. )")

def isalog(archivename, level):
    """
    Função chamada pelo arquivo principal para definir o nome do arquivo
    e o nível do log. Se nome_arquivo for vazio ou None, exibe o erro.
    """
    if not archivename:
        print("IsaImpError: TBMRCL: [ISALOG code: 1] Oops, you don't defined the archive name!!! Try 'logisa.isalog(ARCHIVENAME, logging.LEVEL)' to run correctly (example: twopoints.log)")
        return False
    if not level:
        print("IsaImpError: TBMRCL: [ISALOG code: 2] Oops, you don't defined the level of the log!!! Try 'logisa.isalog(ARCHIVENAME, logging.LEVEL)' and existent levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. (example isalog(twopoints.log, DEBUG))")
        return False

    # Validação se o nível de log é válido (deve ser um inteiro aceito pelo módulo logging)
    if not isinstance(level, int):
        print(f"IsaImpError: TBMRCL: [ISALOG code: 5] Oops, the level '{level}' is invalid! Use standard levels like logging.DEBUG, logging.INFO, etc.")
        return False

    # Validação se o diretório do arquivo existe (caso o caminho inclua pastas)
    directory = os.path.dirname(archivename)
    if directory and not os.path.exists(directory):
        print(f"IsaImpWarn: TBMRCL: [ISALOG code: 6] The directory '{directory}' does not exist. Attempting to create it...")
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            print(f"IsaImpError: TBMRCL: [ISALOG code: 7] Could not create directory '{directory}': {e}")
            return False
        
    logging.basicConfig(
        filename=archivename,
        filemode='a',
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )
    return True

def isalimp(archivename):
    if not archivename:
        print("IsaImpError TBMRCL: [ISALIMP code: 3] Oops, you don't defined the archive name!!! Try 'logisa.isalimp(ARCHIVENAME)' to run correctly (example: twopoints.log)")
        return False
    try:
        with open(archivename, 'w') as arch:
            pass
        print(f"The archive {archivename} is cleaned!!! Try to write new logs!!!")
        return True
    except FileNotFoundError:
        print(f"IsaImpWarn TBMRCL: [ISALIMP code:4] Oops, the archive {archivename} is already clearned, try to write new logs with this archive!!!")
        return True
        
def test():
    dfi =  r"C:\Users\Test"
    acm = os.path.join(dfi, "test.log")
    
    if not os.path.exists(dfi):
        os.makedirs(dfi)
    
    with open(acm, "w", encoding="utf-8") as dfim:
        dfim.write("-- Start -- \n")

    
    print("Hello!!! From Test... Okay, this is just a test :) \n")
    print("Pls DON'T MAKE TBMRCL")
    isalog(acm, logging.INFO)
    logging.info("ITS WORKING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



