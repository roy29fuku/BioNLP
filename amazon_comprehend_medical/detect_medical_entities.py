import boto3
import os
from dotenv import load_dotenv

dotenv_path = '.env'
load_dotenv(dotenv_path)
AWS_ACCOUNT_KEY = os.environ.get('AWS_ACCOUNT_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')


def get_medical_entities(text):
    """
    ref: https://docs.aws.amazon.com/ja_jp/comprehend/latest/dg/get-started-api-med.html
    :param text:
    :type text: str
    :return:
    """
    client = boto3.client(service_name='comprehendmedical', aws_access_key_id=AWS_ACCOUNT_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    result = client.detect_entities(Text=text)
    entities = result['Entities']
    return entities


if __name__ == '__main__':
    text = 'Catechol-initiated cerealx 84 mg daily : multifunctional hydrophilic ligands for PEGylation and functionalization of metal oxide nanoparticles.'
    entities = get_medical_entities(text)
    for entity in entities:
        print('Entity', entity)
