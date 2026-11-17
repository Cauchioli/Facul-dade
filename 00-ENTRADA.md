# Entrada do Segundo Cérebro Acadêmico de Direito

Bem-vindo ao **Direito OS**, um ambiente agêntico projetado para transformar o seu assistente de IA em um parceiro de estudos, pesquisa jurídica, formatação ABNT e organização de carreira do 5º semestre até a aprovação na OAB e a defesa do TCC.

## Mapa do Workspace

| Pasta / Arquivo | O que guarda e para que serve |
|---|---|
| `01-REGRAS.md` | Regras de ouro de conduta, rigor jurídico (zero alucinações) e privacidade |
| `02-PROTOCOLO.md` | Protocolo de operação contínua, atualização de progresso e entrega |
| `.gemini/skills/` | Habilidades especializadas (ABNT, TCC Nota 10, Estudo Ativo, NPJ/Estágio) |
| `scripts/` | Geradores automáticos em Python para Word ABNT (`.docx`) e Slides (`.pptx`) |
| `guias/` | Manuais práticos de uso de IA sem alucinar e trilha estratégica do 5º semestre e OAB |
| `10-disciplinas/` | Materiais, resumos, trabalhos e revisões de provas organizados por matéria |
| `20-estagio-npj/` | Modelos de peças práticas, relatórios de estágio e acompanhamento de audiências (sempre anonimizados) |
| `30-tcc-e-pesquisa/` | Artigos, iniciação científica, fichamentos e projeto de TCC |
| `40-oab-e-carreira/` | Cronograma progressivo, caderno de erros, súmulas e preparação para a OAB |
| `60-estado/onde-estamos.md` | Painel vivo com suas matérias, entregas, provas e pendências atuais |

## Gatilho de Primeira Execução (Onboarding Automático)

Se `60-estado/onde-estamos.md` estiver com `status: NAO_CONFIGURADO`:
1. Apresente o **Panorama Geral do Kit** acima ao estudante de forma clara.
2. Execute a **Entrevista de Configuração** (ou oriente a rodar `python iniciar.py` no terminal) coletando:
   - Nome e apelido preferido;
   - Faculdade e cidade;
   - Semestre atual (ex: indo para o 5º semestre / 3º ano);
   - Lista de disciplinas do semestre;
   - Se já faz estágio ou Núcleo de Prática Jurídica (NPJ);
   - Se já tem interesse em alguma área específica do Direito (Civil, Penal, Trabalhista, Empresarial, Constitucional, etc.) para TCC e OAB.
3. Grave essas informações em `60-estado/onde-estamos.md` (`status: ATIVO`), ajuste `01-REGRAS.md` e crie as pastas das disciplinas em `10-disciplinas/`.
