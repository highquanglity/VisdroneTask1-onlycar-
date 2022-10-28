import os
path_label="C:/Users/Quang Nghiem/Desktop/VisDrone2019-DET-val/annotations"
path_image="C:/Users/Quang Nghiem/Desktop/VisDrone2019-DET-val/images"

name_of_delete_file=[]
files = os .listdir(path_label)

for file in files:
    full_path = os.path.join(path_label, file)
    file_name=file.split('.')[0]
    name_of_delete_file.append(file_name)
    with open(full_path, 'r') as f:
        lines=f.readlines()
    with open(full_path, 'w') as f:
        for line in lines:
            elements_of_line=line.split(',')
            if elements_of_line[5]=='4':
                f.write(line)
    if os.stat(full_path).st_size==0:
        name_of_delete_file.remove(file_name)
        os.remove(full_path)
    
    
images = os.listdir(path_image)
for image in images:
    full_path = os.path.join(path_image, image)
    image_name=image.split('.')[0]
    if image_name not in name_of_delete_file:
        os.remove(full_path)



