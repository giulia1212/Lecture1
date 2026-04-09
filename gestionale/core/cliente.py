
# questo è un DTO

from dataclasses import dataclass

@dataclass
class ClienteRecord:
    nome: str
    mail: str
    categoria: str

    def __hash__(self):                 # due oggetti DTO sono uguali se hanno la stessa chiave primaria
        return hash(self.mail)

    def __eq__(self, other):
        return self.mail == other.mail


    def __str__(self):
        return f"{self.nome} -- {self.mail} ({self.categoria})"