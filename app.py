import customtkinter as ct
from tkinter import filedialog
import pandas as pd
from dateutil import parser
from datetime import datetime
import calendar

# Variável global para armazenar o DataFrame
df = None

# Configurações do tema
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

# Função para carregar e exibir o arquivo CSV
def carregar_csv():
    global df
    # Abrir o diálogo para selecionar o arquivo
    arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos CSV", "*.csv")],
        title="Selecione um arquivo CSV"
    )
    if arquivo:
        try:
            # Ler o arquivo CSV
            df = pd.read_csv(arquivo, encoding="latin1")
            # Normalizar os nomes das colunas
            df.columns = [col.strip().lower().replace('í', 'i').replace('ó', 'o') for col in df.columns]
            # Converter as colunas de datas
            df['inicio'] = df['inicio'].apply(parse_data)
            df['fim'] = df['fim'].apply(parse_data)
            # Exibir uma mensagem de sucesso
            texto_resultado.configure(text=f"Arquivo carregado com sucesso!\n{df.head()}")
        except Exception as e:
            texto_resultado.configure(text=f"Erro ao carregar o arquivo: {e}")

# Função para converter datas
def parse_data(data):
    meses_pt = {
        'jan': 'Jan', 'fev': 'Feb', 'mar': 'Mar', 'abr': 'Apr',
        'mai': 'May', 'jun': 'Jun', 'jul': 'Jul', 'ago': 'Aug',
        'set': 'Sep', 'out': 'Oct', 'nov': 'Nov', 'dez': 'Dec'
    }
    if pd.isna(data):
        return pd.NaT
    for pt, en in meses_pt.items():
        data = str(data).lower().replace(pt, en)
    try:
        return parser.parse(data, dayfirst=True)
    except:
        return pd.NaT

# Função para mostrar férias no mês e ano selecionados
def mostrar_ferias():
    global df
    if df is None:
        texto_resultado.configure(text="Nenhum arquivo carregado.")
        return

    try:
        mes = int(combo_mes.get())
        ano = int(combo_ano.get())
    except ValueError:
        texto_resultado.configure(text="Selecione um mês e ano válidos.")
        return

    resultado = f"\n### FÉRIAS EM {calendar.month_name[mes].upper()} {ano} ###\n"
    encontrou = False
    for _, row in df.iterrows():
        if pd.notna(row['inicio']) and pd.notna(row['fim']):
            if row['inicio'].month == mes and row['inicio'].year == ano:
                resultado += f"  {row['nome']} {row['inicio'].strftime('%d/%m/%Y')} a {row['fim'].strftime('%d/%m/%Y')}\n"
                encontrou = True
    if not encontrou:
        resultado += "  Nenhum colaborador de férias nesse mês.\n"

    texto_resultado.configure(text=resultado)

# Função para exportar os dados filtrados para um arquivo CSV
def exportar_csv():
    global df
    if df is None:
        texto_resultado.configure(text="Nenhum arquivo carregado para exportar.")
        return

    arquivo = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("Arquivos CSV", "*.csv")],
        title="Salvar arquivo CSV"
    )
    if arquivo:
        try:
            df.to_csv(arquivo, index=False, encoding="latin1")
            texto_resultado.configure(text=f"Arquivo exportado com sucesso para:\n{arquivo}")
        except Exception as e:
            texto_resultado.configure(text=f"Erro ao exportar o arquivo: {e}")

# Configuração da janela principal
root = ct.CTk()
root.geometry("600x500")
root.title("Leitor de Arquivos CSV")

# Frame principal
frame = ct.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Botão para carregar o arquivo CSV
botao_carregar = ct.CTkButton(
    master=frame,
    text="Carregar Arquivo CSV",
    command=carregar_csv
)
botao_carregar.pack(pady=10)

# Combobox para selecionar o mês
label_mes = ct.CTkLabel(master=frame, text="Selecione o Mês:")
label_mes.pack(pady=5)
combo_mes = ct.CTkComboBox(
    master=frame,
    values=[str(i) for i in range(1, 13)],
    state="readonly"
)
combo_mes.pack(pady=5)

# Combobox para selecionar o ano
label_ano = ct.CTkLabel(master=frame, text="Selecione o Ano:")
label_ano.pack(pady=5)
combo_ano = ct.CTkComboBox(
    master=frame,
    values=[str(i) for i in range(datetime.today().year, datetime.today().year + 5)],
    state="readonly"
)
combo_ano.pack(pady=5)

# Botão para mostrar férias no mês e ano selecionados
botao_mostrar = ct.CTkButton(
    master=frame,
    text="Mostrar Férias",
    command=mostrar_ferias
)
botao_mostrar.pack(pady=10)

# Botão para exportar o arquivo CSV
botao_exportar = ct.CTkButton(
    master=frame,
    text="Exportar Dados para CSV",
    command=exportar_csv
)
botao_exportar.pack(pady=10)

# Texto para exibir mensagens ou resultados
texto_resultado = ct.CTkLabel(
    master=frame,
    text="Selecione um arquivo CSV para começar.",
    wraplength=500,
    justify="left"
)
texto_resultado.pack(pady=20)

# Iniciar o loop principal
root.mainloop()