import datetime as dt
import pandas as pd

# 資料來源：政府資料開放平台(https://data.gov.tw/dataset/116285)
url = 'https://data.nhi.gov.tw/resource/mask/maskdata.csv'

# 第一步: 使用pandas從資料來源url的csv檔案載入數據、依照需要的欄位製作一個新的dataframe
data = pd.read_csv(url)
df = pd.DataFrame(data, columns=["醫事機構地址", "成人口罩剩餘數", "兒童口罩剩餘數"])

# 第二步： 新增一個"縣市"的欄位：將"醫事機構地址"這個欄位的資料，取前面三個字元即為所在縣市。
df["縣市"] = df["醫事機構地址"].str[0:3]

# 第三步： 依照縣市欄位中的資料做分類加總，新增一欄"口罩剩餘總數"並產生新的表格
mask_in_cities = df.groupby("縣市").sum()
mask_in_cities["口罩剩餘總數"] = mask_in_cities["成人口罩剩餘數"] + mask_in_cities["兒童口罩剩餘數"]
print(mask_in_cities)

# 第四步： 檔名加上檔案處理日期時間後存檔，加上編碼格式避免亂碼
time_stamp = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
mask_in_cities.to_csv(f"各縣市剩餘口罩數_{time_stamp}.csv", encoding="utf_8_sig")
