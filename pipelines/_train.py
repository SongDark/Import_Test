import sys, os
sys.path.append("..")
sys.path.extend([os.path.join(root, name) for root, dirs, _ in os.walk("../") for name in dirs])

from _config import NNConfig
from networks import CNN, LSTM, Encoder, Decoder

nnconfig = NNConfig()
nnconfig.show()

cnn = CNN("cnn_layer1")
lstm = LSTM("lstm_layer1")
cnn.show()
lstm.show()

encoder = Encoder(cnn)
decoder = Decoder(lstm)