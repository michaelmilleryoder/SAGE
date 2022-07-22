"""
Runs SAGE with a grid search over multiple parameters (just searching for good output)
"""

from runSage import runSage, printEtaCSV
from tqdm import tqdm
from StringIO import StringIO 
import sys
import pdb
import os
import csv
import sage


def writeEtaCSV(outpath, etas,vect,x,X_base,num_keywords=25):
    """ Same as printEtaCSV in runSage but prints to a path """
    with open(outpath, 'w') as f:
        writer = csv.DictWriter(f,fieldnames=['source',
                                                       'word',
                                                       'sage',
                                                       'base_count',
                                                       'base_rate',
                                                       'file_count',
                                                       'file_rate'],
                                delimiter='\t'
        )
        writer.writeheader()
        vocab = {i:j for j,i in vect.vocabulary_.iteritems()}
        for filename,eta in etas.iteritems():
            #printEtaCSV(fname+'-sage.csv',eta,vect,x[i],mu,num_keywords=args.num_keywords)
            #with open(filename,'w') as fout:
            for word in sage.topK(eta,vocab,num_keywords):
                idx = vect.vocabulary_[word]
                writer.writerow({'source':filename,
                                 'word':word,
                                 'sage':eta[idx],
                                 'file_count':x[filename][idx],
                                 'file_rate':x[filename][idx]/float(x[filename].sum()),
                                 'base_count':X_base[idx],
                                 'base_rate':X_base[idx]/float(X_base.sum())
                })


def main():
    # Define settings
    splits = ['identities', 'categories', 'power']
    vocab_sizes = [3000] # [1500, 3000, 5000, 10000]
    smoothing_rates = [10, 20, 50, 100]
    num_keywords = 10
    
    #for vocab_size in vocab_sizes:
    for vocab_size in tqdm(vocab_sizes, ncols=80):
        for smoothing_rate in tqdm(smoothing_rates, ncols=50):
            for split in splits:
                files = os.path.join('/home/mamille3/hegemonic_hate/data', split, '*')
                etas, vect, x, X_base = runSage(files, None, vocab_size, float(smoothing_rate))
                outpath = 'output/{}_{}words_{}vocab_{}smoothing.csv'.format(split, num_keywords, vocab_size, smoothing_rate)
                writeEtaCSV(outpath, etas, vect, x, X_base, num_keywords)


if __name__ == '__main__':
    main()
