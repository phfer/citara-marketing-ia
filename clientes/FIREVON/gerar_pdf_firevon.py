#!/usr/bin/env python3
"""
Gerador de PDF FIREVON - Documento Mestre Completo
Cria um PDF profissional e bem estruturado com as cores da marca
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether, Preformatted
)
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import os

# Cores FIREVON
FIREVON_ORANGE = HexColor('#FF6B35')
FIREVON_NAVY = HexColor('#1A1F36')
FIREVON_TEAL = HexColor('#00D4C7')
FIREVON_GRAY = HexColor('#718096')
FIREVON_LIGHT_GRAY = HexColor('#EDF2F7')
FIREVON_CHARCOAL = HexColor('#2D3748')

# Caminho do arquivo
PDF_PATH = "/Users/paulohenrique/Desktop/Citara Marketing IA - Lovable - Claude/FIREVON/FIREVON_DOCUMENTO_MESTRE.pdf"

def create_custom_styles():
    """Cria estilos personalizados para o documento"""
    styles = getSampleStyleSheet()

    # Estilos personalizados com nomes únicos
    styles.add(ParagraphStyle(
        name='TitleMain',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=28,
        textColor=FIREVON_NAVY,
        spaceAfter=0.5*cm,
        alignment=TA_CENTER,
    ))

    styles.add(ParagraphStyle(
        name='Subtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        textColor=FIREVON_GRAY,
        spaceAfter=1*cm,
        alignment=TA_CENTER,
    ))

    # Atualizar estilos existentes
    styles['Heading1'].fontName = 'Helvetica-Bold'
    styles['Heading1'].fontSize = 20
    styles['Heading1'].textColor = FIREVON_NAVY
    styles['Heading1'].spaceBefore = 0.8*cm
    styles['Heading1'].spaceAfter = 0.4*cm

    styles['Heading2'].fontName = 'Helvetica-Bold'
    styles['Heading2'].fontSize = 16
    styles['Heading2'].textColor = FIREVON_NAVY
    styles['Heading2'].spaceBefore = 0.6*cm
    styles['Heading2'].spaceAfter = 0.3*cm

    styles['Heading3'].fontName = 'Helvetica-Bold'
    styles['Heading3'].fontSize = 13
    styles['Heading3'].textColor = FIREVON_CHARCOAL
    styles['Heading3'].spaceBefore = 0.4*cm
    styles['Heading3'].spaceAfter = 0.2*cm

    # Estilos customizados
    styles.add(ParagraphStyle(
        name='FirevonBodyText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        textColor=FIREVON_CHARCOAL,
        spaceAfter=0.3*cm,
        alignment=TA_JUSTIFY,
        leading=14,
    ))

    styles.add(ParagraphStyle(
        name='FirevonBulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        textColor=FIREVON_CHARCOAL,
        spaceAfter=0.2*cm,
        leftIndent=0.5*cm,
        bulletIndent=0.3*cm,
    ))

    styles.add(ParagraphStyle(
        name='FirevonQuoteText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        textColor=FIREVON_NAVY,
        spaceAfter=0.4*cm,
        leftIndent=1*cm,
        rightIndent=1*cm,
        backColor=FIREVON_LIGHT_GRAY,
    ))

    styles.add(ParagraphStyle(
        name='FirevonSmallText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        textColor=FIREVON_GRAY,
        spaceAfter=0.2*cm,
    ))

    styles.add(ParagraphStyle(
        name='FirevonOrangeText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        textColor=FIREVON_ORANGE,
        spaceAfter=0.3*cm,
    ))

    return styles

def create_header_footer(canvas, doc):
    """Cria cabeçalho e footer para cada página"""
    # Cabeçalho
    canvas.saveState()
    canvas.setFillColor(FIREVON_NAVY)
    canvas.rect(0, A4[1]-40, A4[0], 40, fill=True, stroke=False)

    canvas.setFillColor(FIREVON_ORANGE)
    canvas.setFont('Helvetica-Bold', 14)
    canvas.drawString(2*cm, A4[1]-20, 'FIREVON')

    canvas.setFillColor(colors.white)
    canvas.setFont('Helvetica', 9)
    canvas.drawString(4.5*cm, A4[1]-20, 'Documento Mestre Completo')

    # Footer
    canvas.setFillColor(FIREVON_LIGHT_GRAY)
    canvas.rect(0, 0, A4[0], 20, fill=True, stroke=False)

    canvas.setFillColor(FIREVON_GRAY)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(2*cm, 7, f'Página {doc.page}')

    canvas.setFillColor(FIREVON_ORANGE)
    canvas.drawString(A4[0]-4*cm, 7, 'Previsibilidade em Execução')

    canvas.restoreState()

def build_document():
    """Constrói o documento PDF completo"""
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=4*cm,
        bottomMargin=2.5*cm,
    )

    styles = create_custom_styles()
    story = []

    # ==================== CAPA ====================
    story.append(Spacer(0, 2*cm))
    story.append(Paragraph("FIREVON", styles['TitleMain']))
    story.append(Paragraph("Documento Mestre Completo", styles['TitleMain']))
    story.append(Spacer(0, 0.5*cm))
    story.append(Paragraph("Tudo sobre o que criamos até agora", styles['Subtitle']))
    story.append(Paragraph("Não perder nenhuma vírgula", styles['Subtitle']))
    story.append(Spacer(0, 2*cm))

    # Info box
    info_data = [
        ['Data:', '21/02/2026'],
        ['Versão:', '1.0'],
        ['Status:', 'Documento Mestre para Sócios'],
        ['Responsável:', 'PH + Sócio FIREVON'],
    ]
    info_table = Table(info_data, colWidths=[4*cm, 8*cm], hAlign='CENTER')
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_GRAY),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_NAVY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(info_table)
    story.append(Spacer(0, 3*cm))

    # Tagline
    story.append(Paragraph('"Menos achismo. Mais processo. Mais conversão. Mais previsibilidade."', styles['FirevonQuoteText']))
    story.append(PageBreak())

    # ==================== ÍNDICE ====================
    story.append(Paragraph("ÍNDICE GERAL", styles['Heading1']))

    indice_items = [
        ['1.', 'MAPA DO DOCUMENTO', '3'],
        ['2.', 'IDENTIDADE VISUAL - FASE 0', '4'],
        ['3.', 'PSICOLOGIA E ESTRATÉGIA DE CONFIANÇA', '7'],
        ['4.', 'CAMADA A - EXTRAÇÃO FIEL', '10'],
        ['5.', 'CAMADA B - PLANO APRIMORADO', '18'],
        ['6.', 'PLANO DE EXECUÇÃO SEMANAL', '25'],
        ['7.', '6 VARIAÇÕES DE LOGOTIPO', '28'],
        ['8.', 'LOGOTIPOS CRIATIVOS/IMPACTANTES', '32'],
        ['9.', 'BRIEFING PARA DESIGNER', '36'],
        ['10.', 'CÓDIGOS SVG PARA LOGOTIPOS', '39'],
    ]

    indice_table = Table(indice_items, colWidths=[1.5*cm, 12*cm, 2*cm])
    indice_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), FIREVON_CHARCOAL),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('LINEABOVE', (0, 1), (-1, 1), 0.5, FIREVON_LIGHT_GRAY),
    ]))
    story.append(indice_table)
    story.append(PageBreak())

    # ==================== SEÇÃO 1: MAPA ====================
    story.append(Paragraph("1. MAPA DO DOCUMENTO", styles['Heading1']))

    mapa_data = [
        ['Seção', 'Descrição', 'Status'],
        ['Fase 0: Identidade Visual', 'Logotipo, Brandkit e Personalidade', '✅ Completo'],
        ['Fase 0.5: Confiança', 'Coleta humana e Arquitetura de Confiança', '✅ Completo'],
        ['Camada A: Extração Fiel', 'Dados extraídos do documento original', '✅ Completo'],
        ['Camada B: Plano Aprimorado', 'Estratégia, Sprints, Vendas, Governança', '✅ Completo'],
        ['Plano Semanal', '7 pessoas, do zero ao MVP', '✅ Completo'],
        ['Variações de Logo', '6 conceitos + 7 criativos + SVG', '✅ Completo'],
    ]

    mapa_table = Table(mapa_data, colWidths=[5*cm, 7*cm, 2.5*cm])
    mapa_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, FIREVON_LIGHT_GRAY]),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(mapa_table)
    story.append(PageBreak())

    # ==================== SEÇÃO 2: IDENTIDADE VISUAL ====================
    story.append(Paragraph("2. IDENTIDADE VISUAL - FASE 0", styles['Heading1']))
    story.append(Paragraph('Antes de definir estratégia, é necessário estabelecer a identidade visual que dará face e personalidade à marca.', styles['FirevonBodyText']))

    story.append(Paragraph("2.1 ARQUÉTIPO DE MARCA", styles['Heading2']))
    story.append(Paragraph("O CRIADOR (The Creator)", styles['Heading3']))
    story.append(Paragraph('O Criador é aquele que transforma visões em realidade. Ele é inovador, visionário e talentoso. Sua motivação principal é criar coisas de valor duradouro e expressar-se através da inovação.', styles['FirevonBodyText']))

    criador_data = [
        ['Visão:', 'Transformar caos em sistema; criar ordem onde há desordem'],
        ['Motivação:', 'Manifestar a visão através da criação de estruturas'],
        ['Medo:', 'Falhar na execução; criar algo sem valor ou durabilidade'],
        ['Estratégia:', 'Desenvolver capacidades artísticas e habilidades de controle'],
    ]
    criador_table = Table(criador_data, colWidths=[2.5*cm, 12*cm])
    criador_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_CHARCOAL),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(criador_table)

    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("O SÁBIO (The Sage) - Secundário", styles['Heading3']))
    story.append(Paragraph('Busca pela "verdade" dos dados e indicadores. Compartilha conhecimento através de frameworks e playbooks. Analítico, inteligente, especialista.', styles['FirevonBodyText']))
    story.append(PageBreak())

    # Personalidade
    story.append(Paragraph("2.2 PERSONALIDADE DA MARCA", styles['Heading2']))

    personalidade_data = [
        ['Dimensão', 'Traço'],
        ['Sinceridade', 'Autêntica, direta, sem promessas falsas'],
        ['Excitação', 'Inovadora, visionária, moderna'],
        ['Competência', 'Especialista, confiável, inteligente'],
        ['Sophisticação', 'Premium, exclusiva (para ICP selecionado)'],
        ['Rugosidade', 'Forte, resiliente, prática'],
    ]
    personalidade_table = Table(personalidade_data, colWidths=[5*cm, 9.5*cm])
    personalidade_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(personalidade_table)

    story.append(Spacer(0, 0.5*cm))
    story.append(Paragraph("Adjetivos que definem a Firevon:", styles['Heading3']))
    adjetivos = "Precisa • Eficaz • Estruturada • Visionária • Confiável • Analítica • Pragmática • Empoderadora"
    story.append(Paragraph(adjetivos, styles['FirevonOrangeText']))

    # Tom de Voz
    story.append(Spacer(0, 0.5*cm))
    story.append(Paragraph("2.3 TOM DE VOZ", styles['Heading2']))

    voz_data = [
        ['1. DIRETA', 'Não enrolamos. Vamos ao ponto. "Seu comercial depende de sorte. Vamos mudar isso."'],
        ['2. AUTORIDADE SEM ARROGÂNCIA', 'Sabemos, mas não humilhamos. "Aqui está o que funciona"'],
        ['3. ORIENTADA A AÇÃO', 'Verbos, não substantivos. "Implemente", "Execute", "Meça"'],
        ['4. HUMANA E EMPÁTICA', 'Entendemos a dor, mas oferecemos solução. "Sabemos que é frustrante. Aqui está o caminho."'],
    ]
    voz_table = Table(voz_data, colWidths=[4*cm, 10.5*cm])
    voz_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(voz_table)

    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("O que NÃO somos:", styles['Heading3']))
    story.append(Paragraph('❌ "Blá blá blá" corporativo • ❌ Promessas de "sucesso overnight" • ❌ Linguagem técnica excessiva • ❌ Jargões de startup vazios', styles['FirevonBodyText']))

    # Valores
    story.append(PageBreak())
    story.append(Paragraph("2.4 VALORES DA MARCA (CORE VALUES)", styles['Heading2']))

    valores_data = [
        ['1', 'PREVISIBILIDADE ACIMA DE TUDO', 'Criamos sistemas, não dependemos de sorte'],
        ['2', 'DADOS, NÃO OPINIÕES', '"Achismo" é nosso inimigo; evidência é nossa arma'],
        ['3', 'EXECUÇÃO > ESTRATÉGIA', 'Plano sem execução é ilusão'],
        ['4', 'TRANSPARÊNCIA RADICAL', 'Dizemos o que funciona, o que não funciona, e por quê'],
        ['5', 'RESPONSABILIDADE COMPARTILHADA', 'Cliente é co-criador, não espectador'],
    ]
    valores_table = Table(valores_data, colWidths=[1*cm, 4.5*cm, 9*cm])
    valores_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 1), (2, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 1), (0, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (1, 1), (1, -1), FIREVON_NAVY),
        ('TEXTCOLOR', (2, 1), (2, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(valores_table)

    # História
    story.append(Spacer(0, 0.5*cm))
    story.append(Paragraph("2.5 HISTÓRIA DA MARCA", styles['Heading2']))

    story.append(Paragraph("A ORIGEM:", styles['Heading3']))
    story.append(Paragraph('A Firevon nasceu de uma frustração recorrente observada em centenas de PMEs B2B: empresas com ótimos produtos, times talentosos e mercado disposto a comprar, mas presas em um ciclo de montanha-russa de resultados.', styles['FirevonBodyText']))

    story.append(Spacer(0, 0.2*cm))
    story.append(Paragraph("A DESCOBERTA:", styles['Heading3']))
    story.append(Paragraph('O problema nunca era marketing isoladamente, ou vendas isoladamente, ou gestão isoladamente. O problema era a falta de INTEGRAÇÃO entre os três.', styles['FirevonBodyText']))

    story.append(Spacer(0, 0.2*cm))
    story.append(Paragraph("A SOLUÇÃO FIREVON:", styles['Heading3']))
    story.append(Paragraph('Nascemos para instalar SISTEMAS INTEGRADOS de crescimento previsível.', styles['FirevonBodyText']))

    story.append(Spacer(0, 0.2*cm))
    story.append(Paragraph("O NOME:", styles['Heading3']))
    story.append(Paragraph('FIREVON = FIRE + VON (força/impulso) + ON (atividade contínua). Fogo representa transformação, energia, paixão. Von denota origem, força proveniente. On indica algo que está sempre ativo, em movimento.', styles['FirevonBodyText']))
    story.append(Paragraph('"Firevon: A força transformadora que mantém seu crescimento sempre ativo."', styles['FirevonQuoteText']))

    # Paleta de Cores
    story.append(PageBreak())
    story.append(Paragraph("2.6 PALETA DE CORES", styles['Heading2']))

    cores_data = [
        ['COR', 'HEX', 'RGB', 'USO'],
        ['Fire Orange', '#FF6B35', '255,107,53', 'Principal - Energia, Transformação, Ação'],
        ['Deep Navy', '#1A1F36', '26,31,54', 'Texto/Base - Autoridade, Confiança'],
        ['Electric Teal', '#00D4C7', '0,212,199', 'Accent/Destaque - Inovação, Tecnologia'],
        ['Stone Gray', '#718096', '113,128,150', 'Secundário'],
        ['White', '#FFFFFF', '255,255,255', 'Fundo/Negativo'],
    ]
    cores_table = Table(cores_data, colWidths=[3.5*cm, 2*cm, 2.5*cm, 7.5*cm])
    cores_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(cores_table)

    # ==================== SEÇÃO 3: PSICOLOGIA ====================
    story.append(PageBreak())
    story.append(Paragraph("3. PSICOLOGIA E ESTRATÉGIA DE CONFIANÇA - FASE 0.5", styles['Heading1']))
    story.append(Paragraph('"Dados dizem O QUÊ. Pessoas dizem POR QUÊ."', styles['FirevonQuoteText']))

    story.append(Paragraph("3.1 EQUAÇÃO DA CONFIANÇA", styles['Heading2']))
    story.append(Paragraph('CONFIANÇA = (CREDIBILIDADE + CONEXÃO + CONSISTÊNCIA) ÷ VULNERABILIDADE PERCEBIDA', styles['FirevonOrangeText']))

    # 5 Camadas
    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("3.2 AS 5 CAMADAS DE CONFIANÇA", styles['Heading2']))

    confianca_data = [
        ['CAMADA 5', 'CONFIANÇA DE PARCEIROS', '"Nós crescemos juntos." Co-criação de estratégia, Transparência total de margens, Compartilhamento de riscos'],
        ['CAMADA 4', 'CONFIANÇA DE CAPACIDADE', '"Vocês entregam consistentemente." Quick wins nas primeiras semanas, Metodologia comprovada, Equipe técnica qualificada'],
        ['CAMADA 3', 'CONFIANÇA DE INTENÇÃO', '"Vocês querem meu sucesso, não só meu dinheiro." Escuta profunda, Disputa de verdadeira sobre pagamento, Dizem "não" quando não faz sentido'],
        ['CAMADA 2', 'CONFIANÇA DE CARÁTER', '"Vocês são íntegros." Fazem o que prometem, Admitem erros, Sem vendas agressivas'],
        ['CAMADA 1', 'CONFIANÇA DE SEGURANÇA', '"É seguro conversar com vocês." Confidencialidade, Sem julgamentos, Espaço psicológico seguro'],
    ]
    confianca_table = Table(confianca_data, colWidths=[2*cm, 4*cm, 10.5*cm])
    confianca_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_NAVY),
        ('TEXTCOLOR', (2, 0), (2, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(confianca_table)

    # Protocolo 7 dias
    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("3.3 PROTOCOLO DE CONSTRUÇÃO DE CONFIANÇA (PRIMEIROS 7 DIAS)", styles['Heading2']))

    protocolo_data = [
        ['Dia 1-2', 'Segurança Psicológica', 'Reunião inicial: Mais escuta do que fala. "Tudo que disser aqui fica entre nós." Validar: "O que você está sentindo faz sentido."'],
        ['Dia 3-4', 'Demonstração de Competência', 'Entregar algo rápido: Um insight, um mapa. Mostrar: "Já vimos isso antes e resolvemos."'],
        ['Dia 5-6', 'Conexão Humana', 'Perguntar: "O que ninguém perguntou ainda?" Compartilhar vulnerabilidade'],
        ['Dia 7', 'Consolidação', 'Recap: "O que aprendemos sobre vocês". Proposta com base no que foi ouvido. Quick win identificado'],
    ]
    protocolo_table = Table(protocolo_data, colWidths=[2*cm, 3.5*cm, 11*cm])
    protocolo_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_NAVY),
        ('TEXTCOLOR', (2, 0), (2, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(protocolo_table)

    # Framework ESCUTAR
    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("3.4 FRAMEWORK ESCUTAR FIREVON", styles['Heading2']))

    escutar_data = [
        ['E', 'EXPLORAR', '"Me conta mais sobre isso..."'],
        ['S', 'SINTONIZAR', '"Entendi que você está sentindo..."'],
        ['C', 'CURAR', '"O mais importante disso tudo é..."'],
        ['U', 'UNCOVER', '"O que ninguém perguntou ainda..."'],
        ['T', 'TRADUZIR', '"Então, na prática, isso significa..."'],
        ['A', 'ACORDAR', '"Vamos combinar então..."'],
        ['R', 'REFORÇAR', '"O que conversamos hoje foi..."'],
    ]
    escutar_table = Table(escutar_data, colWidths=[1*cm, 2.5*cm, 13*cm])
    escutar_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(escutar_table)

    # ==================== SEÇÃO 4: CAMADA A ====================
    story.append(PageBreak())
    story.append(Paragraph("4. CAMADA A - EXTRAÇÃO FIEL", styles['Heading1']))
    story.append(Paragraph('Dados extraídos do documento original, sem invenções.', styles['FirevonBodyText']))

    story.append(Paragraph("4.1 RESUMO EXECUTIVO", styles['Heading2']))
    story.append(Paragraph('A Firevon é uma consultoria/implementadora que instala um sistema integrado de crescimento previsível, conectando demanda (Marketing), conversão (Comercial) e rotina de execução (Gestão).', styles['FirevonBodyText']))

    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("4.2 POSICIONAMENTO", styles['Heading2']))
    story.append(Paragraph('"Para PMEs que querem crescer com previsibilidade, a Firevon implanta um sistema integrado de Marketing, Comercial e Gestão para transformar estratégia em execução e resultados mensuráveis."', styles['FirevonQuoteText']))

    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("4.3 ICP (CLIENTE IDEAL)", styles['Heading2']))

    icp_data = [
        ['Problema que Resolvemos', '"Meu comercial depende de sorte" • "Tem lead, mas não vira venda" • "O time não segue processo" • "Não tenho números confiáveis" • "Tudo fica na minha cabeça"'],
        ['Resultado que Entregamos', 'Pipeline previsível e qualificado • Taxa de conversão maior • Rotina de gestão sustentável • Indicadores claros para decisão'],
        ['Ticket', 'Negócio com ticket médio de médio a alto e venda consultiva'],
        ['Time', 'Time comercial (ao menos 1 closer) ou fundador vendendo'],
        ['Situação', 'Oferta validada, mas crescimento travado por falta de previsibilidade'],
        ['Anti-ICP', 'Quem quer apenas "posts" • Sem disposição para executar rotina • Negócios sem oferta clara ou caixa mínimo'],
    ]
    icp_table = Table(icp_data, colWidths=[4*cm, 12.5*cm])
    icp_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_NAVY),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(icp_table)

    # Escada de Valor
    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("4.4 ESCADA DE VALOR (OFERTAS)", styles['Heading2']))

    oferta_data = [
        ['Nível', 'Nome', 'Duração', 'Entregáveis'],
        ['Entrada', 'Diagnóstico Firevon 360', '7-14 dias', 'Mapa do funil, gargalos, baseline, plano 90 dias'],
        ['Principal', 'Motor de Receita Firevon', '6-10 semanas', 'ICP, canal primário, CRM, scripts, SLA, dashboard, rituais'],
        ['Recorrente', 'Acompanhamento de Performance', '3-6 meses', 'War-room semanal, otimização, QBR mensal, governança'],
    ]
    oferta_table = Table(oferta_data, colWidths=[2*cm, 4*cm, 2.5*cm, 8*cm])
    oferta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(oferta_table)

    # Framework FIREVON OS
    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("4.5 FIREVON OS - MÉTODO EM 5 ETAPAS", styles['Heading2']))

    framework_data = [
        ['1', 'DIRECIONAR', 'ICP, oferta, mensagem, metas e indicadores'],
        ['2', 'ATRAIR', 'Canal primário, campanhas/rotinas, conteúdo e listas'],
        ['3', 'CONVERTER', 'Pipeline, scripts, cadência, qualificação e proposta'],
        ['4', 'OPERAR', 'Rituais de gestão, dashboard, accountability e execução'],
        ['5', 'ESCALAR', 'Otimização, automação, parcerias e replicação'],
    ]
    framework_table = Table(framework_data, colWidths=[1*cm, 3*cm, 12.5*cm])
    framework_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(framework_table)

    # Pilares
    story.append(PageBreak())
    story.append(Paragraph("4.6 PILARES DE ATUAÇÃO", styles['Heading2']))

    pilares_data = [
        ['Marketing', 'Demanda Previsível', 'Gerar oportunidades qualificadas com consistência', 'Reuniões qualificadas/semana, Conversão visita→lead, Custo por reunião'],
        ['Comercial', 'Conversão e Receita', 'Transformar oportunidades em faturamento com processo', 'Show rate, Call→proposta, Win rate, Ticket médio'],
        ['Gestão', 'Performance Sustentada', 'Fazer o sistema rodar sem depender de esforço heroico', 'Aderência aos rituais, Time to value, NPS, Churn'],
    ]
    pilares_table = Table(pilares_data, colWidths=[2.5*cm, 3.5*cm, 6*cm, 6*cm])
    pilares_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(pilares_table)

    # Mensagens
    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("4.7 MENSAGENS E SLOGANS", styles['Heading2']))

    mensagens = [
        '• Previsibilidade não é sorte - é sistema',
        '• Estratégia sem execução é ruído. A gente instala o motor',
        '• Marketing, Vendas e Gestão no mesmo ritmo',
    ]
    for msg in mensagens:
        story.append(Paragraph(msg, styles['FirevonBodyText']))

    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("Slogans:", styles['Heading3']))
    slogans = [
        '1. Firevon - Previsibilidade em execução',
        '2. Firevon - Onde estratégia vira rotina e resultado',
        '3. Firevon - Sistema de performance para crescer com controle',
        '4. Firevon - Menos achismo. Mais resultado',
    ]
    for slogan in slogans:
        story.append(Paragraph(slogan, styles['FirevonSmallText']))

    # Plano 12 Semanas
    story.append(PageBreak())
    story.append(Paragraph("4.8 PLANO 12 SEMANAS", styles['Heading2']))

    plano_data = [
        ['Fase 1', 'Semanas 1-2', 'Fundação', 'ICP/anti-ICP, Escada de valor, Framework, Metas 90 dias'],
        ['Fase 2', 'Semanas 3-4', 'Ativos', 'Landing Diagnóstico 360, Deck de vendas, CRM, Proposta e objeções'],
        ['Fase 3', 'Semanas 5-8', 'Aquisição e Conversão', 'Canal primário 60 dias, Ajuste copy, 2 mini-cases, SLA MKT-Vendas'],
        ['Fase 4', 'Semanas 9-12', 'Governança e Escala', 'Dashboard, Rituais, Onboarding, QBR mensal, Cases'],
    ]
    plano_table = Table(plano_data, colWidths=[2*cm, 2.5*cm, 3*cm, 11*cm])
    plano_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 1), (2, -1), 'Helvetica-Bold'),
        ('FONTNAME', (3, 1), (3, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(plano_table)

    # KPIs
    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("4.9 INDICADORES DE SUCESSO", styles['Heading2']))

    kpis_data = [
        ['LEADING (Antecipam)', 'Reuniões qualificadas/semana • Show rate • Call→proposta • Win rate • Tempo de resposta • Execução de rituais'],
        ['LAGGING (Resultado)', 'Receita (MRR) • Margem • Churn/renovação • NPS • Previsibilidade de pipeline'],
    ]
    kpis_table = Table(kpis_data, colWidths=[4*cm, 12.5*cm])
    kpis_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(kpis_table)

    # Próximos Passos
    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("4.10 PRÓXIMOS PASSOS (72 HORAS)", styles['Heading2']))

    passos_data = [
        ['1', 'Escolher 1-2 segmentos prioritários', 'Alta'],
        ['2', 'Fechar a escada de valor e faixa de preço', 'Alta'],
        ['3', 'Escrever o framework em 1 página', 'Alta'],
        ['4', 'Montar a landing do Diagnóstico 360', 'Alta'],
        ['5', 'Configurar CRM com pipeline', 'Alta'],
        ['6', 'Produzir 5 conteúdos de autoridade', 'Média'],
        ['7', 'Executar o primeiro ciclo de aquisição (7 dias)', 'Média'],
    ]
    passos_table = Table(passos_data, colWidths=[1*cm, 10*cm, 3.5*cm])
    passos_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (2, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (1, 0), (2, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(passos_table)

    # ==================== SEÇÃO 5: CAMADA B ====================
    story.append(PageBreak())
    story.append(Paragraph("5. CAMADA B - PLANO APRIMORADO", styles['Heading1']))

    story.append(Paragraph("5.1 ESTRATÉGIA DE EXECUÇÃO (90 DIAS)", styles['Heading2']))
    story.append(Paragraph('Validar o sistema integrado de crescimento previsível em um nicho de mercado específico, gerando os primeiros cases de sucesso que comprovem a eficácia do método.', styles['FirevonBodyText']))

    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("Canal Primário Recomendado: Outbound Ativo via LinkedIn e E-mail", styles['FirevonOrangeText']))
    story.append(Paragraph('Por quê? Assertividade (vai direto no ICP), Velocidade de aprendizado (feedback imediato), Custo-benefício (investimento baixo), Alinhamento (venda consultiva).', styles['FirevonBodyText']))

    story.append(Spacer(0, 0.3*cm))
    story.append(Paragraph("Alavancas de Crescimento (por ordem de impacto):", styles['Heading3']))
    alavancas = [
        '1. Definição e Foco no ICP - Dizer "não" para clientes fora do perfil',
        '2. Implementação do "Motor de Receita Firevon" - Execução disciplinada',
        '3. Criação de Provas Sociais - Documentar e divulgar resultados',
    ]
    for alavanca in alavancas:
        story.append(Paragraph(alavanca, styles['FirevonBodyText']))

    # Sprints
    story.append(PageBreak())
    story.append(Paragraph("5.2 PLANO 90 DIAS EM SPRINTS", styles['Heading2']))

    sprint_data = [
        ['Sprint 1', 'Semanas 1-2', 'Fundação e Alinhamento', 'Validar ICP, oferta e framework. 100% dos entregáveis aprovados pelo CEO'],
        ['Sprint 2', 'Semanas 3-4', 'Construção dos Ativos', 'Landing Page, Deck, CRM. Conversão > 2%; 100% do time usando CRM'],
        ['Sprint 3', 'Semanas 5-6', 'Primeira Campanha', 'Lista 50-100 contatos, cadência, relatório. Taxa de resposta > 5%; 3-5 reuniões'],
        ['Sprint 4', 'Semanas 7-8', 'Otimização', 'Ajustes, primeiro cliente fechado, plano onboarding. 1 cliente; NPS kickoff > 8'],
        ['Sprint 5', 'Semanas 9-10', 'Entrega de Valor', 'Onboarding, provas, depoimento. 100% aderência; NPS > 8'],
        ['Sprint 6', 'Semanas 11-12', 'Padronização', 'Playbook, case, plano v2. Playbook validado; case publicado'],
    ]
    sprint_table = Table(sprint_data, colWidths=[2*cm, 2.5*cm, 4*cm, 8*cm])
    sprint_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 1), (2, -1), 'Helvetica-Bold'),
        ('FONTNAME', (3, 1), (3, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(sprint_table)

    # Pitches
    story.append(PageBreak())
    story.append(Paragraph("5.3 ARGUMENTOS DE VENDA", styles['Heading2']))

    story.append(Paragraph("Pitch de 30s:", styles['Heading3']))
    story.append(Paragraph('"A Firevon instala um sistema de crescimento previsível para PMEs B2B. Integramos marketing, vendas e gestão para transformar potencial em performance mensurável. Menos achismo, mais resultado."', styles['FirevonQuoteText']))

    story.append(Spacer(0, 0.2*cm))
    story.append(Paragraph("Frases-Míssil:", styles['Heading3']))
    frases = [
        '• Crescimento não é sorte, é sistema',
        '• Nós instalamos o motor do seu crescimento previsível',
        '• Marketing, Vendas e Gestão no mesmo ritmo',
        '• Chega de montanha-russa de resultados',
        '• Transformamos potencial em performance mensurável',
        '• Menos achismo, mais processo',
        '• Sua estratégia vira rotina e resultado',
        '• Previsibilidade é liberdade',
        '• Nós não vendemos teoria, nós implementamos execução',
        '• Onde o seu time se torna uma máquina de vendas',
    ]
    for frase in frases:
        story.append(Paragraph(frase, styles['FirevonSmallText']))

    # Dashboard CEO
    story.append(PageBreak())
    story.append(Paragraph("5.4 DASHBOARD DO CEO (15 KPIs)", styles['Heading2']))

    kpi_ceo_data = [
        ['KPI', 'Definição', 'Fórmula', 'Pilar'],
        ['Leads Qualificados (MQLs)', 'Leads que atendem critérios mínimos', 'Contagem no CRM', 'Marketing'],
        ['Reuniões Agendadas', 'Primeiras reuniões com MQLs', 'Contagem no calendário', 'Marketing'],
        ['Show Rate', '% reuniões agendadas que aconteceram', '(Realizadas/Agendadas) × 100', 'Vendas'],
        ['Conversão Reunião→Proposta', '% reuniões que viraram proposta', '(Propostas/Reuniões) × 100', 'Vendas'],
        ['Win Rate', '% propostas fechadas', '(Fechadas/Propostas) × 100', 'Vendas'],
        ['Ciclo de Vendas', 'Dias até o fechamento', 'Data Fechamento - Data Lead', 'Vendas'],
        ['Ticket Médio', 'Valor médio dos contratos', 'Receita Total / Clientes', 'Vendas'],
        ['MRR', 'Receita recorrente mensal', 'Soma mensalidades', 'Financeiro'],
        ['CAC', 'Custo para adquirir cliente', '(MKT + Vendas) / Novos Clientes', 'Financeiro'],
        ['LTV', 'Receita total por cliente', '(Ticket × Compras/Ano) × Anos', 'Financeiro'],
        ['LTV/CAC Ratio', 'Relação LTV sobre CAC', 'LTV / CAC', 'Financeiro'],
        ['NPS', 'Lealdade do cliente', '% Promotores - % Detratores', 'Sucesso'],
        ['Churn', '% clientes que cancelaram', '(Cancelados/Total) × 100', 'Sucesso'],
        ['Aderência aos Rituais', '% rituais realizados', '(Realizados/Planejados) × 100', 'Gestão'],
        ['Time to First Value', 'Dias para primeiro valor', 'Primeiro Valor - Início', 'Sucesso'],
    ]
    kpi_ceo_table = Table(kpi_ceo_data, colWidths=[3*cm, 3.5*cm, 3*cm, 3*cm])
    kpi_ceo_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 0.3, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(kpi_ceo_table)

    # ==================== SEÇÃO 6: EQUIPE ====================
    story.append(PageBreak())
    story.append(Paragraph("6. PLANO DE EXECUÇÃO SEMANAL", styles['Heading1']))

    story.append(Paragraph("6.1 EQUIPE FIREVON", styles['Heading2']))

    equipe_data = [
        ['PH', 'CMO/Estrategista', 'Liderança Geral - Vision keeper, decisões finais, integração'],
        ['Thauane', 'Design', 'Lead Visual - Logotipo, brandkit, UI, social media'],
        ['Marcelo', 'Social Media', 'Conteúdo + Distribuição - Copy, calendário, community management'],
        ['Lucas', 'Growth Perf', 'Dados + Otimização - Analytics, tracking, A/B tests, relatórios'],
        ['João', 'Web', 'Desenvolvimento - Landing page, site, CRM, implementações técnicas'],
        ['Pedro', 'Tráfego', 'Aquisição Paga - Campanhas, audiences, criativos, orçamento'],
        ['SM', 'Suporte/Mídia', 'Operações + Coordenação - Checklist, prazos, comunicação, blockers'],
    ]
    equipe_table = Table(equipe_data, colWidths=[2.5*cm, 3*cm, 10*cm])
    equipe_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), FIREVON_NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 1), (2, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(equipe_table)

    # ==================== SEÇÃO 7: LOGOTIPOS ====================
    story.append(PageBreak())
    story.append(Paragraph("7. 6 VARIAÇÕES DE LOGOTIPO", styles['Heading1']))

    logo_desc = [
        ['Var 1', 'Wordmark Minimal', 'FIREVON em negrito, linha laranja abaixo. Uso: Corporativo, B2B'],
        ['Var 2', 'Camel Case Dinâmico', 'F + ireVon, triângulos laterais. Uso: Startups, Tech'],
        ['Var 3', 'Monograma FV', 'Letras FV entrelaçadas em hexágono. Uso: Apps, Social'],
        ['Var 4', 'Lowcase Acessível', 'firevon com arcos sobre letras. Uso: Comunicação interna'],
        ['Var 5', 'Two Words', 'FIRE · VON com seta ascendente. Uso: Ads, Impacto'],
        ['Var 6', 'F/V Abstrato', 'Setas convergentes formando M. Uso: Premium, Selos'],
    ]
    logo_table = Table(logo_desc, colWidths=[1.5*cm, 3.5*cm, 10.5*cm])
    logo_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_NAVY),
        ('TEXTCOLOR', (2, 0), (2, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(logo_table)

    # ==================== SEÇÃO 8: BRIEFING ====================
    story.append(PageBreak())
    story.append(Paragraph("8. BRIEFING PARA DESIGNER", styles['Heading1']))

    briefing_data = [
        ['Nome da marca', 'FIREVON'],
        ['Segmento', 'Consultoria de Crescimento B2B'],
        ['Público-alvo', 'PMEs B2B, 20-50 funcionários, venda consultiva'],
        ['Estética', 'Tech moderna + Premium B2B + Confiança'],
        ['Referências', 'Stripe, Notion, Linear, Figma'],
        ['NÃO usar', 'Serif tradicional, gradiente agressivo, formas redondas, ícones genéricos'],
    ]
    briefing_table = Table(briefing_data, colWidths=[4*cm, 12.5*cm])
    briefing_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_NAVY),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(briefing_table)

    story.append(Spacer(0, 0.5*cm))
    story.append(Paragraph("Versões Necessárias:", styles['Heading2']))
    versoes = [
        '1. Principal - Logo completo (símbolo + texto)',
        '2. Ícone apenas - Símbolo FV quadrado',
        '3. Horizontal - Símbolo à esquerda, texto à direita',
        '4. Stacked - Símbolo acima, texto abaixo',
        '5. Positivo - Fundo branco/claro',
        '6. Negativo - Fundo escuro ou em preto',
        '7. Monocromático - Preto sobre branco',
    ]
    for versao in versoes:
        story.append(Paragraph(versao, styles['FirevonSmallText']))

    # ==================== SEÇÃO 9: CHECKLIST FINAL ====================
    story.append(PageBreak())
    story.append(Paragraph("9. CHECKLIST FINAL - PRONTO PARA RODAR", styles['Heading1']))

    checklist_data = [
        ['Pronto para Adquirir', '• ICP e Personas definidos e validados\n• Escada de valor e precificação definidos\n• Canal primário de aquisição definido\n• Landing page no ar e convertendo\n• Conteúdos de autoridade publicados'],
        ['Pronto para Converter', '• CRM implementado e time treinado\n• Pipeline de vendas com etapas e critérios\n• Deck de vendas e proposta padronizados\n• Scripts de qualificação e diagnóstico\n• Cadência de follow-up e templates'],
        ['Pronto para Operar', '• Rituais de gestão agendados\n• Dashboard de KPIs implementado\n• Processo de onboarding desenhado\n• Contrato de prestação revisado\n• Ferramentas de gestão definidas'],
        ['Pronto para Escalar', '• Primeiro case de sucesso documentado\n• Playbook de vendas documentado\n• Playbook de entrega documentado\n• Processo de NPS estabelecido\n• Plano de contratação futuro'],
    ]
    checklist_table = Table(checklist_data, colWidths=[3.5*cm, 13*cm])
    checklist_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 0), (0, -1), FIREVON_ORANGE),
        ('TEXTCOLOR', (1, 0), (1, -1), FIREVON_CHARCOAL),
        ('GRID', (0, 0), (-1, -1), 0.5, FIREVON_LIGHT_GRAY),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(checklist_table)

    # ==================== FEVERAMENTO ====================
    story.append(PageBreak())
    story.append(Spacer(0, 4*cm))

    story.append(Paragraph("FIREVON", styles['TitleMain']))
    story.append(Spacer(0, 0.5*cm))
    story.append(Paragraph("Previsibilidade em Execução", styles['Subtitle']))
    story.append(Spacer(0, 1*cm))
    story.append(Paragraph('"Menos achismo. Mais processo. Mais conversão. Mais previsibilidade."', styles['FirevonQuoteText']))
    story.append(Spacer(0, 2*cm))
    story.append(Paragraph('Versão 1.0 | 21/02/2026', styles['FirevonSmallText']))

    # Build PDF
    doc.build(story, onFirstPage=create_header_footer, onLaterPages=create_header_footer)
    print(f"PDF gerado com sucesso: {PDF_PATH}")

if __name__ == "__main__":
    build_document()
