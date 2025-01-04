from enum import Enum
from typing import override

from .general_evaluation import GeneralEvaluation


class Dataset(Enum):
    CHATLOGS = 'chatlogs'
    FINANCE = 'finance'
    PUBMED = 'pubmed'
    STATE_OF_THE_UNION = 'state_of_the_union'
    WIKITEXTS = 'wikitexts'


class DatasetEvaluation(GeneralEvaluation):

    def __init__(self, datasets: list[Dataset], chroma_db_path=None):
        # edge cases handling
        if len(datasets) == 0:
            raise ValueError('The `datasets` list argument is empty')

        for dataset in datasets:
            if not isinstance(dataset, Dataset):
                raise TypeError('The `datasets` parameter must be a list of Dataset enum instance')

        # maps enums to their values
        self._datasets: set[str] = set(map(lambda item: item.value, datasets))

        super().__init__(chroma_db_path=chroma_db_path)

    def _load_questions_df(self):
        """Filters the `corpus_list` and `questions_df` to include only the provided dataset values."""
        super()._load_questions_df()

        # filter questions
        filtered_questions = self.questions_df[self.questions_df['corpus_id'].isin(self._datasets)]
        self.questions_df = filtered_questions

        # filter corpus list
        filtered_corpus = list(filter(lambda item: item in self._datasets, self.corpus_list))
        self.corpus_list = filtered_corpus
