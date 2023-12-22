# Importar bibliotecas
import random
import seaborn as sns

# Criar classe Academia
class Academia:
    
    # Método construtor
    def __init__(self):
        self.halteres = [i for i in range(10, 100) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    # Método para reiniciar o dia
    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    # Método para listar os halteres
    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
    
    # Método para listar os espaços
    def listar_espacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    # Método para pegar o halter
    def pegar_halter(self, peso):
        halter_pos = list(self.porta_halteres.values()).index(peso)
        key_halter = list(self.porta_halteres.keys())[halter_pos]
        self.porta_halteres[key_halter] = 0
        return peso
    
    # Método para devolver o halter
    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    # Método para calcular o caos
    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)


# Criar classe Usuário
class Usuario:
    # Método construtor
    def __init__(self, tipo, academia):
        self.tipo = tipo  # 1 - Normal | 2 - Bagunceiro
        self.academia = academia
        self.peso = 0

    # Método para iniciar o treino
    def iniciar_treino(self):
        listar_pesos = self.academia.listar_halteres()
        self.peso = random.choice(listar_pesos)
        self.academia.pegar_halter(self.peso)

    # Método para finalizar o treino
    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()

        # Se o usuário for normal
        if self.tipo == 1:
            # Se o peso do halter estiver na lista de espaços
            if self.peso in espacos:
                # Devolve o halter para o espaço
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                # Escolhe um espaço aleatório para devolver o halter
                pos = random.choice(espacos)
                self.academia.devolver_halter(pos, self.peso)
        # Se o usuário for bagunceiro
        if self.tipo == 2:
            # Escolhe um espaço aleatório para devolver o halter
            pos = random.choice(espacos)
            self.academia.devolver_halter(pos, self.peso)

# Criar objeto Academia       
academia = Academia()

# Criar lista de usuários
usuario = [Usuario(1, academia) for i in range(10)]
usuario += [Usuario(2, academia) for i in range(1)]

# Embaralhar a lista de usuários
random.shuffle(usuario)

# Criar lista de caos
list_caos = []

# Executar o programa
for k in range(50):
    academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuario)
        for user in usuario:
            user.iniciar_treino()
        for user in usuario:
            user.finalizar_treino()

    list_caos += [academia.calcular_caos()]


# Plotar o gráfico
sns.displot(list_caos, kde=True)