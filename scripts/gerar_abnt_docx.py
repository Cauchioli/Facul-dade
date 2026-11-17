"""
Gerador de Trabalhos Academicos em Word (.docx) no Padrao Estrito ABNT
(NBR 14724:2011, NBR 10520:2023 e NBR 6023:2018)

Uso:
    python scripts/gerar_abnt_docx.py

Requer:
    pip install python-docx
"""

import docx
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def _add_page_number(run):
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = 'PAGE'
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    r = run._r
    r.append(fldChar1)
    r.append(instrText)
    r.append(fldChar2)
    r.append(fldChar3)


def criar_documento_abnt(
    arquivo_saida: str,
    instituicao: str,
    curso: str,
    disciplina: str,
    professor: str,
    autor: str,
    ra: str,
    semestre: str,
    titulo: str,
    cidade: str,
    ano: str,
    secoes: list,
    referencias: list,
):
    """
    Gera um arquivo .docx com margens 3-3-2-2 cm, Arial 12, entrelinha 1,5,
    recuo 1,25 cm, paginacao superior direita a partir da pagina 2 e referencias ABNT.
    """
    doc = Document()

    for sec in doc.sections:
        sec.page_width = Cm(21.0)
        sec.page_height = Cm(29.7)
        sec.top_margin = Cm(3.0)
        sec.left_margin = Cm(3.0)
        sec.bottom_margin = Cm(2.0)
        sec.right_margin = Cm(2.0)
        sec.header_distance = Cm(2.0)
        sec.different_first_page_header_footer = True

        header = sec.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run()
        hrun.font.name = 'Arial'
        hrun.font.size = Pt(10)
        _add_page_number(hrun)

    # CAPA
    def _capa_p(texto, size=12, bold=True, space_after=12):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(space_after)
        r = p.add_run(texto)
        r.font.name = 'Arial'
        r.font.size = Pt(size)
        r.font.bold = bold
        return p

    _capa_p(f'{instituicao.upper()}\n{curso.upper()}\n{disciplina.upper()}\nDOCENTE: {professor.upper()}', size=12, space_after=60)
    _capa_p(f'{autor.upper()}\nR.A.: {ra} | {semestre}', size=12, space_after=90)
    _capa_p(titulo.upper(), size=14, space_after=140)
    _capa_p(f'{cidade.upper()}\n{ano}', size=12, space_after=0)

    doc.add_page_break()

    # SECOES TEXTUAIS
    for titulo_sec, paragrafos in secoes:
        p_h = doc.add_paragraph()
        p_h.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_h.paragraph_format.line_spacing = 1.5
        p_h.paragraph_format.space_before = Pt(18)
        p_h.paragraph_format.space_after = Pt(12)
        p_h.paragraph_format.first_line_indent = Cm(0)
        rh = p_h.add_run(titulo_sec.upper())
        rh.font.name = 'Arial'
        rh.font.size = Pt(12)
        rh.font.bold = True

        for texto in paragrafos:
            p_b = doc.add_paragraph()
            p_b.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p_b.paragraph_format.line_spacing = 1.5
            p_b.paragraph_format.space_before = Pt(0)
            p_b.paragraph_format.space_after = Pt(0)
            p_b.paragraph_format.first_line_indent = Cm(1.25)
            rb = p_b.add_run(texto)
            rb.font.name = 'Arial'
            rb.font.size = Pt(12)

    # REFERENCIAS (pagina propria, titulo centralizado, texto alinhado a esquerda)
    doc.add_page_break()
    p_ref_h = doc.add_paragraph()
    p_ref_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ref_h.paragraph_format.line_spacing = 1.5
    p_ref_h.paragraph_format.space_after = Pt(18)
    r_rh = p_ref_h.add_run('REFERÊNCIAS')
    r_rh.font.name = 'Arial'
    r_rh.font.size = Pt(12)
    r_rh.font.bold = True

    for ref in sorted(referencias):
        p_r = doc.add_paragraph()
        p_r.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_r.paragraph_format.line_spacing = 1.0
        p_r.paragraph_format.space_before = Pt(0)
        p_r.paragraph_format.space_after = Pt(12)
        p_r.paragraph_format.first_line_indent = Cm(0)
        rr = p_r.add_run(ref)
        rr.font.name = 'Arial'
        rr.font.size = Pt(12)

    doc.save(arquivo_saida)
    print(f'Documento ABNT gerado com sucesso em: {arquivo_saida}')


if __name__ == '__main__':
    # Exemplo de uso rapido
    criar_documento_abnt(
        arquivo_saida='Exemplo_Trabalho_ABNT.docx',
        instituicao='[NOME DA SUA FACULDADE]',
        curso='Curso de Graduação em Direito',
        disciplina='Direito Processual Civil',
        professor='Prof. [Nome do Docente]',
        autor='[Seu Nome Completo]',
        ra='[Seu RA]',
        semestre='5º Semestre',
        titulo='Modelo de Trabalho Acadêmico em Conformidade com as Normas da ABNT',
        cidade='[Sua Cidade - UF]',
        ano='2026',
        secoes=[
            ('1 INTRODUÇÃO', ['Este é um parágrafo de exemplo já formatado com recuo de 1,25 cm, fonte Arial 12, espaçamento 1,5 e margens oficiais de 3 cm (superior e esquerda) e 2 cm (inferior e direita).']),
            ('2 CONCLUSÃO', ['Substitua os campos de texto pelas suas seções e referências reais antes de entregar.'])
        ],
        referencias=[
            'BRASIL. Lei nº 13.105, de 16 de março de 2015. Código de Processo Civil. Brasília, DF, 2015.'
        ]
    )
