data={"intents":[
    {"tag":"greeting",
     "patterns":["Hello","Hi There","Hi","What's up","Good morning","Good evening","Good afternoon"],
     "responses":["Howdy Partner! im jarvis what may i help you with","Hello im jarvis","Good morning im jarvis what may i help you with","Greetings!","Good evening im jarvis what may i help you with","Good afternoon im jarvis what may i help you with"]
        },
    {"tag":"age",
     "patterns":["how old are you","when is your birthday","when were you born"],
     "responses":["I am 24 years old","I was born in 1999","My birthday is March 14th  1999","14/03/1999"]
        },
    {"tag":"availablity doctor",
     "patterns":["Is there a doctor available","Is there a doctor"],
     "responses":["Yes there are doctor, which one do you need to book an appointment with?"]
        },
    {"tag":"availablity Ambulence",
     "patterns":["Is there a Ambulence available","Is Ambulence there"],
     "responses":["Yes Ambulence is available, should i book one for you?"]
        },
    {"tag":"availablity bed",
     "patterns":["Is there a bed available","Is bed there"],
     "responses":["Yes beds are available, should i book one for you?"]
        },
    {"tag":"availablity oxygen cylinder",
     "patterns":["Is there a oxygen cylinder available","Is oxygen cylinder there"],
     "responses":["Yes oxygen cylinder is available, should i book one for you?"]
        },
    {"tag":"book Doctor",
     "patterns":["Book me an appiontment with doctor Shreyas ","Book me a doctor"],
     "responses":["Apiontment booked with Dr.Shreyas, do you need assitance with something else?"]
        },
     {"tag":"book Ambulence",
     "patterns":["Book me Ambulence ","Book me a Ambulence"],
     "responses":["Ambulence is booked, do you need assitance with something else?"]
        },
     {"tag":"book Bed",
     "patterns":["Book me bed ","Reserve me a bed"],
     "responses":["Bed is reserved,, do you need assitance with something else?"]
        },
     {"tag":"book Oxygen cylinder",
     "patterns":["Book me Oxygen cylinder  ","Reserve me a Oxygen cylinder"],
     "responses":["Oxygen cylinder is reserved, do you need assitance with something else?"]
        },
    {"tag":"name",
     "patterns":["Whats your name?","name please?"],
     "responses":["My name is Jarvis, how may i help you?","Im Jarvis, how may i help you?"]
        },
     {"tag":"goodbye",
     "patterns":["bye","g2g","see ya","adios","cya"],
     "responses":["It was nice speaking to you","See you later","Speak Soon"]
        },
]}
import json
import string
import random

import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Dropout

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer=WordNetLemmatizer()# coverts into lema

words=[]
classes=[]
doc_x=[]
doc_y=[]

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens=nltk.word_tokenize(pattern)
        words.extend(tokens)# adds words/tokens in words list
        doc_x.append(pattern)
        doc_y.append(intent["tag"])
    if intent["tag"] not in classes:
        classes.append(intent["tag"])

words=[lemmatizer.lemmatize(word.lower()) for word in words if word not in string.punctuation]

words=sorted(set(words))
classes=sorted(set(classes))

training=[]
out_empty=[0]*len(classes)

# creating a bag of words model

for idx, doc in enumerate(doc_x): # iteration objects
    bow=[]
    text=lemmatizer.lemmatize(doc.lower())
    for word in words:
        bow.append(1) if word in text else bow.append(0)
    output_row=list(out_empty)
    output_row[classes.index(doc_y[idx])]=1

    training.append([bow, output_row])

random.shuffle(training)

training=np.array(training,dtype=object)

train_X=np.array(list(training[:,0]))
train_y=np.array(list(training[:,1]))

input_shape=(len(train_X[0]),)
output_shape=len(train_y[0])

epochs=500

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Create a Sequential model
model = Sequential()
model.add(Dense(128, input_shape=input_shape, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(output_shape, activation='softmax'))


adam = tf.keras.optimizers.Adam(learning_rate=0.01)


model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

print(model.summary())

model.fit(x=train_X, y=train_y, epochs=500, verbose=1)

def clean_text(text):
    tokens=nltk.word_tokenize(text)
    tokens=[lemmatizer.lemmatize(word) for word in tokens]
    return tokens

def bag_of_words(text,vocab):
    tokens=clean_text(text)
    bow=[0]*len(vocab)
    for w in tokens:
        for idx, word in enumerate(vocab):
            if word==w:
                bow[idx]=1
    return np.array(bow)

def pred_class(text, vocab, labels):
    bow = bag_of_words(text, vocab)
    result = model.predict(np.array([bow]))[0]
    max_prob_index = np.argmax(result)
    if result[max_prob_index] > 0.4:  # Adjust the threshold as needed
        return labels[max_prob_index]
    else:
        return None


def get_response(intents_list, intents_json):
    tag=intents_list[0]
    list_of_intents=intents_json["intents"]
    for i in list_of_intents:
        if i["tag"]==tag:
            result=random.choice(i["responses"])
            break
    return result

while True:
    message = input("")
    intents = pred_class(message, words, classes)
    if intents:
        result = get_response([intents], data)
        print(result)
    else:
        print("I'm sorry, I didn't understand that.")
