from tarefa import Tarefa

class GestorTarefas:
    def __init__(self):
        self.tarefas = []
    def adicionarTarefa(self):
        while True:
            t_id = input("Escreve o id da tarefa: ")
            t_titulo = input("Escreve o título da tarefa: ")
            t_descricao = input("Escreve a descrição da tarefa: ")
            
            while True:
                t_prioridade = int(input("Escreve a prioridade da tarefa de 0 a 5 cendo 0 com menos prioridade e 5 com maior prioridade: "))
                if t_prioridade >5:
                    print("O numero tem que ser menor que 5")
                elif t_prioridade <0:
                    print("O numero tem que ser maior que 0")
                else:
                    break
            
            while True:
                estados_validos= ("pendente", "em curso", "concluída", "cancelada")
                t_estado = input("Escreve o estado da tarefa (pendente, em curso, concluída, cancelada): ").lower()
                if t_estado not in estados_validos:
                    print("Tem de escolher entre: pendente, em curso, concluida ou cancelada")
                else:
                    break
            while True:
                t_dataCriacao = input("Escreve a data de criação (DD/MM/AAAA): ")
                if len(t_dataCriacao) == 10 and t_dataCriacao[2:3] == "/" and t_dataCriacao[5:6] == "/":
                    dia = t_dataCriacao[0:2]
                    mes = t_dataCriacao[3:5]
                    ano = t_dataCriacao[6:10]
                    if dia.isdigit() and mes.isdigit() and ano.isdigit():
                        break
                print("Erro: A estrutura da data tem que ser DD/MM/AAAA (ex: 25/05/2026)")
            while True:
                t_dataLimite = input("Escreve a data limite (DD/MM/AAAA): ")
                if len(t_dataLimite) == 10 and t_dataLimite[2:3] == "/" and t_dataLimite[5:6] == "/":
                    dia = t_dataLimite[0:2]
                    mes = t_dataLimite[3:5]
                    ano = t_dataLimite[6:10]
                    if dia.isdigit() and mes.isdigit() and ano.isdigit():
                        break
                print("Erro: A estrutura da data tem que ser DD/MM/AAAA (ex: 31/12/2026)")
            
            while True:
                t_categoria = input("Escreve a categoria da tarefa (escolar, trabalho, casa, geral): ").lower()
                categoriaValida= ("escolar", "trabalho", "casa", "geral")
                if t_categoria not in categoriaValida:
                    print("Tem de escolher entre: escolar, trabalho, casa ou geral")
                else:
                    break
            
            novaTarefa = Tarefa(t_id, t_titulo, t_descricao, t_prioridade, t_estado, t_dataCriacao, t_dataLimite,t_categoria )
            self.tarefas.append(novaTarefa)
            break
        
    def mostrarTarefa(self):
        if not self.tarefas:
            print("\nNão existem tarefas registadas.")
            return
        for tarefa in self.tarefas:
            tarefa.detalhes_tarefa()
    
    def detalhes_de_uma_tarefa(self):
        idTarefa= input("\nEscreve o id da tarefa que queres pesquisar: ")
        encontrada= False
        if self.tarefas == []:
            print("Ainda não existe tarefas!!")
        else:
            for i in self.tarefas:
                if i.id == idTarefa:
                    i.detalhes_tarefa()
                    encontrada= True
            if not encontrada:
                print(f"Não foi encontrado nenhuma tarefa com o id {idTarefa}")
    
    def alterar_dados(self):
        idTarefa= input("\nEscreve o id da tarefa que queres alterar: ")
        encontrada= False
        if self.tarefas == []:
            print("Ainda não existe tarefas!!")
        else:
            for i in self.tarefas:
                if i.id == idTarefa:
                    encontrada= True
                    while True:
                        print ("-----Escolhe a opcão para alterares o que quiseres na tarefa-----")
                        print("1- Mudar ID")
                        print("2- Mudar Titúlo")
                        print("3- Mudar Descrição")
                        print("4- Mudar Prioridade")
                        print("5- Mudar Estado")
                        print("6- Mudar Data de criação")
                        print("7- Mudar Data limite")
                        print("8- Mudar categoria")
                        print("9- Mudar tudo")
                        print("0- Sair")
                        opcao= int(input("Escolhe a opcão aqui: "))
                        if opcao == 1:
                            i.id= input("Escreve um novo id para esta tarefa: ")
                        
                        elif opcao == 2:
                            i.titulo = input("Escreve um novo titúlo para esta tarefa: ")
                        
                        elif opcao == 3:
                            i.descricao = input("Escreve uma nova descrição para esta tarefa: ")
                        
                        elif opcao == 4:
                            while True:
                                    i.prioridade = int(input("Escreve uma nova prioridade de 0 a 5 cendo 0 com menos prioridade e 5 com maior prioridade: "))
                                    if i.prioridade >5:
                                        print("O numero tem que ser menor que 5")
                                    elif i.prioridade <0:
                                        print("O numero tem que ser maior que 0")
                                    else:
                                        break
                        
                        elif opcao == 5:
                            while True:
                                estados_validos= ("pendente", "em curso", "concluída", "cancelada")
                                i.estado = input("Escreve um novo estado para esta tarefa: ").lower()
                                if i.estado not in estados_validos:
                                    print("Tem de escolher entre: pendente, em curso, concluída ou cancelada")
                                else:
                                    break
                                
                        elif opcao == 6:
                            while True:
                                i.data_criacao = input("Escreve uma nova data de criação para esta tarefa:  ")
                                if len(i.data_criacao) == 10 and i.data_criacao[2:3] == "/" and i.data_criacao[5:6] == "/":
                                    dia = i.data_criacao[0:2]
                                    mes = i.data_criacao[3:5]
                                    ano = i.data_criacao[6:10]
                                    if dia.isdigit() and mes.isdigit() and ano.isdigit():
                                        break
                                print("Erro: A estrutura da data tem que ser DD/MM/AAAA (ex: 25/05/2026)")
                                
                        
                        elif opcao == 7:
                            while True:
                                i.data_limite = input("Escreve uma nova data de limite para esta tarefa:  ")
                                if len(i.data_limite) == 10 and i.data_limite[2:3] == "/" and i.data_limite[5:6] == "/":
                                    dia = i.data_limite[0:2]
                                    mes = i.data_limite[3:5]
                                    ano = i.data_limite[6:10]
                                    if dia.isdigit() and mes.isdigit() and ano.isdigit():
                                        break
                                print("Erro: A estrutura da data tem que ser DD/MM/AAAA (ex: 31/12/2026)")
                        
                        elif opcao == 8:
                            while True:
                                i.categoria = input("Escreve uma novo categoria para esta tarefa: ").lower()
                                categoriaValida= ("escolar", "trabalho", "casa", "geral")
                                if i.categoria not in categoriaValida:
                                    print("Tem de escolher entre: escolar, trabalho, casa ou geral")
                                else:
                                    break
                        
                        elif opcao == 9:
                            i.id= input("Escreve um novo id para esta tarefa: ")
                            
                            i.titulo = input("Escreve um novo titúlo para esta tarefa: ")
                            
                            i.descricao = input("Escreve uma nova descrição para esta tarefa: ")
                            
                            while True:
                                    i.prioridade = int(input("Escreve uma nova prioridade de 0 a 5 cendo 0 com menos prioridade e 5 com maior prioridade: "))
                                    if i.prioridade >5:
                                        print("O numero tem que ser menor que 5")
                                    elif i.prioridade <0:
                                        print("O numero tem que ser maior que 0")
                                    else:
                                        break
                            
                            while True:
                                estados_validos= ("pendente", "em curso", "concluída", "cancelada")
                                i.estado = input("Escreve um novo estado para esta tarefa: ").lower()
                                if i.estado not in estados_validos:
                                    print("Tem de escolher entre: pendente, em curso, concluída ou cancelada")
                                else:
                                    break
                            
                            while True:
                                i.data_criacao = input("Escreve uma nova data de criação para esta tarefa:  ")
                                if len(i.data_criacao) == 10 and i.data_criacao[2:3] == "/" and i.data_criacao[5:6] == "/":
                                    dia = i.data_criacao[0:2]
                                    mes = i.data_criacao[3:5]
                                    ano = i.data_criacao[6:10]
                                    if dia.isdigit() and mes.isdigit() and ano.isdigit():
                                        break
                                print("Erro: A estrutura da data tem que ser DD/MM/AAAA (ex: 25/05/2026)")
                            
                            while True:
                                i.data_limite = input("Escreve uma nova data de limite para esta tarefa:  ")
                                if len(i.data_limite) == 10 and i.data_limite[2:3] == "/" and i.data_limite[5:6] == "/":
                                    dia = i.data_limite[0:2]
                                    mes = i.data_limite[3:5]
                                    ano = i.data_limite[6:10]
                                    if dia.isdigit() and mes.isdigit() and ano.isdigit():
                                        break
                                print("Erro: A estrutura da data tem que ser DD/MM/AAAA (ex: 31/12/2026)")
                            
                            while True:
                                i.categoria = input("Escreve uma novo categoria para esta tarefa: ").lower()
                                categoriaValida= ("escolar", "trabalho", "casa", "geral")
                                if i.categoria not in categoriaValida:
                                    print("Tem de escolher entre: escolar, trabalho, casa ou geral")
                                else:
                                    break
                        
                        
                        elif opcao == 0:
                            break
                    break
            if not encontrada:
                print(f"Não foi encontrado nenhuma tarefa com o id {idTarefa}")
    def tarefa_concluida(self):
        
        idTarefa= input("\nEscreve o id da tarefa que queres por como concluída: ")
        encontrada= False
        if self.tarefas == []:
            print("Ainda não existe tarefas!!")
        else:
            for i in self.tarefas:
                if i.id == idTarefa:
                    if i.estado == "concluída":
                        print("Esta tarefa já estáva concluída")
                    
                    else:
                        i.estado = "concluída"
                        print("Tarefa posta como 'concluida' com sucesso!!")
                    encontrada= True
            if not encontrada:
                print(f"Não foi encontrado nenhuma tarefa com o id {idTarefa}")
    
    def revmover_tarefa(self):
        idTarefa= input("\nEscreve o id da tarefa que queres remover: ")
        encontrada= False
        if self.tarefas == []:
            print("Ainda não existe tarefas!!")
            
        else:
            for i in self.tarefas:
                if i.id == idTarefa:
                    self.tarefas.remove(i)
                    print("Tarefa removida com sucesso!!")
                    encontrada= True
                    break
            if not encontrada:
                print(f"Não foi encontrado nenhuma tarefa com o id {idTarefa}")
    
    def pesquisar_por_texto(self):
        if self.tarefas == []:
            print("Ainda não existe tarefas!!")
            return
        
        tituloTarefa= input("\nEscreve alguma coisa para encontrares a tarefa desejada: ").lower()
        resultados = [i for i in self.tarefas if tituloTarefa in i.titulo.lower() or tituloTarefa in i.descricao.lower()]
        
        if not resultados:
            print(f"\nNão foram encontradas tarefas com o texto '{tituloTarefa}'.")
        else:
            print(f"\n--- Foram encontradas {len(resultados)} tarefa(s) ---")
            for tarefa in resultados:
                tarefa.detalhes_tarefa()
    
    def filtrar(self):
        if self.tarefas == []:
            print("Ainda não existe tarefas!!")
            return
        while True:
            estado_tarefa= input("Escreve o estádo (pendente, em curso, concluída, cancelada): ").lower()
            estados_validos= ("pendente", "em curso", "concluída", "cancelada")
            if estado_tarefa not in estados_validos: 
                print("Tem de escolher entre: pendente, em curso, concluída ou cancelada")
            else:
                resultados = [i for i in self.tarefas if i.estado == estado_tarefa]
                    
                if not resultados:
                    print(f"\nNão foram encontradas tarefas com o este estádo '{estado_tarefa}'.")
                else:
                    print(f"\n--- Foram encontradas {len(resultados)} tarefa(s) com este estádo ---")
                    for tarefa in resultados:
                        tarefa.detalhes_tarefa()
                break
    
    def estatistica(self):
        if self.tarefas == []:
            print("Ainda não existem tarefas para ver as estatísticas!!")
            return
        c_pendente = 0
        c_em_curso = 0
        c_concluida = 0
        c_cancelada = 0
        
        c_categoria_escolar= 0
        c_categoria_trabalho= 0
        c_categoria_casa= 0
        c_categoria_geral= 0
        
        for i in self.tarefas:
            estado= i.estado
            if estado == "pendente":
                c_pendente = c_pendente + 1
            elif estado == "em curso":
                c_em_curso = c_em_curso + 1
            elif estado == "concluída":
                c_concluida = c_concluida + 1
            elif estado == "cancelada":
                c_cancelada = c_cancelada + 1
                
            categoria = i.categoria
            if categoria == "escolar":
                c_categoria_escolar = c_categoria_escolar + 1
            elif categoria == "trabalho":
                c_categoria_trabalho = c_categoria_trabalho + 1
            elif categoria == "casa":
                c_categoria_casa = c_categoria_casa + 1
            elif categoria == "geral":
                c_categoria_geral= c_categoria_geral +1
                
        
        estatisticas_prioridades = {prio: 0 for prio in range(6)}
        for i in self.tarefas:
            p = i.prioridade
            if p in estatisticas_prioridades:
                estatisticas_prioridades[p] += 1
        
        total_tarefas = len(self.tarefas)
        
        print("\n---- Estatísticas das tarefas ----\n")
        print(f"Total de tarefas no sistema: {total_tarefas}")
        print("-" * 35)
        print("Tarefas por Estado:")
        print(f"  - Pendentes:   {c_pendente}")
        print(f"  - Em curso:    {c_em_curso}")
        print(f"  - Concluídas:  {c_concluida}")
        print(f"  - Canceladas:  {c_cancelada}")
        print("-" * 35)
        print("Tarefas por Prioridade:")
        for prioridade, quantidade in estatisticas_prioridades.items():
            print(f"  - Prioridade {prioridade}: {quantidade} tarefa(s)")
        print("-" * 35)
        print("Tarefas por categoria:")
        print(f"  - Escolar:     {c_categoria_escolar}")
        print(f"  - Trabalho:    {c_categoria_trabalho}")
        print(f"  - Casa:        {c_categoria_casa}")
        print(f"  - Geral:       {c_categoria_geral}")
        print("-" * 35)
        



