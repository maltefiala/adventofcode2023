def puzzle(input):
    import pandas as pd
    input = input
    data = pd.Series(input.split('\n'))
    data = data.str.findall('(\d)')
    data = data.apply(lambda x:
        int(x[0] + x[-1]) if len(x) > 0 else int(0))
    return(data.sum())
