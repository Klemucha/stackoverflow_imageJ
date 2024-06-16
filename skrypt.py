import os
from ij import IJ
from ij.IJ import run, setThreshold, setAutoThreshold
from ij.measure import ResultsTable as RT
import csv



folder = "C:/Users/Zuzan/OneDrive/Pulpit/Klementyna/IS_pADPR_RanBP2_100624/SCA7_1/P4"
def files_list(files):
	files_list = []
	for root, dirs, files in os.walk(files):
		for file in files:
			if "Ch11" in file:      #warunek na ch11 w nazwie
				file_path = os.path.join(root,file)   #full path of the file
				files_list.append((file_path,file))   #append a tuple of file path and file name to the list
	return files_list
list_of_files = files_list(folder)

verse1=['mean_int','mean_int_bg' ,'int_intensity','area']
with open(r'C:\Users\Zuzan\OneDrive\Pulpit\Klementyna\GitHub\stackoverflow_imageJ\data.csv','w') as f:
	writer=csv.writer(f, delimiter='\t')
	writer.writerow(verse1)

for n in list_of_files[:4]:
	print(n[0])
	im = IJ.open(n[0])
	run("Duplicate...", " ");
	img = IJ.openImage(n[0]);
	setAutoThreshold(img,"Otsu");
	run("Threshold...");
	run("Convert to Mask");
	run("Create Selection");
	run("Close")
	run("Close")
	run("Restore Selection");
	run("Measure");
	run("Make Inverse");
	run("Measure");
	rt = RT.getResultsTable()
	mean_intensity = rt.getValue("Mean",0) 
	mean_intensity_bg = rt.getValue("Mean",1) 
	int_intensity = rt.getValue("IntDen",0)
	Area = rt.getValue("Area",0)
	run("Close")
	run("Close")
	measurements=[mean_intensity,mean_intensity_bg ,int_intensity,Area ]
	''''with open(r'C:\Users\Zuzan\OneDrive\Pulpit\Klementyna\GitHub\stackoverflow_imageJ\data.csv','a') as f:
		writer=csv.writer(f, delimiter='\t')
		f.seek(0, 2)  # Przesuń kursor na koniec pliku
        if f.tell() > 0
        	f.write('\n')
		writer.writerow(measurements)
	
	#chcę to wszystko zapisać w pliku i najlepiej jeszcze nazwę pliku .csv .tsv (taby - /T?) i jeszcze zadbac zeby bylo wszystko od nowej linii (otworzyc plik, zapisac, zamknac plik) - zadanie domowe:)

'''