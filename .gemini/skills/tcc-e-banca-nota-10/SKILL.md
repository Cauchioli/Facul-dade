---
name: tcc-e-banca-nota-10
description: >
  Metodologia completa para pesquisa jurídica, elaboração de TCC, blindagem contra alucinações de IA,
  criação de apresentações visuais limpas (16:9) e preparação para defesa oral perante banca examinadora.
  Ative quando o estudante for iniciar projeto de pesquisa, artigo, monografia ou slides de defesa.
---

# TCC e Banca Nota 10 (Metodologia Jurídica Anti-Alucinação)

## 1. Protocolo da Tríplice Barreira na Pesquisa Jurídica
Ao usar IA para auxiliar em qualquer pesquisa acadêmica, aplique obrigatoriamente:
1. **Barreira 1 (Ingestão e Sigilo):** Nunca envie dados pessoais reais de processos em segredo de justiça ou clientes para modelos abertos. Anonimize sempre.
2. **Barreira 2 (Comando Parametrizado e RAG):**
   - Sempre use os **4 pilares no prompt**: Papel definido + Contexto restrito + Base de dados fechada (ex: PDFs no NotebookLM) + Regra negativa explícita (*"Se não encontrar na base oficial, informe que não encontrou e NÃO invente"*).
   - Nunca peça jurisprudência genérica em prompt aberto (modelos de linguagem operam por predição estatística de *tokens* e inventam acórdãos verossímeis com números aleatórios).
3. **Barreira 3 (Auditoria Humana na Fonte Primária):** Confira 100% dos artigos de lei no Planalto (`planalto.gov.br`), súmulas e números de REsp/RE diretamente nos portais do STF, STJ e tribunais estaduais/trabalhistas.

## 2. Estrutura de Apresentação de Defesa (Estilo Clean 16:9)
- **Menos texto, mais arquitetura visual:** Máximo de 10 a 15 slides objetivos para defesas de 10 a 12 minutos.
- **Narrativa em arco:**
  1. Capa oficial (Título, Autor, Orientador, Instituição);
  2. Problema de Pesquisa e Metodologia (objetivo geral, específicos e fontes);
  3. Dado Empírico de Impacto (gráfico ou estatística que prova por que o tema é urgente);
  4. Provocação ou Analogia Didática (um slide limpo com uma frase de gancho + o slide seguinte explicando o conceito de forma simples);
  5. Desenvolvimento Jurídico e Marco Normativo (linha do tempo em cartões verticais de *Causa -> Solução Legislativa*, sem texto cortado);
  6. Casos Reais / Jurisprudência (estudos de caso concretos);
  7. Contribuição Prática / Solução Proposta;
  8. Conclusão (resposta direta ao problema + frase de fechamento memorável) e Referências unificadas.
- **Uso do Gerador:** Utilize `scripts/gerar_slides_clean.py` para evitar caixas de texto desalinhadas ou cortes de palavras.

## 3. Escrita Humana (Zero "Cara de IA")
- Evite clichês de IA (*"Em um mundo cada vez mais globalizado"*, *"Diante do exposto, mister se faz"*, listas mecânicas excessivas).
- Prefira parágrafos corridos, encadeamento lógico claro (premissa normativa -> caso concreto -> conclusão crítica) e voz autoral firme.
