# Sistema de Autenticação com FastAPI

Este projeto é um sistema de autenticação básico desenvolvido com FastAPI. A primeira versão do projeto foca na criação de usuários.

## Requisitos

- Python 3.7+
- Pip (gerenciador de pacotes do Python)
- SQLite (usado como banco de dados para este projeto)
- Make (para utilizar o Makefile)

## Configuração do Ambiente

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. **Criar o ambiente virtual e instalar dependências**:

    ```bash
    make venv
    make install
    ```

3. **Instalar dependências de desenvolvimento**:

    ```bash
    make install-dev
    ```

## Executando o Projeto

1. **Execute a aplicação**:

    ```bash
    make run
    ```

2. **Acesse a aplicação**:

    Abra o navegador e acesse `http://127.0.0.1:8000`.

## Estrutura do Projeto

```plaintext
auth_api/
│
├── alembic/                                    # Migrações de banco de dados
│
├── app/                                        # Diretório principal da aplicação
│   ├── __init__.py                             # Inicialização do módulo app e definições das rotas da API
│   ├── main.py                                 # Arquivo principal da aplicação
│   │
│   ├── application/                            # Pasta de aplicação com casos de uso
│   │   ├── __init__.py                         # Inicialização do módulo application
│   │   ├── register_user_uc.py                 # Caso de uso de registro de usuário
|   |   └── authentication_uc.py                # Caso de uso de autenticação
│   │
│   ├── models/                                 # Pasta de modelos
│   │   ├── request_models/                     # Pasta de modelos de request
│   │   │   └── register_user.py                # Modelo de requisição de registro de usuário
│   │   ├── response_models/                    # Pasta de modelos de response
│   │   │   └── register_user.py                # Modelo de resposta de registro de usuário
│   │   └── database_models/                    # Pasta de modelos de banco de dados
│   │       └── user.py                         # Modelo de registro de usuário
│   │
│   ├── models/                                 # Pasta de mappers
│   │   ├── mapper_interface.py                 # Interface de mapper
│   │   └── user_mapper.py                      # Mapper de usuário
│   │
│   ├── infrastructure/                         # Pasta de infraestrutura
│   │   ├── __init__.py                         # Inicialização do módulo infrastructure
│   │   ├── config.py                           # Arquivo de configurações e variáveis de ambiente
│   │   └── database_engine.py                  # Arquivo de engine de banco de dados
│   │
│   ├── dto/                                    # Pasta de mappers
│   │   ├── dto_interface.py                    # Interface de dto
│   │   └── user_dto.py                         # Dto de usuário
│   │
│   ├── repository/                             # Pasta de repository
│   │   ├── implementation/                     # Pasta de implementações de repository
│   │   │   └── user_repository.py              # Implementação de repository de usuário
│   │   └── interface/                          # Pasta de interfaces de repository
│   │       └── user_repository.py              # Interface de repository de usuário
│   │
│   ├── service/                                # Pasta de services
│   │   ├── implementation/                     # Pasta de implementações de service
│   │   │   ├── user_service.py                 # Service de usuário
│   │   │   └── secret_service.py               # Service de geração de token
│   │   └── interface/                          # Pasta de interfaces de service
│   │       ├── interface_user_service.py       # Interface de service de usuário
│   │       └── interface_secret_service.py     # Interface de service de geração de token
│   │
│   ├── schemas.py                              # Definições dos schemas da API
│   │
│   ├── utils/                                  # Funções utilitárias
│   │   ├── __init__.py                         # Inicialização do módulo utils
│   │   ├── interface_security.py               # Interface de Hash
│   │   └── security.py                         # Funções de segurança
│   │
│   ├── controller/                             # Pasta de controllers
│   │   ├── __init__.py                         # Inicialização do módulo controller
│   │   ├── authentication_controller.py        # Controller de fluxos de usuário
│   │   └── authentication_controller.py        # Controller de fluxos de autenticação
│   │
│   ├── tags.py                                 # Tags de documentação
│   │
│   └── test/                                   # Pasta de testes
│       ├── integration/                        # Testes de itegração
│       └── conftest.py                         # Configurações de teste
│
├── venv/                                       # Ambiente virtual
│
├── .gitignore                                  # Arquivo para ignorar arquivos e pastas no Git
├── README.md                                   # Documentação do projeto
├── requirements.txt                            # Dependências do projeto
├── requirements-dev.txt                        # Dependências de desenvolvimento
├── setup.py                                    # Script de configuração do projeto
├── .coveragerc                                 # Arquivo para ignorar files no pytest
└── Makefile                                    # Automação de tarefas

```

### Descrição das Pastas e Arquivos

- **alembic/**: Diretório para migrações de banco de dados.
- **app/**: Diretório principal da aplicação.
  - **\_\_init\_\_.py**: Arquivo de inicialização do módulo `app` e definição das rotas da API.
  - **main.py**: Arquivo principal que inicia a aplicação FastAPI.
  - **application/**: Pasta de aplicação com casos de uso.
    - **\_\_init\_\_.py**: Arquivo de inicialização do módulo `application`.
    - **register_user_uc.py**: Caso de uso para registro de usuário.
  - **models/**: Diretório para os modelos Pydantic.
    - **request_models/**: Modelos para requisições (input).
      - **register_user.py**: Modelo de requisição para registro de usuário.
    - **response_models/**: Modelos para respostas (output).
      - **register_user.py**: Modelo de resposta para registro de usuário.
    - **database_models/**: Modelos de banco de dados.
      - **user.py**: Modelo de banco de dados para usuários.
  - **mappers/**: Diretório para mappers de entidades.
    - **mapper_interface.py**: Interface para mappers.
    - **user_mapper.py**: Implementação do mapper para usuários.
  - **dto/**: Diretório para objetos de transferência de dados (DTOs).
    - **dto_interface.py**: Interface para DTOs.
    - **user_dto.py**: Implementação do DTO para usuários.
  - **repository/**: Diretório para repositórios de acesso a dados.
    - **interface/**: Interfaces de repositórios.
      - **user_repository.py**: Interface do repositório de usuários.
    - **implementation/**: Implementações de repositórios.
      - **user_repository.py**: Implementação do repositório de usuários.
  - **service/**: Diretório para serviços da aplicação.
    - **interface_user_service.py**: Interface para o serviço de usuários.
    - **user_service.py**: Implementação do serviço de usuários.
  - **schemas.py**: Definições dos schemas da API.
  - **utils/**: Funções utilitárias.
    - **\_\_init\_\_.py**: Arquivo de inicialização do módulo `utils`.
    - **interface_security.py**: Interface de hash para segurança.
    - **security.py**: Funções de segurança, incluindo hash e validação de senhas.
  - **controller/**: Diretório para os controladores da aplicação.
    - **authentication_controller.py**: Controlador para fluxos de autenticação de usuário.
  - **tags.py**: Definição de tags para a documentação da API.
  - **test/**: Diretório para os testes automatizados.
    - **integration/**: Testes de integração para a aplicação.
    - **conftest.py**: Arquivo de configuração para os testes, como fixtures.

- **venv/**: Ambiente virtual para isolamento de dependências.
- **.gitignore**: Arquivo que especifica quais arquivos/pastas devem ser ignorados pelo Git.
- **README.md**: Documentação principal do projeto.
- **requirements.txt**: Lista de dependências do projeto.
- **requirements-dev.txt**: Lista de dependências para desenvolvimento.
- **setup.py**: Script para configuração e instalação do projeto.
- **Makefile**: Arquivo para automatização de tarefas comuns (opcional).

## Endpoints da API

### Registrar Usuário

- **URL**: `/register`
- **Método**: `POST`
- **Corpo da Requisição**:

    ```json
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }
    ```

- **Respostas**:
    - **201 Created**:
        ```json
        {
            "id": "uuid",
            "username": "string",
            "email": "string",
            "is_active": "boolean",
            "createdAt": "timestamp"
        }
        ```
    - **400 Bad Request**:
        ```json
        {
            "error": "Dados inválidos"
        }
        ```
    - **409 Conflict**:
        ```json
        {
            "error": "Username ou email já existente"
        }
        ```

## Testes

Para executar os testes, use o comando:

```bash
make test
```

## Documentação

A documentação da API é gerada automaticamente pelo FastAPI e pode ser acessada em:

- `http://127.0.0.1:8000/docs` (Swagger)
- `http://127.0.0.1:8000/redoc` (ReDoc)


## Padrão de Commits

Estamos utilizando o [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) como padrão para nossos commits. Este padrão ajuda a manter um histórico de commits claro e consistente, além de facilitar a automação de processos como geração de changelogs e versionamento semântico.

### Estrutura do Commit

Um commit no padrão de Conventional Commits segue a estrutura:

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé opcional]
```

### Tipos Comuns

- **feat**: Uma nova funcionalidade.
- **fix**: Correção de um bug.
- **docs**: Mudanças na documentação.
- **style**: Alterações que não afetam o significado do código (espaços em branco, formatação, etc.).
- **refactor**: Mudanças no código que não corrigem bugs nem adicionam funcionalidades.
- **test**: Adição ou modificação de testes.
- **chore**: Tarefas auxiliares (atualização de dependências, scripts de build, etc.).
- **perf**: Melhorias de desempenho.
- **build**: Mudanças que afetam o sistema de build ou dependências externas.
- **ci**: Mudanças na configuração de CI (integração contínua).

### Exemplos de Commits

#### feat

Adicionando uma nova funcionalidade:

```
feat: adicionar endpoint de registro de usuário
```

#### fix

Corrigindo um bug:

```
fix: corrigir falha na validação de e-mail no registro de usuário
```

#### docs

Atualizando a documentação:

```
docs: adicionar seção de instalação no README
```

#### style

Ajustes de formatação:

```
style: corrigir indentação em authentication_controller.py
```

#### refactor

Refatoração de código:

```
refactor: mover lógica de autenticação para um serviço separado
```

#### test

Adicionando testes:

```
test: adicionar testes unitários para o serviço de autenticação
```

#### chore

Tarefas auxiliares:

```
chore: atualizar dependências no requirements.txt
```

### Corpo e Rodapé (Opcional)

- **Corpo**: Use para fornecer uma descrição mais detalhada do que foi feito e por que.
- **Rodapé**: Use para informações adicionais, como fechamento de issues (e.g., `Closes #123`).

### Exemplo Completo

Um commit mais completo pode parecer assim:

```
feat(auth): adicionar endpoint de login

Adiciona o endpoint de login com autenticação JWT.
Valida as credenciais e retorna um token de acesso.

Closes #45
```

### Implementação no Projeto

1. **Configurar um Commit Linter**: Utilize ferramentas como `commitlint` e `husky` para forçar a conformidade com o padrão de commits.
2. **Documentar o Padrão**: Adicione esta seção no seu README ou no CONTRIBUTING.md explicando o padrão de commits que você está seguindo.

Seguindo esses padrões, teremos um histórico de commits mais claro e fácil de seguir, o que é benéfico para toda a equipe de desenvolvimento e para qualquer colaborador futuro no projeto.
```

Adicionar essa seção ao seu README ou CONTRIBUTING.md ajudará todos os colaboradores a seguir o mesmo padrão de commits, promovendo consistência e clareza no desenvolvimento do projeto.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Para isso, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma nova branch com a sua feature: `git checkout -b minha-feature`.
3. Commit suas mudanças: `git commit -m 'Adiciona minha feature'`.
4. Push para a branch: `git push origin minha-feature`.
5. Envie um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.
```

Adicione este conteúdo ao seu arquivo `README.md` no repositório do seu projeto. Ele fornece uma visão geral do projeto, instruções de configuração e execução, detalhes sobre os endpoints da API e informações sobre como contribuir.

Se precisar de mais alguma coisa, estou à disposição!