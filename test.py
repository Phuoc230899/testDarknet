from pathlib import Path

imgpath = './data/images/'
final_paths = []
filetext = list(Path(imgpath).rglob('*.[png]*'))
names = [str(path.name).split('.')[0] for path in filetext]
for name in names:
	image_path = imgpath+name+'.png'
	final_paths.append(image_path)



for path in final_paths:
	a = path[2:]

	with open("train.txt",'a') as t:
		t.write(a+'\n')