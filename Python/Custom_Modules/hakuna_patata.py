""" Custom Module for Custom Function/Classes

Developer: Patrick Weatherford
"""
import os as _os
import sqlite3 as _sqlite3
from fuzzywuzzy import fuzz as _fuzz, process as _process
import pandas as _pd
from pprint import pprint as _pprint
from io import StringIO as _StringIO
from contextlib import redirect_stdout as _redirect_stdout
import re as _re


def kaggle_api(username, api_key):
    """Creates a Kaggle API object which can download and search for datasets.

    Args:
        username (str): Kaggle username
        api_key (str): Kaggle API key

    Returns:
        Kaggle API object.
    """
    _os.environ['KAGGLE_USERNAME'] = username
    _os.environ['KAGGLE_KEY'] = api_key

    from kaggle.api.kaggle_api_extended import KaggleApi

    k_api = KaggleApi()
    k_api.authenticate()
    return k_api


def kaggle_dataset_info(kaggle_api, search_criteria):
    """Search for Kaggle datasets

    Args:
        kaggle_api (object): kaggle api object
        search_criteria (str): try dataset owner/dataset as string

    Returns:
        Prints matches found, if any.
    """

    search_match = kaggle_api.datasets_list(search=search_criteria)

    if search_match == []:
        print('Nothing found that meets search criteria!')
    else:
        n_matches = len(search_match)
        print( f"{n_matches} match{'es' if n_matches > 1 else ''} found!\n{'='*20}\n")
        _pprint(search_match)


def kaggle_dataset_download(kaggle_api, dataset, download_path=_os.getcwd(), unzip=False, rename=None, overwrite=True):
    """Download kaggle file(s) into zip file

    Args:
        kaggle_api (object): Kaggle API object.
        dataset (str): Try dataset owner/dataset in Kaggle URL.
        download_path (str, optional): Download directory. Defaults to current working dir
        unzip (bool, optional): Unzip file?. Defaults to False.
        rename (str, optional): New name for file. Defaults is to leave as-is.
        overwrite (bool, optional): If file exists, overwrite?
    """
    captured_output = _StringIO()

    with _redirect_stdout(captured_output):
        kaggle_api.dataset_download_files(dataset=dataset, path=download_path, force=overwrite, unzip=unzip, quiet=False)

    captured_string = captured_output.getvalue()

    re_search = r'(downloading )(.*)( to )(.*)'
    match = _re.search(re_search, captured_string, flags=_re.IGNORECASE)
    download_file_path = _os.path.join(download_path, match.group(2))

    if rename is None:
        print(f"Download successful! File path below:\n{download_file_path}")

    else:
        try:
            _, file_ext = _os.path.splitext(download_file_path)
            new_file_path = _os.path.join(download_path, f"{rename}{file_ext}")

            _os.rename(download_file_path, dst=new_file_path)
            print(f"Download and rename succesful! File path below:\n{new_file_path}")
        except Exception as e:
            print(f"Download successful but rename FAILED! File path below:\n{download_file_path}\n\nException: {e}")


def fuzzy_match_df(col1, col2, threshold=90, fuzz_type='token_sort_ratio'):
    """Create intermediate pandas DataFrame that fuzzy matches 2 arrays of strings.

    Args:
        col1 (array-like): All values are compared.
        col2 (array-like): If not matched to col1 then not retrieved.
        threshold (int, optional): Set minimum matching threshold ratio. Defaults to 90.
        fuzz_type (str, optional): fuzzywuzzy.fuzz matching type. Defaults to 'token_sort_ratio'.

    Returns:
        pandas.DataFrame: Returns a DataFrame from which you can join matched objects together on.
    """

    # get unique values from columns passed to function
    col1 = _pd.Series(col1).unique()
    col2 = _pd.Series(col2).unique()

    matches = []

    for c1 in col1:
        match = _process.extractOne(c1, col2, scorer=getattr(
            _fuzz, fuzz_type), score_cutoff=threshold)  # gets the best match above threshold
        if match is None:
            match_tuple = (c1, None)
        else:
            match_tuple = (c1, match[0])

        matches.append(match_tuple)
    return _pd.DataFrame(matches, columns=['COL1', 'COL2_MATCH'])


def sql_to_df(db_path, sql_txt):
    """Query SQLite database/table and return results into pandas DataFrame

    Args:
        db_path (string): SQLite DB path.
        sql_txt (string): SQL statement in string format.

    Returns:
        pandas.DataFrame
    """

    with _sqlite3.connect(db_path) as conn:
        df = _pd.read_sql_query(sql_txt, conn)
        return df
    conn.close()


def df_to_sqlite(df, db_path, table_name, index=False, if_exists='replace', chunksize=5000):
    """Create SQLite table from pandas DataFrame

    Args:
        df (pd.DataFrame): DataFrame to convert to SQLite table.
        db_path (string): SQLite database path to store table.
        table_name (string): Name for SQLite table.
        index (bool, optional): Index created as column?. Defaults to False.
        if_exists (str, optional): Handle method if exists. Defaults to 'replace'.
        chunksize (int, optional): Chunksize for reading into table. Defaults to 5000.
    """

    df.to_sql(name=table_name, con=f"sqlite:///{db_path}",
              index=index, if_exists=if_exists, chunksize=chunksize)


def sqlite_tables(db_path):
    """Show all custom tables in specified SQLite .db.

    Args:
        db_path (string): SQLite .db path.

    Returns:
        pandas.DataFrame
    """

    sql_txt = r"SELECT name AS TABLE_NAME FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    with _sqlite3.connect(db_path) as conn:
        df = _pd.read_sql_query(sql_txt, conn)
        return df
    conn.close()


def sqlite_drop_table(db_path, table_name):
    """Drop specified table in SQLite db.

    Args:
        db_path (string): SQlite .db path.
        table_name (string): Table name to drop.
    """

    sql_txt = f'DROP TABLE IF EXISTS {table_name}'
    with _sqlite3.connect(db_path) as conn:
        conn.execute(sql_txt)
    conn.close()
