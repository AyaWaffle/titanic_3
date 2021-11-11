from PIL import Image

def my_dtree(feature1, feature2):
    if feature1 == 'Gender':
        feature1 = 'Sex'
    if feature2 == 'Gender':
        feature2 = 'Sex'
    f_name = './tree_imgs_png/' + min(feature1, feature2)  + '_' + max(feature1, feature2) +  '.png'
    image = Image.open(f_name)
    
    return image

def my_pairplot():
    image = Image.open('./all_pairplot.png')
    
    return image

def how_to_check():
    image = Image.open('./HowToCheck.png')
    
    return image

# val_names = ["生存したか(Survived)", "乗客のクラス(Pclass)", "性別(Gender)", "年齢(Age)", "乗船していた兄弟、配偶者の人数(SibSp)",
# "乗船していた両親、子供の人数(Parch)", "運賃(Fare)", "乗船した港(Embarked)"]
def get_val(val_txt):
    if val_txt == "生存したか(Survived)":
        return "Survived"
    elif val_txt == "乗客のクラス(Pclass): 1が高級":
        return "Pclass"
    elif val_txt == "性別(Gender): 0が女性, 1が男性":
        return "Gender"
    elif val_txt == "年齢(Age)":
        return "Age"
    elif val_txt == "乗船していた兄弟、配偶者の人数(SibSp)":
        return "SibSp"
    elif val_txt == "乗船していた両親、子供の人数(Parch)":
        return "Parch"
    elif val_txt == "運賃(Fare)":
        return "Fare"
    elif val_txt == "乗船した港(Embarked): 0がCherbourg, 1がQueenstown, 2がSouthampton":
        return "Embarked"
    else:
        return val_txt
    