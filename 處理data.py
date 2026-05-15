import zipfile
import os

zip_path = r"C:\Users\user\Downloads\總統-各投票所得票明細及概況(Excel檔).zip"
output_path = r"C:\Users\user\Downloads\選舉結果2"

os.makedirs(output_path, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as z:
    for item in z.infolist():
        try:
            fixed_name = item.filename.encode('cp437').decode('big5')
        except:
            fixed_name = item.filename.encode('cp437').decode('gbk', errors='replace')
        
        print(f"解壓縮: {fixed_name}")
        
        dest = os.path.join(output_path, fixed_name)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        
        if not fixed_name.endswith('/'):
            with z.open(item) as src, open(dest, 'wb') as dst:
                dst.write(src.read())

print("完成！")