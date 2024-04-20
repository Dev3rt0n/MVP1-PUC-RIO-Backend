# Portal CorpTeams

## Sobre o Projeto
**CorpTeams** é uma plataforma inovadora que permite **organizar times** dentro de uma organização, facilitando a gestão de projetos e a colaboração entre equipes. Com uma interface intuitiva e recursos poderosos, o CorpTeams é a solução ideal para empresas que buscam otimizar seus processos internos.

## Funcionalidades
- **Gerenciamento de Equipes**: Crie e gerencie equipes com facilidade.
- **Atribuição de Tarefas**: Distribua tarefas e acompanhe o progresso.
- **Comunicação Integrada**: Mantenha sua equipe alinhada com ferramentas de comunicação.

## Começando

### Pré-requisitos
Antes de iniciar, certifique-se de ter o seguinte instalado:
- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)

### Instalação
Para instalar as dependências necessárias, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

### Configuração do Banco de Dados
Para criar o banco de dados e inserir os dados iniciais, execute:

```bash
python create_db.py
```

### Uso
Após a configuração, você pode iniciar o servidor com o seguinte comando:

```
flask run
```

Acesse `http://localhost:5000` no seu navegador para confirmar se o servidor está no ar e
`http://localhost:5000/swagger` para verificar a documentação da API

