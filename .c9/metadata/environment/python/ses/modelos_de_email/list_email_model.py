{"filter":false,"title":"list_email_model.py","tooltip":"/python/ses/modelos_de_email/list_email_model.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":15},"action":"insert","lines":["import boto3","","# Create SES client","ses = boto3.client('ses')","","response = ses.list_templates(","  MaxItems=10",")","","print(response)"],"id":1}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":19},"action":"remove","lines":["# Create SES client"],"id":2}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":15},"end":{"row":9,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1708537841874,"hash":"ac16b1a992a4f3309268465016479642184b2260"}