def nulitos(df):
    nul_col = df.isna().sum()
    print(nul_col[nul_col>0])


def modificar_nombre(nombre):
    if nombre.upper() in 'USA':
        return nombre
    elif 'UAE' in  nombre.upper():
        return 'UAE'
    elif nombre.endswith('?'):
        return nombre.title()[:-1]
    elif nombre is 'N/A':
        return 'N/A'
    else:
        return nombre.title()