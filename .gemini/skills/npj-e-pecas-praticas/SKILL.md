---
name: npj-e-pecas-praticas
description: >
  Fluxo de trabalho para Núcleo de Prática Jurídica (NPJ), estágios em escritórios ou órgãos públicos:
  organização de dossiês de atendimento, redação de peças processuais estruturadas, relatórios de estágio
  e proteção estrita de dados pessoais conforme LGPD e Estatuto da OAB.
---

# NPJ, Estágio e Peças Práticas

## 1. Regra de Ouro de Privacidade (LGPD + Art. 7º, XIX, EAOAB)
- **Antes de analisar qualquer caso real**, substitua nomes, CPFs, RGs, endereços, números de processo em segredo de justiça e prontuários médicos por marcadores genéricos (`[CLIENTE]`, `[PARTE CONTRÁRIA]`, `[ENDEREÇO]`).
- Nunca faça upload de documentos reais com CPF/RG no GitHub ou em chats sem anonimização prévia.

## 2. Organização de Pastas de Casos Práticos
Para cada atendimento no NPJ ou caso de estágio, organize localmente (fora do Git, protegido pelo `.gitignore`) na pasta `20-estagio-npj/`:
- `AAAA-MM-DD_TipoAcao_IniciaisCliente/`
  - `00_FICHA_DO_CASO.md` (resumo dos fatos, documentos faltantes, prazo e teses jurídicas);
  - Documentos numerados cronologicamente (`01_Procuracao`, `02_Declaracao_Hipossuficiencia`, `03_Documentos_Pessoais`, `04_Provas`).

## 3. Estrutura Padrão de Peça Processual
Ao auxiliar na elaboração de esboços de peças (Iniciais, Contestações, Recursos):
1. Endereçamento correto (competência material e territorial);
2. Qualificação completa das partes (usando placeholders se anonimizado);
3. Síntese fática cronológica e objetiva;
4. Fundamentação jurídica escalonada (Constituição Federal -> Lei Federal / Código -> Jurisprudência verificada);
5. Tutela de urgência (se houver *fumus boni iuris* e *periculum in mora* com base nos fatos);
6. Pedidos claros e especificados + valor da causa + requerimento de provas e gratuidade da justiça (art. 98 do CPC, quando cabível).
