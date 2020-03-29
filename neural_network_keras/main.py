import tensorflow.keras as K
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers


nb_classes = 3
image_size = (128, 128)
drop_out = True

train_dir = "./Targets"
augmentated_data_path = "./augmentedData"
out = "./3_classes_train"
#validation_dir = "./dataset/save"
#Load pretrained vgg
print("Loading VGG")
vgg_conv = VGG16(weights='imagenet', include_top=False, input_shape=(image_size[0], image_size[1], 3))

# Freeze convs
for layer in vgg_conv.layers:#[:-4]:
    layer.trainable = False

for layer in vgg_conv.layers:
    print(layer, layer.trainable)

model = K.Sequential()
model.add(vgg_conv)
model.add(K.layers.Flatten())
model.add(K.layers.Dense(256, activation='relu'))
if drop_out:
    model.add(K.layers.Dropout(0.8))
model.add(K.layers.Dense(256, activation='relu'))
if drop_out:
    model.add(K.layers.Dropout(0.8))

model.add(K.layers.Dense(nb_classes, activation='softmax'))
model.summary()

#Load images

#PreprocessThem
train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=20,
      width_shift_range=0.2,
      height_shift_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')

#validation_datagen = ImageDataGenerator(rescale=1./255)

train_batchsize = 256
#val_batchsize = 10

train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=image_size,
        batch_size=train_batchsize,
        class_mode='categorical',
        save_to_dir = augmentated_data_path)
'''
validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=image_size,
        batch_size=val_batchsize,
        class_mode='categorical',
        shuffle=False)
'''

#Train

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.Adam(),
              metrics=['acc'])
# Train the model
history = model.fit(
      train_generator,
      steps_per_epoch=train_generator.samples/train_generator.batch_size ,
      epochs=50,
      verbose=1)

# serialize model to JSON
model_json = model.to_json()
with open(out + ".json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights(out + ".h5")
