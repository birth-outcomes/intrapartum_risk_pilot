def replace_missing_values(s, method):
    "Replace missing values"

    if method == 'NA':
        missing = s.isnull()
        s[missing] = 'NA'
    
    elif method == 'zero':
        missing = s.isnull()
        s[missing] = 0

    return s