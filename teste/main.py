#%%
import openpyxl
import pandas as pd

#%%
def read_xslx(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name='02.2024', header=2)
    return df


def get_columns(
    df: pd.DataFrame, col1: str, col2: str, col3: str, col4: str, col5: str
) -> pd.DataFrame:
    df = df[[col1, col2, col3, col4, col5]]
    return df


def drop_na(df: pd.DataFrame, col1: str) -> pd.DataFrame:
    df = df.dropna(subset=[col1])
    df[col1] = df[col1].replace('NaN', 0)
    df = df[df[col1] != col1].reset_index()
    return df


def split_col_name(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[['CIDADE', 'ESTADO']] = df[column].str.split('-', n=1, expand=True)
    df.drop(columns=[column], inplace=True)
    return df


#%%
path = 'C:/Users/JHS/Documents/repos/reading_10m_rows/teste/RED MEAT.xlsx'
df = read_xslx(path)
df = get_columns(df, 'DATA', 'ORIGEM', 'PESO', 'MACHOS', 'FEMEAS')
df = drop_na(df, 'DATA')
df = split_col_name(df, 'ORIGEM')
print(df)


# %%
