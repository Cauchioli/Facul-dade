---
name: abnt-trabalhos-academicos
description: >
  Formata e revisa trabalhos acadêmicos brasileiros (TCC, monografia, artigo) conforme as normas da ABNT:
  NBR 14724:2011 (apresentação), NBR 6023:2018 (referências), NBR 10520:2023 (citações),
  NBR 6024:2012 (numeração progressiva), NBR 6027:2012 (sumário), NBR 6028:2021 (resumo),
  NBR 6022:2018 (artigo) e IBGE (tabelas). Use quando o usuário pedir "formata na ABNT", "revisa as normas",
  "arruma as referências", "confere as citações", "deixa o TCC nas normas", ou ao gerar/editar qualquer .docx acadêmico.
---

# ABNT para trabalhos acadêmicos (pt-BR)

## 0. Regras de conduta (valem antes de qualquer formatação)

1. **Nunca invente conteúdo para "cumprir a norma".** Formatar é mexer na forma. Se faltar um dado de referência
   (editora, página, data de acesso, número do processo, data do julgamento), deixe marcado como `[CONFERIR: ...]`
   e informe o usuário. Nunca preencha com um valor plausível.
2. **Nunca invente resultados de pesquisa, testes, entrevistas ou estatísticas.** Se a metodologia promete algo
   que o texto não entrega, aponte a divergência e pergunte se o procedimento foi realmente feito.
3. **Não apague referências existentes.** Toda obra citada no texto precisa estar nas referências e vice-versa.
   Ao reorganizar a lista, faça a fusão (antigas + novas), nunca substitua.
4. **O manual da instituição prevalece** sobre a ABNT quando houver conflito (fonte, modelo de capa, artigo x monografia,
   caixa das citações). Peça o manual/template da faculdade se ele existir.
5. Trabalhe sempre em **cópia nova** do arquivo (`... - V7.docx`) e preserve o original.
6. As normas ABNT são pagas; este guia resume as regras a partir do conhecimento geral sobre elas. Em caso de dúvida
   pontual, diga que é uma dúvida e indique que o usuário confirme na biblioteca da instituição.

## 1. Estrutura do trabalho (NBR 14724:2011)

| Parte | Elementos (ordem) | Obrigatório? |
|---|---|---|
| Externa | Capa; lombada | Capa sim; lombada opcional |
| Pré-textual | Folha de rosto (verso: ficha catalográfica); errata; folha de aprovação; dedicatória; agradecimentos; epígrafe; resumo em português; resumo em língua estrangeira; listas (ilustrações, tabelas, abreviaturas, símbolos); sumário | Folha de rosto, aprovação, resumo, abstract e sumário sim; o resto opcional |
| Textual | Introdução; desenvolvimento; conclusão | Sim |
| Pós-textual | Referências; glossário; apêndices; anexos; índice | Só referências é obrigatória |

**Artigo científico (NBR 6022:2018):** título, autor(es) com nota de rodapé de afiliação, resumo + palavras-chave,
abstract + keywords, texto (introdução, desenvolvimento, considerações finais), referências. Muitos cursos de Direito
pedem "TCC em formato de artigo" com capa e folha de rosto antes: confirme qual modelo a instituição usa.

## 2. Formatação geral (NBR 14724:2011)

| Item | Regra |
|---|---|
| Papel | A4 (21 x 29,7 cm), branco |
| Margens | Superior e esquerda **3 cm**; inferior e direita **2 cm** (anverso) |
| Fonte | Tamanho **12** no texto. Tamanho **menor e uniforme (geralmente 10)** em: citações longas, notas de rodapé, paginação, ficha catalográfica, legendas e fontes de ilustrações e tabelas. A ABNT não fixa a família da fonte (Arial ou Times é decisão da instituição) |
| Entrelinha | **1,5** no texto. **Simples** em: citações longas, notas de rodapé, referências, legendas, ficha catalográfica, natureza do trabalho (folha de rosto/aprovação) |
| Parágrafo | Recuo de primeira linha (uso corrente **1,25 cm**; a NBR não fixa o valor, mas exija **um só valor** no trabalho inteiro). Texto justificado |
| Referências | Alinhadas à **esquerda** (sem justificar), entrelinha simples, separadas entre si por **uma linha em branco simples** |
| Natureza do trabalho | Na folha de rosto, recuada a partir do meio da mancha (≈ 8 cm), justificada, entrelinha simples |
| Paginação | Folhas contadas desde a folha de rosto, número **aparece a partir da Introdução**, algarismos arábicos, **canto superior direito**, a 2 cm da borda superior. Capa não é contada |
| Títulos de seção primária | Iniciam em **folha nova**, separados do texto que os sucede por **um espaço de 1,5** |
| Títulos sem indicativo numérico | Errata, agradecimentos, listas, resumo, abstract, sumário, referências, glossário, apêndice, anexo, índice: **centralizados** e sem número |
| Elementos sem título e sem número | Folha de aprovação, dedicatória, epígrafe |

## 3. Numeração progressiva das seções (NBR 6024:2012)

- Indicativo numérico em algarismo arábico, **alinhado à esquerda**, separado do título por **um espaço**.
- **Nada** entre o número e o título: sem ponto, hífen, travessão ou dois-pontos.
- Destaque gradativo e coerente com o sumário (ex.: primária MAIÚSCULA NEGRITO; secundária MAIÚSCULA normal;
  terciária Minúscula negrito...).
- Não use palavras como "Capítulo" no indicativo.
- Alíneas: letras minúsculas seguidas de parêntese `a)`, texto começa em minúscula e termina em ponto e vírgula; a última termina em ponto. Subalíneas com travessão.

```text
ERRADO                                         CERTO
CAPÍTULO 1: INTELIGÊNCIA ARTIFICIAL...         4 INTELIGÊNCIA ARTIFICIAL NO COTIDIANO JURÍDICO
1. Pesquisa Jurídica e Análise:                4.1 PESQUISA JURÍDICA E ANÁLISE DE DOCUMENTOS
Capítulo 2: Desafios Éticos...                 5 DESAFIOS ÉTICOS E LIMITES TÉCNICOS DA IA NO DIREITO
Considerações Finais                           8 CONSIDERAÇÕES FINAIS
```

Itens de lista (ex.: "Resumo: condensar documentos") **não são títulos**: não podem estar em estilo de título
nem aparecer no sumário.

## 4. Sumário (NBR 6027:2012)

- Último elemento pré-textual, título "SUMÁRIO" centralizado.
- Lista as seções **na mesma grafia e destaque** usados no texto, com o indicativo numérico alinhado à esquerda e a página.
- Elementos pré-textuais (resumo, abstract, listas) **não entram** no sumário.
- Gere pelo campo automático do Word (estilos de Título 1/2/3) para que números de página batam.

## 5. Resumo e palavras-chave (NBR 6028:2021)

- **Parágrafo único**, frases afirmativas, voz ativa, terceira pessoa.
- Extensão em trabalhos acadêmicos: **150 a 500 palavras**; em artigos: **100 a 250 palavras**.
- Deve conter objetivo, método, resultados e conclusões.
- Logo abaixo: `Palavras-chave:` seguidas dos termos **separados por ponto e vírgula e finalizados por ponto**,
  com inicial **minúscula** (exceto nomes próprios e científicos).

```text
Palavras-chave: inteligência artificial; direito processual; ética profissional; engenharia de prompt.
Keywords: artificial intelligence; procedural law; professional ethics; prompt engineering.
```

## 6. Citações (NBR 10520:2023)

| Tipo | Regra |
|---|---|
| Direta curta (até 3 linhas) | No corpo do texto, entre **aspas duplas**; aspas simples para citação dentro de citação. Página obrigatória |
| Direta longa (mais de 3 linhas) | Parágrafo próprio, **recuo de 4 cm** da margem esquerda, fonte menor (10), entrelinha simples, **sem aspas**. Página obrigatória |
| Indireta (paráfrase) | Sem aspas; página opcional |
| Citação de citação | `apud` (Sobrenome, ano, p. x apud Sobrenome, ano, p. y). Use só quando o original for inacessível |
| Supressão / acréscimo / destaque | `[...]` para supressão; `[ ]` para acréscimo; destaque com "grifo nosso" ou "grifo do autor" |
| Mesmo autor e ano | Acrescente letras: (Silva, 2024a), (Silva, 2024b) |
| Vários autores na mesma chamada | Separados por ponto e vírgula, em ordem alfabética |

**Caixa da autoria:** a versão 2023 da NBR 10520 passou a usar **maiúsculas e minúsculas** na indicação de autoria,
inclusive entre parênteses: `(Floridi, 2013, p. 45)`. Na versão anterior (2002) era maiúscula dentro dos parênteses:
`(FLORIDI, 2013, p. 45)`. **Muitas instituições ainda aceitam ou exigem o formato antigo: confirme com o orientador e
use um padrão só no trabalho inteiro.**

```text
Narrativa: Segundo Susskind (2017, p. 12), "a profissão jurídica ..."
Parentética: A IA não substitui o juízo humano (Russell, 2019).
Entidade:   ... (Ordem dos Advogados do Brasil, 2024) ou sigla definida antes: (OAB SP, 2024)
Legislação no texto: cite o diploma por extenso na primeira menção — Lei nº 13.709/2018 (LGPD), art. 6º —
                     e inclua a lei nas referências.
```

## 7. Referências (NBR 6023:2018)

Regras gerais:
- Ordem **alfabética** pela entrada (sobrenome ou entidade), alinhadas à esquerda, entrelinha simples, uma linha em branco entre elas.
- **Destaque** (negrito ou itálico, escolha um) no título principal; uniforme em todas.
- Sobrenome em MAIÚSCULAS, prenomes como na obra.
- Até 3 autores: todos, separados por ponto e vírgula. 4 ou mais: pode-se indicar todos ou o primeiro seguido de `et al.`
- Online: `Disponível em: URL. Acesso em: 14 out. 2026.` — **sem os sinais < >** (abolidos em 2018).
- Meses abreviados: jan. fev. mar. abr. maio jun. jul. ago. set. out. nov. dez.
- Sem data: `[2024?]`, `[ca. 2024]`. Sem local: `[S. l.]`. Sem editora: `[s. n.]`.
- Obra traduzida: indique o título em português **e** a editora/local da edição traduzida que você leu. Não misture título em português com editora e ano da edição original.

Modelos (destaque em **negrito** representado por `**`):

```text
LIVRO
SUSSKIND, Richard. **Tomorrow's lawyers**: an introduction to your future. 2. ed. Oxford: Oxford University Press, 2017.

CAPÍTULO DE LIVRO
SOBRENOME, Nome. Título do capítulo. In: SOBRENOME, Nome (org.). **Título do livro**. Local: Editora, ano. p. 10-25.

ARTIGO DE PERIÓDICO
YEUNG, Karen. Algorithmic regulation: a critical interrogation. **Regulation & Governance**, [s. l.], v. 12, n. 4, p. 505-523, 2018.

NOTÍCIA ONLINE
MIGALHAS. Juiz multa advogadas que esconderam prompt para enganar IA da Justiça. **Migalhas**, [s. l.], 13 maio 2026. Disponível em: https://www.migalhas.com.br/quentes/455817/... Acesso em: 14 out. 2026.

LEGISLAÇÃO
BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). **Diário Oficial da União**: seção 1, Brasília, DF, p. 59, 15 ago. 2018.
BRASIL. [Constituição (1988)]. **Constituição da República Federativa do Brasil de 1988**. Brasília, DF: Presidência da República, [2026]. Disponível em: http://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm. Acesso em: 14 out. 2026.

ATO NORMATIVO
CONSELHO NACIONAL DE JUSTIÇA (Brasil). Resolução nº 615, de 11 de março de 2025. [Ementa conforme publicada]. Brasília, DF: CNJ, 2025. Disponível em: URL. Acesso em: dd mmm. aaaa.

PROJETO DE LEI
BRASIL. Senado Federal. **Projeto de Lei nº 2.338, de 2023**. Dispõe sobre o uso da inteligência artificial. Brasília, DF: Senado Federal, 2023. Disponível em: URL. Acesso em: dd mmm. aaaa.

JURISPRUDÊNCIA
BRASIL. Tribunal Regional do Trabalho (8. Região). 3ª Vara do Trabalho de Parauapebas. **Ação Trabalhista nº 0001062-55.2025.5.08.0130**. Juiz: Luiz Carlos de Araujo Santos Junior. [Data da sentença: CONFERIR]. Disponível em: URL. Acesso em: dd mmm. aaaa.
ESTADOS UNIDOS. United States District Court for the Southern District of New York. **Mata v. Avianca, Inc.**, No. 22-cv-1461 (PKC). Opinion and order on sanctions, 22 jun. 2023.

DOCUMENTO DE ENTIDADE / RELATÓRIO
OAB SP; TRYBE; JUSBRASIL; ITS RIO. **1º Relatório Impacto da IA Generativa no Direito**: panorama sobre adoção e percepções. São Paulo: OAB SP, 2024. Disponível em: URL. Acesso em: dd mmm. aaaa.

PREPRINT (arXiv)
KORBAK, Tomek et al. **Chain of thought monitorability**: a new and fragile opportunity for AI safety. arXiv, 2025. Disponível em: https://arxiv.org/abs/2507.11473. Acesso em: dd mmm. aaaa.
```

## 8. Ilustrações e tabelas (NBR 14724:2011 + IBGE)

- Identificação **acima**: `Figura 1 – Título`, `Quadro 1 – Título`, `Gráfico 1 – Título`, `Tabela 1 – Título`.
- **Fonte abaixo, obrigatória** (mesmo que seja o próprio autor: `Fonte: elaborado pelo autor (2026).`), fonte 10.
- Inseridas o mais próximo possível do trecho que as menciona e citadas no texto.
- Tabela (IBGE): sem bordas laterais; quadro: bordas fechadas, conteúdo textual.

## 9. Notas de rodapé

- Fonte 10, entrelinha simples, separadas do texto por filete de 5 cm a partir da margem esquerda (padrão do Word).
- Use para explicar termos sem inflar o corpo do texto (ex.: definição de *prompt injection*).

## 10. Implementação no .docx (python-docx) — roteiro para o agente

1. **Auditar antes de mudar:** margens por seção, estilo Normal (fonte, tamanho, entrelinha, recuo), distribuição de
   recuos/entrelinhas reais por parágrafo, estilos de título usados, chamadas autor-data no texto x lista de referências,
   presença de campo PAGE no cabeçalho. Relate o diagnóstico ao usuário.
2. **Configurar no estilo, não parágrafo a parágrafo:** `Normal` com fonte 12, entrelinha 1,5, recuo 1,25 cm, justificado.
   Crie estilos próprios: `Citacao Longa` (recuo esquerdo 4 cm, 10 pt, simples, sem recuo de 1ª linha),
   `Referencia` (esquerda, simples, espaço depois de 12 pt, sem recuo), `Legenda`.
3. Ao reescrever texto de um parágrafo, **preserve os runs** quando houver itálico/negrito (ex.: termos estrangeiros
   como *prompt*). Substituir `p.text` apaga a formatação dos runs: avise ou reaplique.
4. Títulos: aplique `Heading 1/2/3` só a títulos reais, com indicativo numérico conforme a NBR 6024; remova o estilo de
   título de itens de lista. Depois, peça ao usuário para **atualizar o sumário no Word** (F9), pois o python-docx não recalcula páginas.
5. Paginação: inserir campo `PAGE` no cabeçalho alinhado à direita, em seção que começa na Introdução
   (quebra de seção antes da Introdução, cabeçalho desvinculado da seção anterior).
6. Referências: monte a lista final pela **fusão** das existentes com as novas, ordene por entrada, aplique o estilo
   `Referencia` e o destaque no título. Liste ao usuário cada item com `[CONFERIR]`.
7. Valide: toda chamada `(Autor, ano)` tem referência; toda referência é citada; nenhuma URL com `< >`;
   um único padrão de caixa nas citações; nenhum título com "Capítulo", ponto ou dois-pontos após o número.

## 11. Checklist final de entrega

- [ ] Margens 3/3/2/2 em todas as seções
- [ ] Fonte 12 no texto; 10 em citações longas, notas, legendas, fontes e paginação
- [ ] Entrelinha 1,5 no texto; simples nos casos da tabela da seção 2
- [ ] Um único recuo de parágrafo em todo o texto
- [ ] Títulos numerados conforme NBR 6024, sem "Capítulo", sem pontuação após o número
- [ ] Seções primárias em folha nova; sumário atualizado e idêntico aos títulos
- [ ] Paginação a partir da Introdução, canto superior direito
- [ ] Resumo em parágrafo único, dentro do limite de palavras; palavras-chave no formato da NBR 6028
- [ ] Citações diretas com página; longas com recuo de 4 cm; padrão de caixa único
- [ ] Referências em ordem alfabética, alinhadas à esquerda, destaque uniforme, sem `< >`, todas citadas no texto
- [ ] Toda figura/tabela com título acima e fonte abaixo
- [ ] Nenhum dado, resultado ou referência inventado; pendências marcadas com `[CONFERIR]` e informadas
