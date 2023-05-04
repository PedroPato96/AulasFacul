from desktop import Desktop
from notebook import Notebook

# Cria objetos Desktop e Notebook
desktop = Desktop("Dell", "Preto", 2500.00, 500)
notebook = Notebook("Lenovo", "Prata", 3000.00, 8)

# Exibir infos computadores
print(desktop.getInformacoes())
print(notebook.getInformacoes())
