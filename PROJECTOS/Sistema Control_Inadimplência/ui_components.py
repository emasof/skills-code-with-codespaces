from PyQt6.QtWidgets import QTabWidget, QVBoxLayout, QWidget, QLabel, QMenu
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

def setup_tabs(window):
    tab_widget = QTabWidget()

    # Configurar abas
    data_tab = QWidget()
    report_tab = QWidget()
    graph_tab = QWidget()

    tab_widget.addTab(data_tab, "Dados Carregados")
    tab_widget.addTab(report_tab, "Relatórios")
    tab_widget.addTab(graph_tab, "Gráficos")

    # Configurar layouts para cada aba
    setup_data_tab(data_tab)
    setup_report_tab(report_tab)
    setup_graph_tab(graph_tab)

    window.setCentralWidget(tab_widget)
    return tab_widget

def setup_data_tab(tab):
    layout = QVBoxLayout()
    label = QLabel("Aba Dados Carregados (em desenvolvimento)")
    layout.addWidget(label)
    tab.setLayout(layout)

def setup_report_tab(tab):
    layout = QVBoxLayout()
    label = QLabel("Aba Relatórios (em desenvolvimento)")
    layout.addWidget(label)
    tab.setLayout(layout)

def setup_graph_tab(tab):
    layout = QVBoxLayout()
    placeholder_label = QLabel("Gráficos em desenvolvimento")
    placeholder_label.setStyleSheet("font-size: 16px; color: gray;")
    placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(placeholder_label)
    tab.setLayout(layout)

def create_menu(window):
    menu_bar = window.menuBar()
    file_menu = menu_bar.addMenu("Arquivo")

    # Opção de carregar arquivo
    load_action = QAction("Carregar Arquivo", window)
    load_action.triggered.connect(window.load_file)  # Conectar ao método no MainWindow
    file_menu.addAction(load_action)

    # Menu de relatório com subopções
    report_menu = QMenu("Gerar Relatório de Inadimplentes >", window)

    view_report_action = QAction("Exibir Relatório", window)
    view_report_action.triggered.connect(window.show_report)  # Conectar ao método no MainWindow
    report_menu.addAction(view_report_action)

    export_report_action = QAction("Exportar Relatório", window)
    export_report_action.triggered.connect(window.export_report)  # Conectar ao método no MainWindow
    report_menu.addAction(export_report_action)

    file_menu.addMenu(report_menu)
