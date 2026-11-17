# Direito OS : Kit Acadêmico e Segundo Cérebro para Estudantes de Direito

Um repositório estruturado para transformar qualquer Agente de IA (Antigravity, Claude Code, Cursor, Gemini CLI) em um assistente jurídico acadêmico rigoroso, focado em **estudo ativo, trabalhos nas normas ABNT, preparação progressiva para a OAB, estágio/NPJ e TCC sem alucinações**.

> Construído e validado na prática acadêmica do curso de Direito (do ciclo intermediário até a aprovação de TCC com nota máxima e indicação de publicação). Totalmente livre de dados pessoais e pronto para personalizar.

---

## O Que Vem Neste Kit (Panorama Geral)

### 1. Habilidades Especializadas para o Agente (`.gemini/skills/`)
* **`abnt-trabalhos-academicos`:** Regras completas das normas NBR 14724 (estrutura e margens), NBR 6023 (referências), NBR 10520 (citações), NBR 6024 e NBR 6028.
* **`tcc-e-banca-nota-10`:** Metodologia anti-alucinação para pesquisa jurídica, protocolo da Tríplice Barreira, estruturação de slides limpos para banca e técnica de escrita natural (sem "cara de IA").
* **`estudo-e-revisao-direito`:** Método de estudo em 4 camadas (Lei Seca -> Aplicação Prática -> Súmulas/Jurisprudência -> Questões FGV/OAB + Técnica de Feynman).
* **`npj-e-pecas-praticas`:** Organização de atendimentos e estágios, roteiro de peças processuais e regras estritas de anonimização (LGPD + Estatuto da OAB).

### 2. Geradores Automáticos em Python (`scripts/`)
* **`gerar_abnt_docx.py`:** Cria arquivos `.docx` do Word já formatados com papel A4, margens 3-3-2-2 cm, fonte Arial 12, espaçamento 1,5, recuo 1,25 cm, paginação superior direita a partir da página 2 e referências alinhadas à esquerda.
* **`gerar_slides_clean.py`:** Cria apresentações `.pptx` em 16:9 com design limpo e legível para seminários e bancas.

### 3. Guias Práticos de Estudo e Metodologia (`guias/`)
* **`01_Guia_Uso_IA_Sem_Alucinar_no_Direito.md`:** Explica de forma intuitiva como os LLMs funcionam, por que inventam jurisprudência e como aplicar a fórmula dos 4 pilares no prompt + ambiente fechado (NotebookLM/RAG).
* **`02_Mapa_Estrategico_5o_Semestre_e_OAB.md`:** Trilha estratégica para quem está saindo do 4º semestre e entrando no 5º (3º ano), integrando matérias processuais, estágio, pré-OAB e ideias de TCC.

### 4. Arquitetura de Segundo Cérebro
* **`00-ENTRADA.md`, `01-REGRAS.md`, `02-PROTOCOLO.md`:** Base de memória persistente para o agente nunca perder o contexto das suas provas e trabalhos.
* **`10-disciplinas/`**, **`20-estagio-npj/`**, **`30-tcc-e-pesquisa/`**, **`40-oab-e-carreira/`**, **`60-estado/onde-estamos.md`**.
* **`.gitignore` blindado:** Impede o envio acidental de arquivos `.pdf`, `.docx`, imagens ou documentos de clientes/estágio para o GitHub.

---

## Como Instalar e Começar (Passo a Passo)

### Passo 1: Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/direito-os-kit-academico.git
cd direito-os-kit-academico
```

### Passo 2: Instalar as dependências Python (opcional, para gerar Word e Slides)
```bash
pip install python-docx python-pptx
```

### Passo 3: Rodar a Entrevista de Onboarding
Você tem **duas formas** de configurar o sistema:
* **Pelo terminal (Automático):**
  ```bash
  python iniciar.py
  ```
  O script exibe o panorama geral do kit, faz 6 perguntas rápidas (nome, faculdade, semestre, matérias, estágio e área de interesse), cria automaticamente suas pastas em `10-disciplinas/` e configura seu painel em `60-estado/onde-estamos.md`.
* **Pelo próprio Agente de IA:**
  Basta abrir a pasta no seu agente (Antigravity, Claude Code, Cursor ou Gemini CLI) e mandar um *"Oi, acabei de clonar o kit, vamos começar"*. Como `60-estado/onde-estamos.md` começa com `status: NAO_CONFIGURADO`, o próprio agente conduzirá a entrevista e configurará tudo para você.
