# flaskAPI
Flask API
To run this Program just Open your Pycharm OR any Other IDE open the terminal run the application sever and then go to local host through URL
#To use Get or view all the users in NoSQL format just add " /users " in the end of the URL of the Application it will show you all users in the database or in the file

#To use POST you can run a curl command initially for some of you curl command will not execute so first run the following curl command in the same directory" Remove-item alias:curl " then run " curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/users "

#To use PUT you can run a curl command but here you also have to mention the index of the Dataset for example use the following curl command in the same directory " curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/users/3 " here the 3 in the end of the command denotes 3rd indexed value element that is to be updated

#Same goes for DELETE  suppose we want to delete a particular user whose ID is 3 so use the following curl command in the same directory " curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/users/3 " here 3 at the end specifies user whose ID is 3 getting Deleted from System.
