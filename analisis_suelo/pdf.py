import os
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, PageBreak







# Obtener la ruta a la carpeta de descargas
downloads_path = str(Path.home() / "Downloads")  # Funciona para Windows, macOS, y Linux
img_path = str(Path.home() / "static/images")
file_name = os.path.join(downloads_path, "informe.pdf")  # Guardar en Descargas

# Ruta de la imagen del logo (asegúrate de colocar el nombre correcto de tu imagen)
logo_path = os.path.join(downloads_path, "keittweb.png")

# Crear el documento
pdf = SimpleDocTemplate(file_name, pagesize=letter)
# Establecer márgenes
margin = 0.5 * inch  # Cambia este valor según tus necesidades
pdf = SimpleDocTemplate(file_name, pagesize=letter, rightMargin=margin, leftMargin=margin, topMargin=margin, bottomMargin=margin)
styles = getSampleStyleSheet()

# Elementos del PDF
elements = []

# Añadir la imagen del logo y mantener su proporción
logo = Image(logo_path)
logo._restrictSize(1 * inch, 1 * inch)  # Restringir el tamaño sin perder proporción
logo.preserveAspectRatio = True  # Mantener la proporción
logo.mask = 'auto'  # Ayuda a mantener la calidad

# Crear una tabla con dos columnas, el logo en la primera columna, vacío en la segunda
logo_table = Table([[logo, '']], colWidths=[50, 450])  # Ajusta los anchos según el tamaño de la página
logo_table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (0, 0), 'LEFT'),  # Alinear el logo a la izquierda
    ('VALIGN', (0, 0), (0, 0), 'TOP')    # Alinear el logo en la parte superior
]))

elements.append(logo_table)

# Título del documento
title = Paragraph("Informe de Análisis de Suelo", styles['Title'])
elements.append(title)

# Espacio en blanco
elements.append(Paragraph("<br/>", styles['Normal']))

# Subtítulo
subtitle = Paragraph("Datos del Cliente", styles['Heading2'])
elements.append(subtitle)

# Datos de ejemplo (esto lo cambiarás luego con los datos reales)
client_data = [
    ['Nombre:', 'Juan Pérez'],
    ['Fecha:', '28 de Octubre, 2024'],
    ['Ubicación:', 'Valledupar, Cesar'],
]

# Tabla de datos del cliente
table = Table(client_data, colWidths=[120, 320])  # Aumenta el ancho de la segunda columna
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.grey),  # Color de fondo solo en la primera fila
    ('TEXTCOLOR', (0, 0), (0, 0), colors.whitesmoke),  # Texto blanco solo en la primera fila
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
]))

elements.append(table)

# Espacio en blanco
elements.append(Paragraph("<br/><br/>", styles['Normal']))

# Sección de resultados de análisis
analysis_title = Paragraph("Resultados del Análisis de Suelo", styles['Heading2'])
elements.append(analysis_title)

# Datos de ejemplo para el análisis
analysis_data = [
    ['Nutriente', 'Valor (kg/ha)', 'Óptimo', 'Estado'],
    ['pH', '6.5', '6.0 - 7.0', 'Óptimo'],
    ['Materia Orgánica', '3.0', '5.0 - 10.0', 'Bajo'],
    ['Nitrógeno (N)', '50', '40 - 80', 'Óptimo'],
    ['Fósforo (P)', '15', '25 - 30', 'Bajo'],
    ['Potasio (K)', '40', '80 - 120', 'Óptimo'],
    ['Calcio (Ca)', '120', '100 - 200', 'Elevado'],
    ['Magnesio (Mg)', '30', '20 - 50', 'Bajo'],
    ['Hierro (Fe)', '50', '30 - 100', 'Óptimo'],
    ['Cobre (Cu)', '8', '5 - 10', 'Elevado'],
    ['Zinc (Zn)', '20', '15 - 25', 'Óptimo'],
]

# Tabla de resultados de análisis
analysis_table = Table(analysis_data, colWidths=[180, 120, 120, 120])  # Ajustar anchos de columnas
analysis_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.lightgrey),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  # Color del texto
]))
elements.append(analysis_table)

# Salto de página
elements.append(PageBreak())

# Sección de recomendaciones
recommendations_title = Paragraph("Recomendaciones", styles['Heading2'])
elements.append(recommendations_title)

# Recomendaciones para cada nutriente (puedes ajustar los textos según tus necesidades)
recommendations_data = [
    ['Nutriente', 'Recomendaciones'],
    ['pH', 'Mantener entre 6.0 y 7.0. Considerar enmiendas si es necesario.'],
    ['Materia Orgánica', 'Incrementar la materia orgánica mediante compost o abonos.'],
    ['Nitrógeno (N)', 'Aplicar fertilizantes nitrogenados según la necesidad del cultivo.'],
    ['Fósforo (P)', 'Incorporar fósforo adicional si los niveles son bajos.'],
    ['Potasio (K)', 'Asegurar un suministro adecuado de potasio para un crecimiento saludable.'],
    ['Calcio (Ca)', 'Verificar la disponibilidad de calcio y ajustar si es necesario.'],
    ['Magnesio (Mg)', 'Añadir magnesio si se observan deficiencias.'],
    ['Hierro (Fe)', 'Aplicar quelatos de hierro si hay signos de clorosis.'],
    ['Cobre (Cu)', 'Mantener los niveles de cobre dentro de los límites seguros.'],
    ['Zinc (Zn)', 'Aplicar zinc si se presentan síntomas de deficiencia.'],
]

# Tabla de recomendaciones
recommendations_table = Table(recommendations_data, colWidths=[120, 400])  # Ajustar anchos de columnas
recommendations_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.lightgrey),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
]))
elements.append(recommendations_table)

# Guardar el archivo PDF
pdf.build(elements)

print(f"PDF guardado en: {file_name}")
