
# Convert the predicted peptide scores into scores for each amino acid position
def calculateScore(protein_file_path,netpan_result_file_path,peptide_nubmer):
    import pandas as pd
    import numpy as np
    import itertools
    from collections import Counter
    from pandas.core.indexes.base import Index
    import glob,os
    from Bio import SeqIO
    from Bio.Seq import  Seq
    netpan_result_files = glob.glob(os.path.join(netpan_result_file_path, "*.xlsx"))
    protein_files=glob.glob(os.path.join(protein_file_path, "*.txt"))
    for protein_file in protein_files:
        for protein_seq in SeqIO.parse(protein_file,"fasta"):
            all_protein_str=list(str(protein_seq.seq))
            data1=pd.DataFrame({'amino': pd.Series(all_protein_str)})
            for netpan_sig_file in netpan_result_files:
                def C_core(netpan_sig_file):
                    file_neirong=pd.read_excel(netpan_sig_file)
                    file_neirong=pd.DataFrame(file_neirong)
                    buchong_hang_nubmer=int(peptide_nubmer)
                    for i in range(buchong_hang_nubmer-1):
                        file_neirong.loc[len(file_neirong)]=[len(file_neirong),0] 
                    huachuang_result=file_neirong["NB"].rolling(peptide_nubmer,min_periods=1).sum()
                    data3=pd.DataFrame({netpan_sig_file:pd.Series(huachuang_result)})
                    data3=pd.concat([data1,data3],axis=1)
                    data3.to_excel(netpan_sig_file+'BSM_result.xlsx', float_format='%.5f') 
                C_core(netpan_sig_file)
               
calculateScore(protein_file_path="protein_file_path",netpan_result_file_path="netpan_result_file_path",peptide_nubmer="Number")

