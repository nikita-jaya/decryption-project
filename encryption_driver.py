from mapping_module import Mapping
from preprocess_module import load_data, \
    preprocess_data, save_data
import sys

# find random descryption map
map = Mapping()
for i in range(100):
    map.swap()
    map.permanent_swap()

# load in subset of reference text
string = load_data(sys.argv[1])
string = preprocess_data(string)

# encrypt text
encryption = map.encrypt(string)

# save into new file
save_data("encryptedPic.txt", encryption)
