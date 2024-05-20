# FIFA 23 Dashboard
## Sobre o Projeto
Este projeto foi desenvolvido como parte do aprendizado através de um vídeo no YouTube do canal Asimov Academy. O vídeo que serviu de base para este projeto pode ser encontrado [aqui](https://www.youtube.com/watch?v=0lYBYYHBT5k&t=4911s). Apenas fiz algumas adições no projeto com minhas preferências. 

O FIFA 23 Dashboard é uma aplicação desenvolvida em Python usando as bibliotecas Streamlit e Pandas. Ele oferece uma interface interativa para visualizar dados e informações relacionadas aos jogadores e clubes do jogo FIFA 23.


## Funcionalidades
-  Visualização de estatísticas e dados dos jogadores
- Análise dos clubes
- Comparação entre jogadores


## Base de Dados
O arquivo usado como base de dados foi retirado do Kaggle, um conhecido site de datasets. Você pode baixar o dataset através do botão abaixo:
[Dataset FIFA 23 no Kaggle](https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data).


## Estrutura do Projeto
O projeto está organizado de maneira a otimizar a utilização do Streamlit. O Streamlit trabalha com uma pasta chamada "Pages", onde cada página é um módulo individual. Os módulos são nomeados seguindo o padrão 2_namepage, 3_namepage, e assim por diante, para definir a ordem de exibição no aplicativo.
Apenas a pagina inicial "1_Home.py" ficando de fora da pasta.


## Instalação

## Clone o repositório:
- git clone https://github.com/DanielSR14/DashFIFA23.git
- cd fifa23-dashboard

# Crie um ambiente virtual:
- python -m venv venv
- source venv/bin/activate
- No Windows, use venv\Scripts\activate

# Instale as dependências:
- pip install -r requirements.txt

# Executando o Projeto
Para iniciar a aplicação, execute o seguinte comando:
- streamlit run .\1_Home.py


## Agradecimentos
- [Asimov Academy](https://www.youtube.com/@AsimovAcademy)
- [Kaggle](https://www.kaggle.com)
