import os

from .base_benchmark import BaseBenchmark

class GeneralBenchmark(BaseBenchmark):
    def __init__(self, chroma_db_path=None):
        self.general_benchmark_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'general_benchmark_data')
        questions_df_path = os.path.join(self.general_benchmark_path, 'questions_df.csv')

        corpora_folder_path = os.path.join(self.general_benchmark_path, 'corpora')
        corpora_filenames = [os.path.join(corpora_folder_path, f) for f in os.listdir(corpora_folder_path) if os.path.isfile(os.path.join(corpora_folder_path, f))]

        corpora_id_paths = {
            os.path.splitext(os.path.basename(f))[0]: f for f in corpora_filenames
        }

        super().__init__(questions_df_path, chroma_db_path=chroma_db_path, corpora_id_paths=corpora_id_paths)

        self.is_general = True
        