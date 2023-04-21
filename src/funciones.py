def nulitos(df):
    nul_col = df.isna().sum()
    print(nul_col[nul_col>0])


