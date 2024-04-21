import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import random 
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import json 
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import SGD

class Chatbot:
    def __init__(self, intents_file):
        self.intents_file = intents_file
        self.stemmer = LancasterStemmer()
        self.words = []
        self.labels = []
        self.training_data = []
        self.output_data = []
        self.model = None

    def load_intents(self):
        with open(self.intents_file) as file:
            data = json.load(file)
        return data

    def tokenize(self, sentence):
        return nltk.word_tokenize(sentence)

    def stem(self, word):
        return self.stemmer.stem(word.lower())

    def preprocess_data(self):
        data = self.load_intents()

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                tokens = self.tokenize(pattern)
                self.words.extend(tokens)
                self.training_data.append(tokens)
                self.output_data.append(intent["tag"])

                if intent["tag"] not in self.labels:
                    self.labels.append(intent["tag"])

        self.words = sorted(list(set([self.stem(word) for word in self.words if word != "?"])))
        self.labels = sorted(self.labels)

        out_empty = [0] * len(self.labels)

        for idx, doc in enumerate(self.training_data):
            bag = [0] * len(self.words)
            tokens = [self.stem(word) for word in doc]

            for word in self.words:
                if word in tokens:
                    bag[self.words.index(word)] = 1

            output_row = out_empty[:]
            output_row[self.labels.index(self.output_data[idx])] = 1

            self.X.append(bag)
            self.y.append(output_row)

        self.X = np.array(self.X)
        self.y = np.array(self.y)

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_shape=(len(self.X[0]),)),  
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(64, activation='relu'),  
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(len(self.y[0]), activation='softmax')
        ])

        sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

        model.compile(optimizer=sgd,
                      loss='categorical_crossentropy',
                      metrics=['accuracy']
                      )
        self.model = model

    def train_model(self):
        self.preprocess_data()
        self.build_model()
        self.model.fit(self.X, self.y, epochs=350, batch_size=5, verbose=1)

    def bag_of_words(self, s):
        bag = [0] * len(self.words)
        s_words = self.tokenize(s)
        s_words = [self.stem(word.lower()) for word in s_words]

        for se in s_words:
            if se in self.words:
                bag[self.words.index(se)] = 1

        return np.array(bag)

    def chat(self):
        print("Start Talking with the bot (type quit to stop)")
        while True:
            inp = input("You: ")
            if inp.lower() == "quit":
                break

            inp_bag_of_words = self.bag_of_words(inp)
            inp_bag_of_words = inp_bag_of_words.reshape(1, -1)

            results = self.model.predict(inp_bag_of_words)[0]
            results_index = np.argmax(results)
            tag = self.labels[results_index]

            if results[results_index] > 0.3:
                for tg in self.load_intents()["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                print(random.choice(responses))
                print("\n")
            else:
                print("I didn't get that, try again")

    def save_model(self, filename):
        self.model.save(filename)  
    