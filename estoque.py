import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox, QLabel

# Dicionário para armazenar os produtos
estoque = {}

# Funções para gerenciar o estoque
def adicionar_produto():
    codigo, ok = QInputDialog.getText(None, "Adicionar Produto", "Digite o código do produto:")
    if not ok or not codigo:
        return
    if codigo in estoque:
        QMessageBox.critical(None, "Erro", f"Produto com código {codigo} já existe.")
        return

    nome, ok = QInputDialog.getText(None, "Adicionar Produto", "Digite o nome do produto:")
    descricao, ok = QInputDialog.getText(None, "Adicionar Produto", "Digite a descrição do produto:")
    quantidade, ok = QInputDialog.getInt(None, "Adicionar Produto", "Digite a quantidade do produto:")
    preco, ok = QInputDialog.getDouble(None, "Adicionar Produto", "Digite o preço do produto:")

    estoque[codigo] = {
        'nome': nome,
        'descricao': descricao,
        'quantidade': quantidade,
        'preco': preco
    }
    QMessageBox.information(None, "Sucesso", f"Produto {nome} adicionado com sucesso.")

def atualizar_produto():
    codigo, ok = QInputDialog.getText(None, "Atualizar Produto", "Digite o código do produto a ser atualizado:")
    if not ok or not codigo or codigo not in estoque:
        QMessageBox.critical(None, "Erro", f"Produto com código {codigo} não encontrado.")
        return

    nome, ok = QInputDialog.getText(None, "Atualizar Produto", "Digite o novo nome do produto (ou deixe em branco para manter o atual):")
    descricao, ok = QInputDialog.getText(None, "Atualizar Produto", "Digite a nova descrição do produto (ou deixe em branco para manter a atual):")
    quantidade, ok = QInputDialog.getInt(None, "Atualizar Produto", "Digite a nova quantidade do produto (ou deixe em branco para manter a atual):")
    preco, ok = QInputDialog.getDouble(None, "Atualizar Produto", "Digite o novo preço do produto (ou deixe em branco para manter o atual):")

    if nome:
        estoque[codigo]['nome'] = nome
    if descricao:
        estoque[codigo]['descricao'] = descricao
    if quantidade is not None:
        estoque[codigo]['quantidade'] = quantidade
    if preco is not None:
        estoque[codigo]['preco'] = preco

    QMessageBox.information(None, "Sucesso", f"Produto {codigo} atualizado com sucesso.")

def remover_produto():
    codigo, ok = QInputDialog.getText(None, "Remover Produto", "Digite o código do produto a ser removido:")
    if not ok or not codigo or codigo not in estoque:
        QMessageBox.critical(None, "Erro", f"Produto com código {codigo} não encontrado.")
        return

    del estoque[codigo]
    QMessageBox.information(None, "Sucesso", f"Produto {codigo} removido com sucesso.")

class EstoqueApp(QWidget):
    def __init__(self):
        super().__init__()
        self.janela_estoque = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sistema de Gerenciamento de Estoque")
        layout = QVBoxLayout()

        btn_adicionar = QPushButton("Adicionar Produto")
        btn_adicionar.clicked.connect(adicionar_produto)
        layout.addWidget(btn_adicionar)

        btn_atualizar = QPushButton("Atualizar Produto")
        btn_atualizar.clicked.connect(atualizar_produto)
        layout.addWidget(btn_atualizar)

        btn_remover = QPushButton("Remover Produto")
        btn_remover.clicked.connect(remover_produto)
        layout.addWidget(btn_remover)

        btn_visualizar = QPushButton("Visualizar Estoque")
        btn_visualizar.clicked.connect(self.visualizar_estoque)
        layout.addWidget(btn_visualizar)

        btn_sair = QPushButton("Sair")
        btn_sair.clicked.connect(QApplication.quit)
        layout.addWidget(btn_sair)

        self.setLayout(layout)

    def visualizar_estoque(self):
        if not estoque:
            QMessageBox.information(None, "Estoque Vazio", "Nenhum produto no estoque.")
            return

        if self.janela_estoque is None:
            self.janela_estoque = QWidget()
            self.janela_estoque.setWindowTitle("Estoque Atual")
        
        layout = QVBoxLayout()

        for codigo, dados in estoque.items():
            layout.addWidget(QLabel(f"Código: {codigo}"))
            layout.addWidget(QLabel(f"  Nome: {dados['nome']}"))
            layout.addWidget(QLabel(f"  Descrição: {dados['descricao']}"))
            layout.addWidget(QLabel(f"  Quantidade: {dados['quantidade']}"))
            layout.addWidget(QLabel(f"  Preço: {dados['preco']}"))
            layout.addWidget(QLabel("-----------------------------"))

        self.janela_estoque.setLayout(layout)
        self.janela_estoque.show()

def main():
    app = QApplication(sys.argv)
    window = EstoqueApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
