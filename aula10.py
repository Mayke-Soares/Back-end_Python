class Pessoa:
  def __init__(self, nome, idade, altura):
    self.nome = nome
    self.idade = idade
    self.altura = altura

  def ver_nome(self):
    print(f"Meu nome é {self.nome}")

  def falar(self, texto):
    print(f"{self.nome}: {texto}")

  def alterar_nome(self, novo_nome):
    self.nome = novo_nome

    # Instancia um objeto da Classe "Pessoa"
ramon = Pessoa(nome='Ramon', idade=29, altura=1.78)

# Chama os métodos de "Pessoa"
ramon.ver_nome()
ramon.falar('Fala Siô')
ramon.alterar_nome("Artur")
ramon.ver_nome()
ramon.falar('Fala Gênio')