# Use Python to call the netMHCIIpan program for prediction
import glob,os
import subprocess
from Bio import SeqIO
from Bio.Seq import  Seq
import shutil
def netMHCIIpan(protein_files_path,MHCII_Type_file):
    protein_files = glob.glob(os.path.join(protein_files_path, "*.txt"))
    for protein_file in protein_files: 
        protein_file_name=str(protein_file.split('.')[0])
        outfile_folder_path=os.path.join(protein_files_path,'{}'.format(protein_file_name))
        os.makedirs(outfile_folder_path,exist_ok=True) 
        with open(MHCII_Type_file,'r') as MHCII_HQ_Type_file:
            MHCII_HQ_Type =MHCII_HQ_Type_file.read()
            MHCII_HQ_Type_list=MHCII_HQ_Type.split(",")
            for i in MHCII_HQ_Type_list:
                i=str(i)
                subprocess.run(['netMHCIIpan','-f',protein_file,'-a', i ,'-xls','-xlsfile' ,protein_file_name+'_'+i+'.xls'])
                netMHCIIpan_outfile_path=os.path.join(os.getcwd(),protein_file_name+'_'+i+'.xls')
                shutil.move(netMHCIIpan_outfile_path,outfile_folder_path)
netMHCIIpan("protein_files_path","MHCII_Type_file")
