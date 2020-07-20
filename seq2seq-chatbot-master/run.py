import tensorflow as tf
import tensorlayer as tl
from tensorlayer.models.seq2seq import Seq2seq
import sys
from data.twitter import data

model_ = Seq2seq(
    decoder_seq_length = 20,
    cell_enc=tf.keras.layers.GRUCell,
    cell_dec=tf.keras.layers.GRUCell,
    n_layer=3,
    n_units=256,
    embedding_layer=tl.layers.Embedding(vocabulary_size=8004, embedding_size=1024),
    )
load_weights = tl.files.load_npz(name='model.npz')
tl.files.assign_weights(load_weights, model_)

def initial_setup(data_corpus):
    metadata, idx_q, idx_a = data.load_data(PATH='data/{}/'.format(data_corpus))
    (trainX, trainY), (testX, testY), (validX, validY) = data.split_dataset(idx_q, idx_a)
    trainX = tl.prepro.remove_pad_sequences(trainX.tolist())
    trainY = tl.prepro.remove_pad_sequences(trainY.tolist())
    testX = tl.prepro.remove_pad_sequences(testX.tolist())
    testY = tl.prepro.remove_pad_sequences(testY.tolist())
    validX = tl.prepro.remove_pad_sequences(validX.tolist())
    validY = tl.prepro.remove_pad_sequences(validY.tolist())
    return metadata, trainX, trainY, testX, testY, validX, validY


def inference(seed, top_n):
    model_.eval()
    seed_id = [word2idx.get(w, unk_id) for w in seed.split(" ")]
    sentence_id = model_(inputs=[[seed_id]], seq_length=20, start_token=start_id, top_n = top_n)
    sentence = []
    for w_id in sentence_id[0]:
        w = idx2word[w_id]
        if w == 'end_id':
            break
        sentence = sentence + [w]
    return sentence

data_corpus = "twitter"

#data preprocessing
metadata, trainX, trainY, testX, testY, validX, validY = initial_setup(data_corpus)

word2idx = metadata['w2idx']   # dict  word 2 index
unk_id = word2idx['unk']   # 1
start_id = 8002
idx2word = metadata['idx2w']
idx2word = idx2word + ['start_id', 'end_id']
top_n = 3

print("请输入 >")
sys.stdout.flush()
seed = sys.stdin.readline()




while seed:
    for i in range(top_n):
        sentence = inference(seed, top_n)
        print(" >", ' '.join(sentence))

    print("请输入 >")
    sys.stdout.flush()
    seed = sys.stdin.readline()