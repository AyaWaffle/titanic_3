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