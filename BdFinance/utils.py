from io import BytesIO
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import io
from xhtml2pdf import pisa

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None

def render_to_pdf(template,context={}):
    template = get_template(template)
    context= {}
    html=template.render(context)
    result= io.StringIO(template)
    pdf=pisa.pisaDocument(io.StringIO(html.encode("ISO-8859-1 ")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    else:
        return HttpResponse('Errors')