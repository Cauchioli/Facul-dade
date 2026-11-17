"""
Instalador e Entrevista Inicial do Direito OS - Kit Academico

Ao rodar `python iniciar.py`, este script:
1. Exibe o panorama completo do que existe neste repositorio;
2. Faz uma entrevista rapida para personalizar o ambiente ao seu semestre e faculdade;
3. Cria suas pastas de materias em `10-disciplinas/` e ativa `60-estado/onde-estamos.md`.
"""

import os
import re
from datetime import date


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[áàâã]', 'a', text)
    text = re.sub(r'[éèê]', 'e', text)
    text = re.sub(r'[íìî]', 'i', text)
    text = re.sub(r'[óòôõ]', 'o', text)
    text = re.sub(r'[úùû]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    print('=' * 70)
    print('  BEM-VINDO AO DIREITO OS : KIT ACADEMICO E AGENTE DE DIREITO')
    print('=' * 70)
    print('\nPANORAMA GERAL DO QUE VOCE ACABOU DE INSTALAR:\n')
    print('  1. Habilidades do Agente (.gemini/skills/):')
    print('     - abnt-trabalhos-academicos : Regras ABNT NBR 14724, 6023, 10520')
    print('     - tcc-e-banca-nota-10       : Pesquisa sem alucinacoes, slides e defesa')
    print('     - estudo-e-revisao-direito  : Lei seca, sumulas, metodo FGV/OAB')
    print('     - npj-e-pecas-praticas      : Estagio, pecas e sigilo LGPD/OAB\n')
    print('  2. Geradores Automaticos (scripts/):')
    print('     - gerar_abnt_docx.py        : Gera Word (.docx) 100% nas normas ABNT')
    print('     - gerar_slides_clean.py     : Gera apresentacoes 16:9 limpas\n')
    print('  3. Guias Praticos e Templates UniFSP (guias/ e templates/):')
    print('     - Guia de Uso de IA Sem Alucinar no Direito (Triplice Barreira)')
    print('     - Mapa Estrategico do 5o Semestre ate a OAB e o TCC')
    print('     - Guia Completo de Funcionamento da UniFSP (400h Extensao, NPJ, TCC)')
    print('     - CAPA_OFICIAL_UNIFSP_MODELO.docx com o brasao oficial pronto\n')
    print('  4. Organizacao do Segundo Cerebro:')
    print('     - 10-disciplinas/   | 20-estagio-npj/ | 30-tcc-e-pesquisa/')
    print('     - 40-oab-e-carreira/ | 60-estado/onde-estamos.md\n')
    print('-' * 70)
    print('ENTREVISTA RAPIDA DE CONFIGURACAO (leva 1 minuto):')
    print('-' * 70)

    nome = input('1. Seu nome completo (ou como quer ser chamado): ').strip() or 'Estudante de Direito'
    faculdade = input('2. Nome da sua faculdade / universidade: ').strip() or 'Faculdade de Direito'
    semestre = input('3. Semestre que esta cursando ou entrando (ex: 5o Semestre): ').strip() or '5o Semestre'
    disciplinas_raw = input('4. Liste suas materias atuais separadas por virgula (ex: Processo Civil, Penal, Trabalho): ').strip()
    estagio = input('5. Ja faz estagio ou NPJ? Onde / qual area? (ex: Nao / Escritorio Civel): ').strip() or 'Ainda nao iniciado'
    interesse = input('6. Qual area do Direito mais te atrai hoje para TCC/OAB? ').strip() or 'A definir'

    disciplinas = [d.strip() for d in disciplinas_raw.split(',') if d.strip()] if disciplinas_raw else [
        'Direito Processual Civil',
        'Direito Processual Penal',
        'Direito do Trabalho',
        'Direito Empresarial'
    ]

    # Criar pastas das disciplinas em 10-disciplinas/
    disc_dir = os.path.join(base_dir, '10-disciplinas')
    os.makedirs(disc_dir, exist_ok=True)
    for d in disciplinas:
        folder = os.path.join(disc_dir, slugify(d))
        os.makedirs(folder, exist_ok=True)
        notes_file = os.path.join(folder, 'resumo-e-anotacoes.md')
        if not os.path.exists(notes_file):
            with open(notes_file, 'w', encoding='utf-8') as f:
                f.write(f'# {d}\n\n- **Semestre:** {semestre}\n\n## Ementa e Datas de Prova\n- [ ] Inserir cronograma do professor\n\n## Resumos e Lei Seca\n')

    # Atualizar 60-estado/onde-estamos.md
    hoje = date.today().isoformat()
    estado_path = os.path.join(base_dir, '60-estado', 'onde-estamos.md')
    disc_md = '\n'.join([f'* [ ] **{d}** (`10-disciplinas/{slugify(d)}/`)' for d in disciplinas])
    estado_content = f"""---
tipo: estado
status: ATIVO
atualizado: {hoje}
---

# Painel Executivo da Faculdade: Onde Estamos

## Dados do Estudante
* **Nome:** {nome}
* **Instituição:** {faculdade}
* **Semestre Atual:** {semestre}
* **Estágio / NPJ:** {estagio}
* **Área de Interesse Principal:** {interesse}

## Disciplinas do Semestre Atual
{disc_md}

## Entregas e Provas Próximas
* [ ] Registrar datas das provas bimestrais e trabalhos aqui

## Trilha de Longo Prazo (3º ao 5º Ano)
* [ ] Consolidar base de Processo Civil, Processo Penal e Trabalho
* [ ] Iniciar caderno de erros OAB em `40-oab-e-carreira/caderno-de-erros.md`
* [ ] Anotar ideias de temas de TCC em `30-tcc-e-pesquisa/ideias-de-tema.md`
"""
    with open(estado_path, 'w', encoding='utf-8') as f:
        f.write(estado_content)

    # Criar arquivos iniciais em 30-tcc e 40-oab
    tcc_ideas = os.path.join(base_dir, '30-tcc-e-pesquisa', 'ideias-de-tema.md')
    if not os.path.exists(tcc_ideas):
        with open(tcc_ideas, 'w', encoding='utf-8') as f:
            f.write(f'# Banco de Ideias para TCC e Iniciação Científica\n\n* **Área de Interesse Inicial:** {interesse}\n\n## Temas e Problemas Observados em Aula\n- [ ] Exemplo: [Tema] -> [Qual a lacuna da lei ou conflito jurisprudencial?]\n')

    oab_erros = os.path.join(base_dir, '40-oab-e-carreira', 'caderno-de-erros.md')
    if not os.path.exists(oab_erros):
        with open(oab_erros, 'w', encoding='utf-8') as f:
            f.write('# Caderno de Erros FGV / OAB\n\n| Disciplina | Assunto | Por que errei | Regra exata da lei ou súmula |\n|---|---|---|---|\n')

    print('\n' + '=' * 70)
    print('CONFIGURACAO CONCLUIDA COM SUCESSO!')
    print('=' * 70)
    print(f'- Pastas criadas em 10-disciplinas/ para {len(disciplinas)} materias.')
    print('- Painel atualizado em 60-estado/onde-estamos.md.')
    print('- Agora voce ja pode abrir esta pasta no seu Agente de IA (Antigravity,')
    print('  Claude Code, Cursor ou Gemini CLI) e comecar a estudar e produzir.')
    print('=' * 70)


if __name__ == '__main__':
    main()
