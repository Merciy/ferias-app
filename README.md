# 🗓️ Controle de Férias - Python

Aplicação em Python com interface gráfica para controle de férias de colaboradores. Permite visualizar quem está de férias no mês atual, no próximo mês e nos próximos 6 meses. O projeto gera um `.exe` automaticamente para Windows via GitHub Actions.

---

## 🚀 Funcionalidades

- 📅 Leitura de um arquivo `ferias.csv` com os dados dos colaboradores
- 🔍 Filtros por mês atual, próximo mês e próximos 6 meses
- 📤 Exportação dos dados para CSV ou Excel
- 💻 Interface amigável (Tkinter)
- 🪄 Geração automática de `.exe` para Windows via GitHub Actions
- 👨‍💻 Desenvolvido por 🥽[@Merciy](https://github.com/Merciy) com apoio de 🧿[@otavioays](https://github.com/otavioays) 🚀


---

## 📦 Tecnologias usadas

- Python 3.13.2
- Pandas
- Tkinter
- PyInstaller
- GitHub Actions (para build automático)

---

## 🛠️ Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/Merciy/ferias-app.git
cd NOME_DO_REPO
```

2. Crie um ambiente virtual e ative:

```bash
python3 -m venv venv
source venv/bin/activate  # no macOS/Linux
venv\Scripts\activate   # no Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode o app:

```bash
python app.py
```

---

## 🧪 Arquivo de exemplo

Se quiser testar com um exemplo, crie um arquivo `ferias.csv` com colunas como:

```csv
Nome,Data Início,Data Fim
Maria,01-Jan-2025,15-Jan-2025
João,20-Fev-2025,28-Fev-2025
```

---

## 🧱 Geração de .exe

Ao fazer `push` para a branch `main`, o GitHub Actions irá gerar automaticamente um `.exe` do projeto usando PyInstaller. O executável ficará disponível na aba **Actions** > workflow > Artifacts.

---

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
