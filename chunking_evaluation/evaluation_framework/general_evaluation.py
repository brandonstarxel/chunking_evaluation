from .base_evaluation import BaseEvaluation
from importlib import resources

class GeneralEvaluation(BaseEvaluation):
    def __init__(self, chroma_db_path=None):
        with resources.as_file(resources.files('chunking_evaluation.evaluation_framework') / 'general_evaluation_data') as general_benchmark_path:
            self.general_benchmark_path = general_benchmark_path
            questions_df_path = self.general_benchmark_path / 'questions_df.csv'

            corpora_folder_path = self.general_benchmark_path / 'corpora'
            corpora_filenames = [f for f in corpora_folder_path.iterdir() if f.is_file()]

            corpora_id_paths = {
                f.stem: str(f) for f in corpora_filenames
            }

            super().__init__(str(questions_df_path), chroma_db_path=chroma_db_path, corpora_id_paths=corpora_id_paths)

            self.is_general = True
