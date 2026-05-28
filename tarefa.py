class Tarefa:
    def __init__(self, id:str, titulo:str, descricao:str, prioridade:int, estado:str, data_criacao:str, data_limite:str, categoria: str):
        self.id=id
        self.titulo=titulo
        self.descricao=descricao
        self.prioridade=prioridade
        self.estado=estado
        self.data_criacao=data_criacao
        self.data_limite=data_limite
        self.categoria=categoria
    def detalhes_tarefa(self):
        print("\n======================================================================")
        print(f"      Detalhes da tarefa {self.id} | Categoria: {self.categoria}       ")
        print("========================================================================")
        print(f"ID:           {self.id}")
        print(f"Título:       {self.titulo}")
        print(f"Descrição:    {self.descricao}")
        print(f"Prioridade:   {self.prioridade}")
        print(f"Estado:       {self.estado}")
        print(f"Criada em:    {self.data_criacao}")
        print(f"Prazo limite: {self.data_limite}")
        print("========================================================================\n")
        