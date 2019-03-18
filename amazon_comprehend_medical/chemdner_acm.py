import sys
import csv
from tqdm import tqdm
from detect_medical_entities import get_medical_entities


def get_acm_annotations(abstracts_file_path, predictions_file_path):
    """
    :param abstracts_file_path: file path of CHEMDNER abstracts.txt
    :tyep abstracts_file_path: str
    :param predictions_file_path: output file path of predictions
    :tyep predictions_file_path: str
    :return: annotations
    """
    documents = []
    with open(abstracts_file_path) as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            # row = [paper_id, title, abstract]
            documents.append(row)

    predictions = []
    for doc in tqdm(documents):
        rank = 1  # The rank of the chemical entity returned for this document
        paper_id = doc[0]
        title = doc[1]
        abstract = doc[2]

        t_entities = get_medical_entities(title)
        a_entities = get_medical_entities(abstract)
        for i, entities in enumerate([t_entities, a_entities]):
            if i == 0:
                doc_type = 'T'
            else:
                doc_type = 'A'

            for entity in entities:
                if entity['Category'] != 'MEDICATION':
                    continue
                offset = ':'.join([doc_type, str(entity['BeginOffset']), str(entity['EndOffset'])])
                prediction = [paper_id, offset, rank, entity['Score']]
                predictions.append(prediction)
                rank += 1

    with open(predictions_file_path, 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(predictions)

    return


def check_length(abstracts_path, max_length=20000):
    """
    Amazon Comprehend Medical has length constraints.
    Maximum length of 20,000.
    https://docs.aws.amazon.com/ja_jp/comprehend/latest/dg/API_hera_DetectEntities.html

    :param abstracts_path: file path of CHEMDNER abstracts.txt
    :type abstracts_path: str
    :param max_length: maximum length of amazon comprehend medical
    :type max_length: int
    :return:
    """
    exceed_list = []
    with open(abstracts_path) as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            paper_id = row[0]
            title = row[1]
            abstract = row[2]
            if max(len(title), len(abstract)) > max_length:
                exceed_list.append(paper_id)

    if exceed_list:
        raise ValueError('Following papers exceeded maximum length.\n{}'.format(exceed_list))

    print('All abstracts satisfy condition.')
    return


def check_price(abstracts_path):
    """
    :param abstracts_path: file path of CHEMDNER abstracts.txt
    :type abstracts_path: str
    :return:
    """
    usd_per_unit = 0.01
    unit = 0
    with open(abstracts_path) as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            title = row[1]
            abstract = row[2]
            unit += - (-len(title)//100)  # round up
            unit += - (-len(abstract)//100)  # round up

    total_cost = unit * usd_per_unit
    print('It will cost {} USD.'.format(total_cost))
    print('continue process?')
    option = input('input y or n: ')

    if option != 'y':
        sys.exit('process ended')

    return


if __name__ == '__main__':
    input_dir = '../data/chemdner/chemdner_corpus/'
    abs_path = input_dir + 'evaluation.abstracts.txt'
    output_dir = '../data/chemdner/predictions/'
    pred_path = output_dir + 'chemdner_predictions_acm.txt'

    check_length(abs_path, max_length=20000)
    check_price(abs_path)
    get_acm_annotations(abs_path, pred_path)
