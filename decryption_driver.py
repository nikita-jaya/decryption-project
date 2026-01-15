from mapping_module import Mapping
from scoring_module import score, get_reftext_log_freqs
from preprocess_module import load_data, \
    preprocess_data, save_data
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

# Load and process encrypted text
string = load_data(sys.argv[1])
string = preprocess_data(string)

# Load and process reference text
ref_text = load_data(sys.argv[2])
ref_text = preprocess_data(ref_text)
ref_text_pairs = get_reftext_log_freqs(ref_text)

# parameter p
p = float(sys.argv[3])

# initialize Mapping object
map = Mapping()

# initialize tracker objects
scores = []
max = 0
max_map = None
max_decrypt = None

# iterate 10000 runs for Metropolis algorithm
for i in range(10000):

    # Given the current decryption d,
    # randomly sample a candidate decryption
    map.swap()

    # Sample an independent Uniform
    U = np.random.uniform()

    # score for decryption d
    score_i = score(map, string, ref_text_pairs)

    # score for decryption d_prime
    score_prime = score(map, string, ref_text_pairs, new=True)

    # save new score
    scores.append(score_prime)

    # compute score ratio
    ratio = math.exp(score_prime - score_i)**p

    if U < ratio:
        # keep decryption d_prime
        map.permanent_swap()
    else:
        # reject decryption d_prime
        map.new = None

    # keep decryption if d_prime is new maximum
    if max < score_prime:
        max = score_prime
        max_map = map.save()
        max_decrypt = map.decrypt(string)

print(max_decrypt)
save_data("some_text_decrypted.txt", max_decrypt)

t = range(0, 10000)
plt.plot(t, scores, label='L', color='blue', linestyle='-')
plt.xlabel("t")
plt.ylabel("log(Score of descryption d')")
plt.title('log(Score) vs t')
plt.show()
