"""
Scoring of text using n-gram probabilities as log10 values
See http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
This code was imported, adapted to Python3 for use in this project from the original.
"""
from math import log10
from pathlib import Path
import zipfile
from src.helpers import strip_text

DATA_DIR = Path(__file__).parent / 'ngrams_data'


def _iter_over_ngram_data_file(ngram_filename: str):
    """
    Iterates over the contents of an n-gram data file. This function supports both plain text files
    and zipped text files. Each yielded line from the file is returned as a string. The function
    expects the filenames to end with either `.txt` or `.txt.zip`. If the file does not exist
    or has an incorrect file extension, an exception is raised.

    :param ngram_filename: Name of the n-gram file to iterate over. The file should be located
        in the predefined `DATA_DIR` directory.
    :type ngram_filename: str
    :return: A generator yielding lines from the n-gram data file as strings.
    :rtype: generator
    :raises ValueError: If the file does not exist in `DATA_DIR` or the filename has an
        unsupported extension.
    """
    data_file = DATA_DIR / ngram_filename
    if not data_file.exists():
        raise ValueError(f"ngram_filename {ngram_filename} does not exist in {DATA_DIR}")
    if ngram_filename.endswith('.txt'):
        with open(data_file, encoding='utf-8') as f:
            yield from f
    elif ngram_filename.endswith('.txt.zip'):
        with zipfile.ZipFile(data_file) as zip_file:
            # Get the name of the .txt file inside the zip
            txt_filename = ngram_filename[:-4]  # Remove .zip extension
            with zip_file.open(txt_filename) as f:
                # Need to decode bytes to string for zip files
                for line in f:
                    yield line.decode('utf-8')
    else:
        raise ValueError(f"ngram_filename must end in .txt or .txt.zip, but got {ngram_filename}")


class NgramScorer:
    """
    Build a ngram scorer from a datafile
    """
    def __init__(self, ngram_filename: str, sep: str = ' '):
        """
            load a file containing ngrams and counts, calculate log probabilities

            File contains lines of the form:
              n-gram  count
            where n-gram is an upper-case ngram and count the number of times that n-gram
            appears in the training data.

            The file is assumed to be in the ngrams_data directory (relative to this file).  If
            the file name ends in .txt, it is read as a text file.  If it ends in .txt.zip, it
            is treated as a zip file containing a single text file with the same name as the
            .zip file (minus the .zip extension).
        """
        self.ngrams = {}
        key = ''
        for line in _iter_over_ngram_data_file(ngram_filename):
            key, count = line.split(sep)
            self.ngrams[key] = int(count)
        self.ngram_len = len(key)
        self.num_of_training_ngrams = sum(self.ngrams.values())
        # calculate the log probabilities, logs are used to prevent underflow when scoring
        for key, value in self.ngrams.items():
            self.ngrams[key] = log10(float(value)/self.num_of_training_ngrams)
        # min score for unknown ngrams
        self.floor = log10(0.01 / self.num_of_training_ngrams)

    def score(self, text: str) -> float:
        """
            compute the score of some imput text
        """
        score = 0
        text = strip_text(text).upper()  # remove non-letters, fold to uppercase
        ngrams = self.ngrams.__getitem__  # cache the method lookup
        for i in range(len(text) - self.ngram_len + 1):
            # Check each ngram in text, add its value to the score
            ngram = text[i:i+self.ngram_len]
            if ngram in self.ngrams:
                score += ngrams(ngram)
            else:
                score += self.floor
        return score

    def get_stats(self) -> dict:
        """
        Returns statistics about the n-gram scorer
        """
        return {
            'num_of_training_ngrams': self.num_of_training_ngrams,
            'ngram_length': self.ngram_len,
            'floor_value': self.floor
        }

