import boto3

ses = boto3.client('ses')

response = ses.create_template(
    
    Template = {
        'TemplateName' : 'TEMPLATE_NAME',
        'SubjectPart' : 'SUBJECT_LINE',
        'TextPart' : 'TEXT_CONTEXT',
        'HtmlPart' : 'HTML_CONTENT'
    }    
)