import os
import time
import random
from services.selo import calcular_minimo_ingredientes

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class CaldeiraJogo:
    def __init__(self):
        self.ingredientes = {
            "Pó de Fênix": 3,
            "Lágrima de Dragão": 5,
            "Essência Noturna": 7,
            "Raiz de Mandrágora": 11
        }
        self.peso_alvo = 0
        self.peso_atual = 0
        self.movimentos_jogador = 0
        self.historico_jogador = []

    def iniciar_novo_nivel(self):
        self.peso_alvo = random.randint(20, 50)
        self.peso_atual = 0
        self.movimentos_jogador = 0
        self.historico_jogador = []

    def exibir_status(self):
        print("\n" + "="*45)
        print(f"  🔮 CALDEIRA ALQUÍMICA | Alvo: {self.peso_alvo}kg")
        print(f"  Peso Atual: {self.peso_atual}kg | Ingredientes Usados: {self.movimentos_jogador}")
        print("="*45)
        print(" Ingredientes disponíveis:")
        for idx, (nome, peso) in enumerate(self.ingredientes.items(), 1):
            print(f"   [{idx}] {nome:<20} (+{peso}kg)")
        print("   [0] Abandonar Poção (Voltar ao Menu)")
        print("-"*45)

    def animar_caldeirao(self):
        """Exibe uma animação de bolhas subindo dentro de um frasco de vidro"""
        frames = [
            """
                 [ ]
                /   \\
               |     |
               | . o |
               |o . o|
               \\_____/
            """,
            """
                 [ ]
                /   \\
               | . o |
               |o .  |
               |  o .|
               \\_____/
            """,
            """
                 [ ]
                /   \\
               |o . o|
               |  o  |
               |.   o|
               \\_____/
            """,
            """
                 [ ]
                /   \\
               | .   |
               |o . o|
               |  o .|
               \\_____/
            """
        ]

        for _ in range(2):
            for frame in frames:
                limpar_tela()
                print("\n ✨ Infundindo ingredientes no frasco... ✨")
                print(frame)
                time.sleep(0.2)

    def obter_nome_por_peso(self, peso):
        """Retorna o nome do ingrediente baseado no seu peso mágico"""
        for nome, p in self.ingredientes.items():
            if p == peso:
                return nome
        return f"Elemento Desconhecido ({peso}kg)"

    def calcular_rank(self, solucao_perfeita):
        if solucao_perfeita is None:
            return "S (Você alcançou o impossível!)"
        
        if self.movimentos_jogador == solucao_perfeita:
            return "S (Perfeito! Mestre Alquimista)"
        elif self.movimentos_jogador <= solucao_perfeita + 2:
            return "A (Muito bom, mas dava pra otimizar)"
        elif self.movimentos_jogador <= solucao_perfeita + 4:
            return "B (Eficiente, mas gastou ingredientes extras)"
        else:
            return "C (Caldeira instável, usou caminhos muito longos)"

    def exibir_comparativo_final(self, solucao_perfeita, pesos_ideais):
        """Mostra o comparativo entre o que o jogador fez e a previsão do sistema (PD)"""
        print("\n" + "📊" + "—"*50 + "📊")
        print(" RECAPITULAÇÃO DO LABORATÓRIO:")
        print("—"*52)
        
        print(f" Extrato do seu frasco ({len(self.historico_jogador)} itens):")
        if self.historico_jogador:
            for item in self.historico_jogador:
                print(f"  • {item} (+{self.ingredientes[item]}kg)")
        else:
            print("  • Nenhum ingrediente adicionado.")
            
        print("\n Solução Perfeita Prevista pelo Sistema (PD):")
        if solucao_perfeita is not None:
            # Converte os pesos ideais de volta para os nomes comerciais
            for peso in pesos_ideais:
                nome_ideal = self.obter_nome_por_peso(peso)
                print(f"  ✔ {nome_ideal} (+{peso}kg)")
            print(f" Total Ideal de Movimentos: {solucao_perfeita}")
        else:
            print("  • Nenhuma combinação exata era matematicamente possível para este alvo!")
        print("—"*52)

    def jogar(self):
        self.iniciar_novo_nivel()
        valores_ingredientes = list(self.ingredientes.values())
        
        solucao_perfeita, pesos_ideais = calcular_minimo_ingredientes(valores_ingredientes, self.peso_alvo)

        while self.peso_atual < self.peso_alvo:
            limpar_tela()
            self.exibir_status()
            opcao = input(" Escolha um ingrediente (número): ").strip()

            if opcao == '0':
                limpar_tela()
                print("\n Esvaziando a caldeira e limpando o laboratório...")
                time.sleep(1.5)
                return

            if not opcao.isdigit() or int(opcao) < 1 or int(opcao) > len(self.ingredientes):
                print("\n [Erro] Escolha inválida! Tente novamente.")
                time.sleep(1.5)
                continue

            chaves = list(self.ingredientes.keys())
            nome_escolhido = chaves[int(opcao) - 1]
            peso_escolhido = self.ingredientes[nome_escolhido]

            self.peso_atual += peso_escolhido
            self.movimentos_jogador += 1
            self.historico_jogador.append(nome_escolhido)  # Registra no histórico

            self.animar_caldeirao()

            limpar_tela()
            print("\n" + "═"*45)
            print(f" ✨ Celeridade Arcana: Adicionado {nome_escolhido}!")
            print(f" -> Consumo de +1 espaço no inventário da poção.")
            print(f" -> Peso incrementado em +{peso_escolhido}kg.")
            print("═"*45)
            time.sleep(1.8)

            if self.peso_atual > self.peso_alvo:
                limpar_tela()
                print("\n" + "💥"*20)
                print(f" [BOOM!] A CALDEIRA EXPLODIU!")
                print(f" O peso total atingiu {self.peso_atual}kg, passando do limite de {self.peso_alvo}kg.")
                print("💥"*20)
                
                self.exibir_comparativo_final(solucao_perfeita, pesos_ideais)
                input("\nPressione Enter para voltar ao menu principal...")
                break

            if self.peso_atual == self.peso_alvo:
                limpar_tela()
                rank = self.calcular_rank(solucao_perfeita)
                print("\n" + "═"*50)
                print(" ✨ SUCESSO! A POÇÃO FOI CONCLUÍDA COM PRECISÃO! ✨")
                print(f"  RANK OBTIDO: {rank}")
                print("═"*50)
                
                self.exibir_comparativo_final(solucao_perfeita, pesos_ideais)
                input("\nPressione Enter para retornar gloriosamente ao menu...")
                break