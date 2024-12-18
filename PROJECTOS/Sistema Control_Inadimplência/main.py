# =========================
# main.py (Arquivo Principal)
# =========================

import sys
from utils import validate_and_format_data
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_components import setup_tabs, create_menu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Controle de Inadimplência")
        self.setGeometry(100, 100, 800, 600)

        # Conexão com o banco de dados
        from database import connect_to_db, create_table
        self.db_connection = connect_to_db()
        create_table(self.db_connection)

        # Configuração da interface
        from ui_components import setup_tabs, create_menu
        self.tab_widget = setup_tabs(self)
        create_menu(self)

        # Configurar abas e menu
        self.tab_widget = setup_tabs(self)
        create_menu(self)

    def show_report(self):
        # Exemplo: Exibir um relatório simples na aba Relatórios
        try:
            # Consulta para dados fictícios de inadimplentes
            query = "SELECT * FROM credit_data WHERE days > 30"
            cursor = self.db_connection.cursor()
            results = cursor.execute(query).fetchall()

            # Obter os nomes das colunas
            columns = [description[0] for description in cursor.description]

            # Criar um DataFrame para exibir os dados
            import pandas as pd
            report_data = pd.DataFrame(results, columns=columns)

            # Exibir os dados na aba Relatórios
            self.populate_table(self.tab_widget.widget(1).layout().itemAt(0).widget(), report_data)
            print("Relatório exibido com sucesso.")
        except Exception as e:
            print(f"Erro ao exibir relatório: {e}")



    # Carregar Arquivo
    def load_file(self):
        # Abrir seletor de arquivo
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecione um arquivo Excel", "", "Excel Files (*.xls *.xlsx)")

        if not file_path:  # Verificar se o usuário selecionou um arquivo
            print("Nenhum arquivo selecionado.")
            return

        try:
            # Ler o arquivo Excel
            data = pd.read_excel(file_path)

            # Validar e formatar dados
            data = self.validate_and_format_data(data)

            # Atualizar banco de dados
            from database import connect_to_db, create_table  # Certifique-se de importar as funções do módulo correto
            connection = connect_to_db()
            create_table(connection)
            self.update_database(data, connection)

            # Exibir os dados na tabela
            self.populate_table(self.tab_widget.widget(0).layout().itemAt(1).widget(),
                                data)  # Exibir na aba Dados Carregados

            print(f"Arquivo carregado com sucesso: {file_path}")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())