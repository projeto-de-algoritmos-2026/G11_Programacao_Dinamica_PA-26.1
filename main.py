import os
import sys
import time
from core.game import CaldeiraJogo, limpar_tela

def ler_tecla():
    if os.name == 'nt':
        import msvcrt
        ch = msvcrt.getch()
        if ch in (b'\x00', b'\xe0'):
            ch = msvcrt.getch()
            if ch == b'H': return 'cima'
            if ch == b'P': return 'baixo'
        if ch == b'\r': return 'enter'
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                ch2 = sys.stdin.read(2)
                if ch2 == '[A': return 'cima'
                if ch2 == '[B': return 'baixo'
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        if ch == '\n' or ch == '\r': return 'enter'
    return None

def exibir_menu_principal(opcao_selecionada):
    limpar_tela()
    ascii_art = """
 ███  █      ███  █   █ ███ █   █ ███  ████ █████  ███     ████  █████ ████  █████ █████ ███ █████  ███  
█   █ █     █   █ █   █  █  ██ ██  █  █       █   █   █     █   █ █     █   █ █     █      █   █   █   █ 
█████ █     █   █ █   █  █  █ █ █  █   ███    █   █████     ████  ████  ████  ████  ████   █   █   █   █ 
█   █ █     █  █  █   █  █  █   █  █      █   █   █   █     █     █     █  █  █     █      █   █   █   █ 
█   █ █████  ██ █  ███  ███ █   █ ███ ████    █   █   █     █     █████ █   █ █     █████ ███  █    ███  
    """
    print(ascii_art)
    print("\n" + "—"*70)
    print(" Use as SETAS DO TECLADO (▲/▼) para navegar e ENTER para selecionar:")
    print("—"*70 + "\n")
    
    if opcao_selecionada == 0:
        print("  ► \033[1;32m[ INICIAR JOGO ]\033[0m")
        print("    [ SAIR DO JOGO ]")
    else:
        print("    [ INICIAR JOGO ]")
        print("  ► \033[1;31m[ SAIR DO JOGO ]\033[0m")
    print("\n" + "—"*70)

def main():
    opcao_atual = 0
    
    while True:
        exibir_menu_principal(opcao_atual)
        tecla = ler_tecla()
        
        if tecla == 'cima':
            opcao_atual = 0
        elif tecla == 'baixo':
            opcao_atual = 1
        elif tecla == 'enter':
            if opcao_atual == 0:
                jogo = CaldeiraJogo()
                jogo.jogar()
            else:
                limpar_tela()
                print("\n Fechando grimório... Até a próxima, mestre alquimista!")
                time.sleep(1)
                break

if __name__ == "__main__":
    main()