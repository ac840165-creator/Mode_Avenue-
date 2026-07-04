from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import io
from datetime import datetime

def generate_invoice_pdf(invoice_data):
    """
    Generate a PDF invoice from invoice data
    Returns PDF as bytes
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2a5298')
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor=colors.HexColor('#2d3748')
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        textColor=colors.HexColor('#4a5568')
    )
    
    # Build story
    story = []
    
    # Company Header
    story.append(Paragraph("Mode Avenue", title_style))
    story.append(Paragraph("Fashion E-commerce Platform", normal_style))
    story.append(Paragraph("123 Fashion Street, New York, NY 10001", normal_style))
    story.append(Paragraph("Phone: (555) 123-4567 | Email: info@modeavenue.com", normal_style))
    story.append(Spacer(1, 20))
    
    # Invoice Title and Details
    story.append(Paragraph("INVOICE", title_style))
    story.append(Spacer(1, 10))
    
    # Invoice Info Table
    invoice_info_data = [
        ['Invoice Number:', invoice_data['order_id']],
        ['Order Date:', invoice_data['order_date']],
        ['Payment Method:', invoice_data['payment_method']],
        ['Status:', 'PAID']
    ]
    
    invoice_info_table = Table(invoice_info_data, colWidths=[2*inch, 3*inch])
    invoice_info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8f9fa')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0'))
    ]))
    
    story.append(invoice_info_table)
    story.append(Spacer(1, 20))
    
    # Bill To Section
    story.append(Paragraph("Bill To:", heading_style))
    story.append(Paragraph(f"<b>{invoice_data['customer_name']}</b>", normal_style))
    story.append(Paragraph(invoice_data['customer_email'], normal_style))
    story.append(Paragraph(invoice_data['shipping_address'], normal_style))
    story.append(Spacer(1, 20))
    
    # Order Items Table
    story.append(Paragraph("Order Details:", heading_style))
    
    # Table headers
    headers = ['#', 'Product Name', 'Quantity', 'Unit Price', 'Total']
    data = [headers]
    
    # Add items
    for i, item in enumerate(invoice_data['order_items'], 1):
        data.append([
            str(i),
            item['name'],
            str(item['quantity']),
            f"${item['price']:.2f}",
            f"${item['total']:.2f}"
        ])
    
    # Create table
    table = Table(data, colWidths=[0.5*inch, 3*inch, 1*inch, 1*inch, 1*inch])
    table.setStyle(TableStyle([
        # Header style
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2a5298')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        
        # Data rows
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('ALIGN', (2, -1), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        
        # Grid
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')])
    ]))
    
    story.append(table)
    story.append(Spacer(1, 20))
    
    # Summary Table
    summary_data = [
        ['Subtotal:', f"${invoice_data['subtotal']:.2f}"],
        ['Tax (8%):', f"${invoice_data['tax']:.2f}"],
        ['Shipping:', 'FREE'],
        ['Total:', f"${invoice_data['total']:.2f}"]
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 1.5*inch])
    summary_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -2), 'RIGHT'),
        ('ALIGN', (0, -1), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, -1), (-1, -1), 12),
        ('TEXTCOLOR', (0, -1), (-1, -1), colors.HexColor('#2a5298')),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('LINEBELOW', (0, -2), (-1, -2), 2, colors.HexColor('#2a5298'))
    ]))
    
    story.append(summary_table)
    story.append(Spacer(1, 30))
    
    # Footer
    story.append(Paragraph("Thank you for your business!", normal_style))
    story.append(Paragraph("This is a computer-generated invoice and does not require a signature.", normal_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Questions about this invoice? Contact us at billing@modeavenue.com", normal_style))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    
    return buffer.getvalue()
