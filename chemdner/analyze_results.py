import csv
import pandas as pd


def analyze_results(annotations_file_path, abstracts_file_path, predictions_file_path):
    """
    :param annotations_file_path:
    :type annotations_file_path: str
    :param abstracts_file_path:
    :type abstracts_file_path: str
    :param predictions_file_path:
    :type predictions_file_path: str
    :return:
    """
    predictions = pd.read_csv(predictions_file_path, delimiter='\t', names=['paper_id', 'offset', 'rank', 'score'])
    predictions['pred'] = [True] * len(predictions)
    annotations = pd.read_csv(annotations_file_path, delimiter='\t', names=['paper_id', 'offset'])
    annotations['ann'] = [True] * len(annotations)
    abstracts = pd.read_csv(abstracts_file_path, delimiter='\t', names=['paper_id', 'title', 'abstract'])

    pred_ann = pd.merge(predictions, annotations, how='outer')
    pred_ann = pred_ann.fillna(False)

    true_positive = pred_ann[(pred_ann['ann'] & pred_ann['pred'])]
    false_positive = pred_ann[(~pred_ann['ann'] & pred_ann['pred'])]
    false_negative = pred_ann[(pred_ann['ann'] & ~pred_ann['pred'])]

    print('true positive: {}'.format(len(true_positive)))
    print('false positive: {}'.format(len(false_positive)))
    print('false negative: {}'.format(len(false_negative)))
    print('-'*50)
    analyze_false_positive(false_positive, abstracts)
    analyze_false_negative(annotations, abstracts)
    return


def analyze_false_positive(false_positive, abstracts, sample_num=30):
    """
    print the most confident predictions in false negative
    :param false_positive:
    :type false_positive: list
    :param abstracts:
    :type abstracts: pd Dataframe
    :param sample_num:
    :type sample_num: int
    :return:
    """
    false_positive_sub = false_positive.sort_values('score', ascending=False)[:sample_num]
    paper_ids = false_positive_sub['paper_id']
    offsets = false_positive_sub['offset']

    entities = []
    for pid, offset in zip(paper_ids, offsets):
        doc_type, start, end = offset.split(':')
        if doc_type == 'T':
            doc_col_name = 'title'
        elif doc_type == 'A':
            doc_col_name = 'abstract'
        document = abstracts[abstracts['paper_id'] == pid][doc_col_name].iloc[0]
        entity = document[int(start):int(end)]
        entities.append(entity)
    entities = [e.lower() for e in entities]
    print(set(entities))
    print('-'*50)
    return


def analyze_false_negative(false_negative, abstracts, sample_num=30):
    """
    print samples of false negative
    :param false_negative:
    :type false_negative: list
    :param sample_num:
    :type sample_num: int
    :return:
    """
    false_negative_sub = false_negative[:sample_num]

    paper_ids = false_negative_sub['paper_id']
    offsets = false_negative_sub['offset']

    entities = []
    for pid, offset in zip(paper_ids, offsets):
        doc_type, start, end = offset.split(':')
        if doc_type == 'T':
            doc_col_name = 'title'
        elif doc_type == 'A':
            doc_col_name = 'abstract'
        document = abstracts[abstracts['paper_id'] == pid][doc_col_name].iloc[0]
        entity = document[int(start):int(end)]
        entities.append(entity)
    entities = [e.lower() for e in entities]
    print(set(entities))
    print('-'*50)
    return
    return


def get_abstract(abstracts, paper_id, doc_type):
    """
    :param abstracts:
    :type abstracts: list
    :param paper_id:
    :type paper_id: int
    :param doc_type:
    :type doc_type: str ('A' or 'T')
    :return:
    """
    if doc_type == 'T':
        document = abstracts[abstracts['paper_id'] == paper_id]['title'][0]
    elif doc_type == 'A':
        document = abstracts[abstracts['paper_id'] == paper_id]['abstract'][0]
    return document


if __name__ == '__main__':
    data_dir = '../data/chemdner/'
    annotations_file_path = data_dir + 'chemdner_corpus/cem_ann_test_13-09-13.txt'
    abstracts_file_path = data_dir + 'chemdner_corpus/evaluation.abstracts.txt'
    predictions_file_path = data_dir + 'predictions/chemdner_predictions_acm.txt'
    analyze_results(annotations_file_path, abstracts_file_path, predictions_file_path)