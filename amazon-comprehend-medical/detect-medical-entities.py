import boto3
REGION = 'us-west-2'


def get_medical_entities(text):
    """
    ref: https://docs.aws.amazon.com/ja_jp/comprehend/latest/dg/get-started-api-med.html
    :param text:
    :type text: str
    :return:
    """
    client = boto3.client(service_name='comprehendmedical', region_name=REGION)
    result = client.detect_entities(Text=text)
    entities = result['Entities']
    return entities


if __name__ == '__main__':
    entities = get_medical_entities('cerealx 84 mg daily')
    for entity in entities:
        print('Entity', entity)
