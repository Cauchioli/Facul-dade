# Guia Prático: Como Usar Inteligência Artificial no Direito Sem Alucinar

Este guia condensa a metodologia validada em pesquisa acadêmica de Direito e Tecnologia para que você utilize ferramentas de IA (ChatGPT, Claude, Gemini, NotebookLM) com rigor técnico, ética profissional e zero erros grosseiros.

---

## 1. Como um Modelo de Linguagem (LLM) Realmente Funciona

Imagine que alguém comece a seguinte frase e pare no meio:
> *"Água mole em pedra dura..."*

Sua mente completa automaticamente: *"...tanto bate até que fura"*. Você não calculou a física da água nem a geologia da pedra: você completou por puro padrão de repetição estatística.

Um **LLM** (*Large Language Model*) opera exatamente como um **super autocompletar estatístico**:
1. Ele divide o texto em pequenos pedaços chamados *tokens*;
2. Calcula matematicamente qual é a próxima palavra com maior probabilidade de aparecer em sequência.

### Por que a IA inventa jurisprudência (Alucinação)?
Se você abrir um chat genérico e pedir: *"Cite um acórdão do STJ sobre dano moral por inscrição indevida"*, sem conectar a IA a um arquivo oficial, ela não vai consultar o site do tribunal. Ela vai montar um quebra-cabeça verossímil: junta a sigla `REsp`, inventa sete números aleatórios, coloca o nome de um Ministro conhecido e indica uma Turma competente. A citação fica linda e elegante, mas **não existe no mundo real**.

---

## 2. O Protocolo da Tríplice Barreira Forense

Para usar IA em trabalhos da faculdade, estágio ou futura advocacia sem correr riscos, siga sempre as três barreiras:

### Barreira 1: Ingestão e Sigilo
* Nunca envie nomes reais de clientes, CPFs, RGs ou processos em segredo de justiça para chats gratuitos abertos.
* Substitua por `[AUTOR]`, `[RÉU]`, `[EMPRESA]`. Isso protege você sob a LGPD e o art. 7º, XIX, do Estatuto da OAB.

### Barreira 2: Comando Parametrizado e Base Fechada (RAG)
* **Saia do prompt aberto:** Nunca peça *"escreva um trabalho sobre..."* ou *"cite jurisprudência sobre..."* de forma vaga.
* **Use a Fórmula dos 4 Pilares no Prompt:**
  1. **Papel:** *"Atue como pesquisador acadêmico de Direito Processual Civil..."*
  2. **Contexto:** *"Estou analisando o caso [X] sob a ótica da tutela de urgência..."*
  3. **Base de Dados / Travas:** *"Use APENAS os arquivos/leis fornecidos neste chat. É terminantemente proibido inventar artigos ou julgados. Se não encontrar na base fornecida, responda exatamente: 'Não localizado na base'."*
  4. **Saída:** *"Estruture em 3 parágrafos corridos, linguagem formal sem clichês e indique os artigos exatos."*
* **Use ferramentas de ambiente fechado (como o NotebookLM):** Você sobe os PDFs das aulas, livros e leis, e a IA responde citando exatamente a página do seu material, eliminando o risco de invenção.

### Barreira 3: Auditoria Humana na Fonte Primária
* A última palavra é sempre sua.
* Confira **cada artigo de lei** no portal oficial do Planalto (`planalto.gov.br`) e **cada súmula ou precedente** diretamente nos sites do STF, STJ ou Tribunais de Justiça.
