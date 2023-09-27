def replace_missing_values(s, method):
    "Replace missing values"

    if method == 'NA':
        missing = s.isnull()
        s[missing] = 'NA'    

    return s