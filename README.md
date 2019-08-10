                                                ||JAY SHREE RAM||
# End_to_end_machine_learning_approach_for_crop_yeild_prediction





Table of contents:
                  1.Problem statement explanation
                  2. Dataset Explanation
                  3.Prerequesities for running the code
                  5.steps to be followed
                  
                  
                  
                  
1.Problem statement explanation:The problem statement is to create a local web server wherein by entering certain parameteres,you are able to predict the crop yeild for a particular crop.Here we have taken rice as a crop but various datasets of other crops with same features are available.First we have written a code in python 3.7 language and used multiple linear regression to predict the crop yeild. This we have done for 5 major rice producing districts of India. Then we have used flask and created pickle file and dumped them into our final server file


.
2. Dataset Explanation:The dataset conatins state and district name as the primary parameteres. The feature Y is the yeild that we had in the previous year.X1 is a label and is the  AREA OF YOUR FARM(In acres),X2 defines the PREVIOUS YEAR CROP YEILD YOU HAD,X3 is the PREVIOUS YEAR RAINFALL nad X4 is CURRENT YEAR EXPECTED RAINFALL. We have such data for 5 different districts of india.





3.Prerequesities for running the code: This code is written in python so you can use any platform where python is operable.But you need to amke sure that the libraries are preinstalled. Libraries prerequired are pandas,numpy,sklearn,matplotlib,sns,jason,Seaborns,pickle.
 
 
 
 
 
 
 
 4.steps to be followed:
                        1. Make sure that you have all the files in the same folder
                        2. First pre install all the required libraries and check if you have them
                        3. There are 5 csv files and 5 code files for those csv files
                        4. Change the location in the python code with respect to the csv file
                        6. As soon as you run your python code, a pickle file will be created in the same folder
                        7. repeat the steps for all the 5 files
                        8. After all the pickle files are created, simply run the server file.
                        Now your local server is created
                        9. On the top, where you see file location, double click and type cmd,a command promt will open
                        10.Type the following command to create server'python b_server.py'
                        click enter and a link will pop up to you
                        11. Copy that local server link and paste in any web browser
                        12.Following is the format to run the web page
                        'local server link/districtname?pC=(last year crop yeild)&area=your feild area&r1=last year rainfall&last to last year rainfall'
                        13. A web page with predicted crop yeild will be displayed
                        
HOPE THIS HELPS

                        
