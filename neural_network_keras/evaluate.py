import tensorflow.keras as K
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers
from tensorflow.keras.models import model_from_json
import cv2
import numpy as np

def cv2Evaluation(model, classes, model_input_format=(64, 64)):
    capture = cv2.VideoCapture(0)

    frame_count = 0
    while(True):
        ret, frame = capture.read()
        frame = cv2.resize(frame, model_input_format)
        cv2.imshow('', frame)

        if cv2.waitKey(1) == 27:
            #break if ESC pressed
            break

        frame_count += 1
        if frame_count % 60 == 0:
            frame_count = 0
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = frame.astype(np.float32)
            frame = frame / 255.0
            frame = np.expand_dims(frame, axis = 0)
            pred = model.predict(frame)[0]
            print("cl : " , classes[np.argmax(pred)])
            print("rate : ", np.max(pred))

    capture.release()
    cv2.destroyAllWindows()



model_file = "./3_classes_train"
model_input_format = (128, 128)
classes = ["firewire", "prises", "RCA"]
# load json and create model
json_file = open(model_file + ".json", 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights(model_file + ".h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.Adam(),
              metrics=['acc'])

cv2Evaluation(loaded_model, classes, model_input_format)

#score = loaded_model.evaluate(X, Y, verbose=0)
#print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
