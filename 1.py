def 1(input):
  import pandas as pd
  input = """1abc2
  pqr3stu8vwx
  a1b2c3d4e5f
  treb7uchet"""
  data = pd.Series(input.split('\n'))
  data = data.str.findall('(\d)')
  data = data.apply(lambda x: int(str(x[0] + x[-1])) if len(x) > 1 else int(x[0]))
  return(int(data.sum())
