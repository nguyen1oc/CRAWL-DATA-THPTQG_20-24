import pandas as pd

df = pd.read_csv("thpt_2020.csv", dtype={"SBD": str})

ma_tinh_dict = {
    "01": "Thành phố Hà Nội",
    "02": "Thành phố Hồ Chí Minh",
    "03": "Thành phố Hải Phòng",
    "04": "Thành phố Đà Nẵng",
    "05": "Tỉnh Hà Giang",
    "06": "Tỉnh Cao Bằng",
    "07": "Tỉnh Lai Châu",
    "08": "Tỉnh Lào Cai",
    "09": "Tỉnh Tuyên Quang",
    "10": "Tỉnh Lạng Sơn",
    "11": "Tỉnh Bắc Kạn",
    "12": "Tỉnh Thái Nguyên",
    "13": "Tỉnh Yên Bái",
    "14": "Tỉnh Sơn La",
    "15": "Tỉnh Phú Thọ",
    "16": "Tỉnh Vĩnh Phúc",
    "17": "Tỉnh Quảng Ninh",
    "18": "Tỉnh Bắc Giang",
    "19": "Tỉnh Bắc Ninh",
    "21": "Tỉnh Hải Dương",
    "22": "Tỉnh Hưng Yên",
    "23": "Tỉnh Hòa Bình",
    "24": "Tỉnh Hà Nam",
    "25": "Tỉnh Nam Định",
    "26": "Tỉnh Thái Bình",
    "27": "Tỉnh Ninh Bình",
    "28": "Tỉnh Thanh Hóa",
    "29": "Tỉnh Nghệ An",
    "30": "Tỉnh Hà Tĩnh",
    "31": "Tỉnh Quảng Bình",
    "32": "Tỉnh Quảng Trị",
    "33": "Tỉnh Thừa Thiên - Huế",
    "34": "Tỉnh Quảng Nam",
    "35": "Tỉnh Quảng Ngãi",
    "36": "Tỉnh Kon Tum",
    "37": "Tỉnh Bình Định",
    "38": "Tỉnh Gia Lai",
    "39": "Tỉnh Phú Yên",
    "40": "Tỉnh Đắk Lắk",
    "41": "Tỉnh Khánh Hòa",
    "42": "Tỉnh Lâm Đồng",
    "43": "Tỉnh Bình Phước",
    "44": "Tỉnh Bình Dương",
    "45": "Tỉnh Ninh Thuận",
    "46": "Tỉnh Tây Ninh",
    "47": "Tỉnh Bình Thuận",
    "48": "Tỉnh Đồng Nai",
    "49": "Tỉnh Long An",
    "50": "Tỉnh Đồng Tháp",
    "51": "Tỉnh An Giang",
    "52": "Tỉnh Bà Rịa - Vũng Tàu",
    "53": "Tỉnh Tiền Giang",
    "54": "Tỉnh Kiên Giang",
    "55": "Thành phố Cần Thơ",
    "56": "Tỉnh Bến Tre",
    "57": "Tỉnh Vĩnh Long",
    "58": "Tỉnh Trà Vinh",
    "59": "Tỉnh Sóc Trăng",
    "60": "Tỉnh Bạc Liêu",
    "61": "Tỉnh Cà Mau",
    "62": "Tỉnh Điện Biên",
    "63": "Tỉnh Đắk Nông",
    "64": "Tỉnh Hậu Giang"
}

def get_khu_vuc(sbd):
    ma = str(sbd)[:2]  
    return ma_tinh_dict.get(ma, "Không rõ")
    
df["khu_vuc"] = df["SBD"].apply(get_khu_vuc)

cols = df.columns.tolist()
cols.insert(1, cols.pop(cols.index('khu_vuc'))) 
df = df[cols]

df.to_csv("thpt2020_final.csv", index=False) 

print(df.head())
