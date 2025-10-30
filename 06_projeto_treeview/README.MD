# Projeto 6: Rastreador de Hábitos

Bem-vindo ao **Rastreador de Hábitos**, um projeto de gestão pessoal focado em ajudar o usuário a criar, acompanhar e manter hábitos saudáveis de forma eficiente e intuitiva.

## Funcionalidades Principais (Core CRUD)

- **Cadastro de Hábitos:** Permite ao usuário criar novos hábitos, informando:
  - `nome_habito`: Nome do hábito a ser rastreado.
  - `descrição`: Breve descrição do hábito.
  - `frequência_desejada`: Com que frequência o usuário deseja praticar o hábito (diário, semanal, etc).
- **Listagem de Hábitos:** Visualização de todos os hábitos cadastrados.
- **Edição de Hábitos:** Alteração de informações de hábitos existentes.
- **Remoção de Hábitos:** Exclusão de hábitos que o usuário não deseja mais acompanhar.

## Desafio Extra: Sistema de Check-in e Sequência (Streak)

- **Check-in Diário:** O usuário pode selecionar um hábito e clicar em "Registrar Hoje" para marcar que realizou o hábito no dia.
- **Exibição de Sequência (Streak):** O sistema calcula e mostra quantos dias consecutivos aquele hábito foi registrado, incentivando o usuário a manter sua rotina sem quebras.
- **Resistência à Quebra de Sequência:** Caso o usuário não registre o hábito em algum dia, a contagem de streak é reiniciada.

## Como Usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/rastreador-de-habitos.git
   cd rastreador-de-habitos
   ```

2. **Instale as dependências** (ajuste conforme a stack utilizada):
   ```bash
   npm install
   ```

3. **Inicie o projeto:**
   ```bash
   npm start
   ```

4. **Acesse no navegador:**  
   `http://localhost:3000`

## Tecnologias Utilizadas

- [ ] (Preencha aqui as tecnologias/frameworks/libraries usadas, ex: React, Node.js, SQLite, etc.)

## Estrutura do Projeto

- `src/`
  - `components/` — Componentes reutilizáveis da interface
  - `pages/` — Páginas principais da aplicação
  - `services/` — Serviços de API/localstorage
  - `utils/` — Funções utilitárias
- `public/` — Arquivos estáticos

## Contribuição

Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests!

## Licença

Este projeto está sob a licença MIT.

---

Bons hábitos, grandes conquistas! 🚀