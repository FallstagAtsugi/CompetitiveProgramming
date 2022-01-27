from operator import index
import sys
import pandas as pd
csv_input = pd.read_csv(
    filepath_or_buffer="C:\\Users\\kakiz\\OneDrive\\デスクトップ\\python_lesson\\TEST_STOCK.csv", encoding="utf-8", sep=",")

# 降順ソート rank付与
df = csv_input.sort_values('始値', ascending=False)
df['rank'] = df['始値'].rank(
    ascending=False).round().astype(int)
df.set_index('rank').sort_index()  # rankの付与成功
print(df)

# 指定したカラムだけ抽出したDataFrameオブジェクトを返却します。
print(df[["rank", "始値", "銘柄名"]].to_csv(sys.stdout, index=False))

print('上位3')
print(df.sort_values('始値', ascending=False).head(3).to_string(header=False))
print('下位3')
print(df.sort_values('始値', ascending=False).tail(3).to_string(header=False))
