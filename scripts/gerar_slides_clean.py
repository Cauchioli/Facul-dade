"""
Gerador de Apresentacoes Academicas Limpas (16:9) para Seminarios e Bancas de TCC

Padrao visual minimalista: fundo branco, azul marinho (#1F3864) e laranja terra (#C55A11),
sem sobrecarga de texto e sem cortes de palavras.

Requer:
    pip install python-pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


NAVY = RGBColor(0x1F, 0x38, 0x64)
ORANGE = RGBColor(0xC5, 0x5A, 0x11)
DARK_TEXT = RGBColor(0x26, 0x26, 0x26)
MUTED = RGBColor(0x59, 0x59, 0x59)


def nova_apresentacao():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs


def adicionar_capa(prs, titulo, subtitulo, autor, instituicao):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    tb = slide.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(3.5))
    tf = tb.text_frame
    tf.word_wrap = True

    p1 = tf.paragraphs[0]
    p1.text = titulo
    p1.alignment = PP_ALIGN.CENTER
    p1.font.name = 'Calibri'
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = NAVY

    p2 = tf.add_paragraph()
    p2.text = subtitulo
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(14)
    p2.font.name = 'Calibri'
    p2.font.size = Pt(18)
    p2.font.color.rgb = ORANGE

    p3 = tf.add_paragraph()
    p3.text = f'{autor}\n{instituicao}'
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(36)
    p3.font.name = 'Calibri'
    p3.font.size = Pt(15)
    p3.font.color.rgb = MUTED


def adicionar_slide_frase_impacto(prs, frase, legenda=''):
    """Slide limpo estilo TED/Banca para pausar e provocar reflexao."""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    tb = slide.shapes.add_textbox(Inches(1.5), Inches(2.4), Inches(10.3), Inches(2.8))
    tf = tb.text_frame
    tf.word_wrap = True

    p1 = tf.paragraphs[0]
    p1.text = frase
    p1.alignment = PP_ALIGN.CENTER
    p1.font.name = 'Calibri'
    p1.font.size = Pt(42)
    p1.font.bold = True
    p1.font.color.rgb = NAVY

    if legenda:
        p2 = tf.add_paragraph()
        p2.text = legenda
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(18)
        p2.font.name = 'Calibri'
        p2.font.size = Pt(16)
        p2.font.italic = True
        p2.font.color.rgb = ORANGE


def adicionar_slide_duas_colunas(prs, titulo, sub_esq, itens_esq, sub_dir, itens_dir):
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Titulo superior
    tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.9))
    p_t = tb_t.text_frame.paragraphs[0]
    p_t.text = titulo.upper()
    p_t.font.name = 'Calibri'
    p_t.font.size = Pt(24)
    p_t.font.bold = True
    p_t.font.color.rgb = NAVY

    def _montar_coluna(left_in, subtitulo, itens):
        tb_s = slide.shapes.add_textbox(Inches(left_in), Inches(1.5), Inches(5.4), Inches(0.5))
        ps = tb_s.text_frame.paragraphs[0]
        ps.text = subtitulo.upper()
        ps.font.name = 'Calibri'
        ps.font.size = Pt(14)
        ps.font.bold = True
        ps.font.color.rgb = ORANGE

        tb_b = slide.shapes.add_textbox(Inches(left_in), Inches(2.1), Inches(5.4), Inches(4.8))
        tf = tb_b.text_frame
        tf.word_wrap = True
        for i, item in enumerate(itens):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = f'• {item}'
            p.space_after = Pt(10)
            p.font.name = 'Calibri'
            p.font.size = Pt(14)
            p.font.color.rgb = DARK_TEXT

    _montar_coluna(0.8, sub_esq, itens_esq)
    _montar_coluna(7.0, sub_dir, itens_dir)


if __name__ == '__main__':
    prs = nova_apresentacao()
    adicionar_capa(prs, 'Título do Seminário ou TCC', 'Subtítulo explicativo', 'Seu Nome Completo', 'Curso de Direito • 2026')
    adicionar_slide_frase_impacto(prs, '"Frase provocativa central..."', '(Use este slide para criar pausa e engajar a sala ou a banca)')
    adicionar_slide_duas_colunas(
        prs,
        'Análise Comparativa',
        'Aspectos Normativos',
        ['Artigo de lei aplicável', 'Princípio constitucional envolvido'],
        'Aplicação Prática',
        ['Caso concreto analisado', 'Conclusão do grupo']
    )
    prs.save('Exemplo_Apresentacao_Clean.pptx')
    print('Apresentacao gerada com sucesso!')
