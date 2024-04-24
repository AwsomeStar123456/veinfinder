# Veinfinder Project
This is the GitHub for the veinfinder project. Our project uses an IR emitter array with a NoIR Picam which has a IR pass filter on it. Using this we can see veins on peoples arms.

## Team Members
Donggi Lee | u1376432 | donggi2834@gmail.com <br />
Semrah Odobasic | u1293090 | semrahodobasic@icloud.com <br />
Logan Allen | u1190764 | Logan.Allen@utah.edu <br />
Jin Jeong   | u1375534 | djwls97865@gmail.com <br />

## Parts List
Raspberri Pi 2: https://www.raspberrypi.com/products/raspberry-pi-2-model-b/ <br />
NoIR PiCam 2: https://www.raspberrypi.com/products/pi-noir-camera-v2/ <br />
IR Emitter Array: https://www.ebay.com/itm/203067233072?chn=ps&norover=1&mkevt=1&mkrid=711-117182-37290-0&mkcid=2&mkscid=101&itemid=203067233072&targetid=2295557531990&device=c&mktype=pla&googleloc=9029771&poi=&campaignid=19851828444&mkgroupid=160536780385&rlsatarget=pla-2295557531990&abcId=9307249&merchantid=101644847&gad_source=1&gclid=Cj0KCQjwiYOxBhC5ARIsAIvdH51PvhkMOsm8p80wdNCZ_c5YhiLxNzNg80BskEwZZuzRu6qdxxyuCBwaApDhEALw_wcB <br />
Projector: https://www.amazon.com/KODAK-Luma-Pocket-Projector-Built/dp/B07RLXZ88F/ref=asc_df_B07RLXZ88F?tag=bngsmtphsnus-20&linkCode=df0&hvadid=80195746823025&hvnetw=s&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=&hvtargid=pla-4583795273963725&psc=1 <br />
IR Pass Filter: https://www.amazon.com/dp/B0981BX423?psc=1&ref=ppx_yo2ov_dt_b_product_details <br />
Voltage Regulator: https://a.co/d/2TbWu2m <br />
Beam Splitter: https://www.amazon.com/dp/B00MA5S2YE?ref_=cm_sw_r_cso_cp_apin_dp_VDXDWMDAAD2QBHMKNW0C&starsLeft=1 <br />

## Files
### Documentation
The Documentation folder contains the documentation of our project. This includes all of the various documents that we created over the semester. Included is also a wiring diagram. The diagram shows how the power delivery works and how all of the components are connected to eachother. There is also an SOP which discusses how the veinfinder should be used.

### Images
This folder includes all of the training images we have taken along with the augmentation code. The augmentation code is in C# which we run using Visual Studio. There is a folder for the original image set of 117 images from 12 people. There is another folder which contains all of the augmented images. This folder contains 2,808 images which are augmented from the original dataset. We have found that this can give us a very good model.

### ML Models
This folder contains all of the models which we have deemed as successful. This contains the images showing how each epoch changes the model. There is also a text document where we outline the training set as well as the learning late. The actual models are too large to be uploaded to GitHub so they can be found here: https://drive.google.com/drive/folders/1DGls1SB5syulKGr5hgQqLpTfuY4aNmA4?usp=sharing

## Notes
The SOP contains a lot of valuable information. Please read it. Make sure you understand the wiring diagram.