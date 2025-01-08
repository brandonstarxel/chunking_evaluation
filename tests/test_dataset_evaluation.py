import pytest
import pandas as pd

from chunking_evaluation.evaluation_framework.dataset_evaluation import DatasetEvaluation, Dataset

QUESTIONS_DF_PATH = './chunking_evaluation/evaluation_framework/general_evaluation_data/questions_df.csv'


def test_does_not_accept_empty_list():
    with pytest.raises(ValueError, match='The `datasets` list argument is empty'):
        DatasetEvaluation(datasets=[])


def test_accepts_only_dataset_enum_values():
    with pytest.raises(TypeError, match='The `datasets` parameter must be a list of Dataset enum instance'):
        DatasetEvaluation(
            datasets=['chatlogs', 'finance']
        )


def test_maps_enum_values_to_datasets():
    dataset_eval = DatasetEvaluation(
        datasets=[
            Dataset.FINANCE,
            Dataset.CHATLOGS
        ]
    )

    assert dataset_eval._datasets == {'finance', 'chatlogs'}


def test_ignores_duplicate_dataset_names():
    dataset_eval = DatasetEvaluation(
        datasets=[
            Dataset.FINANCE,
            Dataset.FINANCE,
            Dataset.FINANCE,
            Dataset.CHATLOGS,
            Dataset.CHATLOGS,
        ]
    )

    assert len(dataset_eval._datasets) == 2
    assert dataset_eval._datasets == {'finance', 'chatlogs'}


def test_filters_corpus_list_based_on_datasets():
    dataset_eval = DatasetEvaluation(
        datasets=[Dataset.PUBMED, Dataset.WIKITEXTS]
    )

    assert sorted(dataset_eval.corpus_list) == sorted(['pubmed', 'wikitexts'])


def test_filters_questions_df_based_on_datasets():
    dataset_eval = DatasetEvaluation(
        datasets=[Dataset.STATE_OF_THE_UNION, Dataset.FINANCE]
    )

    questions_df = pd.read_csv(QUESTIONS_DF_PATH)
    filtered_df = questions_df[questions_df['corpus_id'].isin(['state_of_the_union', 'finance'])]

    assert len(filtered_df) == len(dataset_eval.questions_df)


def test_loads_all_questions_df_and_corresponding_corpus():
    dataset_eval = DatasetEvaluation(
        datasets=[Dataset.STATE_OF_THE_UNION, Dataset.FINANCE, Dataset.CHATLOGS, Dataset.PUBMED, Dataset.WIKITEXTS]
    )
    assert sorted(dataset_eval.corpus_list) == sorted(
        ['state_of_the_union', 'finance', 'chatlogs', 'pubmed', 'wikitexts'])

    questions_df = pd.read_csv(QUESTIONS_DF_PATH)
    assert len(questions_df) == len(dataset_eval.questions_df)
