"""
Runs SAGE with a grid search over multiple parameters (just searching for good output)
Just constructs shell commands to do this
NOT COMPLETED
"""
from tqdm import tqdm


def main():
    # Define settings
    splits = ['identity', 'categories', 'power']
    vocab_sizes = [1500, 3000, 5000, 10000]
    num_keywords = 10
    
    #for vocab_size in tqdm(vocab_sizes, ncols=80):
    for vocab_size in vocab_sizes:
        for split in splits:
            files = os.path.join('/home/mamille3/hegemonic_hate/data', split, '*')
            etas, vect, x, X_base = runSage(files, None, vocab_size, 1.)
            outpath = 'output/{}_{}words_{}vocab.csv'.format(splits, num_keywords, vocab_size)
            with open(outpath, 'w') as f:
                with Capturing() as output:
                    pdb.set_trace()
                    printEtaCSV(etas, vect, x, X_base, num_keywords)


if __name__ == '__main__':
    main()
