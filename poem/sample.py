# -*- coding: utf-8 -*-
# filename: sample.py

from __future__ import print_function
import numpy as np
import tensorflow as tf
import argparse
import time
import os
from six.moves import cPickle

from model import Model

from six import text_type


def say(keyword):
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--save_dir', type=str, default='save',
    #                    help='model directory to store checkpointed models')
    # parser.add_argument('--prime', type=str, default='',
    #                    help=u'输入指定文字生成藏头诗')
    # parser.add_argument('--sample', type=int, default=1,
    #                    help='0 to use max at each timestep, 1 to sample at each timestep')

    # args = parser.parse_args()
    # if keyword is not None:
    #     args.prime = keyword
    if keyword is not None:
        sample(keyword.decode("utf-8"))
    else:
        sample(u"")


def sample(keyword):
    with open(os.path.join(r"./rnn/config.pkl").encode('utf-8').strip(), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(r"./rnn/chars_vocab.pkl").encode('utf-8').strip(), 'rb') as f:
        chars, vocab = cPickle.load(f)
    model = Model(saved_args, True)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(r"./rnn")
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            print(model.sample(sess, chars, vocab, keyword, 1).encode('utf-8').strip())
            return model.sample(sess, chars, vocab, keyword, 1).encode('utf-8').strip()
            # args.prime


# decode('utf-8',errors='ignore')
if __name__ == '__main__':
    say(u"")
