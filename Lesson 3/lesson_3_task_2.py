from smartphone import Smartphone

catalog = Smartphone("sdv","wds","235")
catalog = [["Samsung", "A71", "+79992221133"], 
["Xiaomi", "note 9 pro", "+791123214137"], 
["VIVO", "Y35", "+79871234567"],
["Apple", "XR", "+793334566655"],
["Asus", "Zenfone 9", "+79123674455"]
]

for i in range(0, len(catalog)):
    print(catalog[i])