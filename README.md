## System Architecture Diagram

![Info](https://user-images.githubusercontent.com/20634568/120741664-49687900-c4aa-11eb-8e01-d82be4c16400.PNG)

# Question-Answering Model

The objective of this webapp is to display the correct answer to a question asked by a user, using a given context using pretrained models from [Hugging Face](https://huggingface.co/models?pipeline_tag=question-answering). The user can either enter the question and context manually, or choose to upload a csv file with the question, context and model name, and the answer will be displayed. In addition to answering a question, the user is also able to input their model of choice to answer their question, delete a model from the database, and view all available models. 

## Functionalities
- Add model 
  - Here the user needs to enter the model name and tokenizer from [Hugging Face](https://huggingface.co/models?pipeline_tag=question-answering) and give it a model name in the name text box. On clicking on add model, the model will be added to the database and can then be used to answer questions.
 
<img width="765" alt="Screen Shot 2021-06-03 at 6 31 54 PM" src="https://user-images.githubusercontent.com/20634568/120727673-fe416c80-c48f-11eb-832f-20eae58b2535.png">

- Delete Model
  - Here the user can simply enter the name of the model they wish to delete from the database and click on the delete button. All the models after deleting the model will then be displayed.
<img width="902" alt="Screen Shot 2021-06-03 at 8 21 06 PM" src="https://user-images.githubusercontent.com/20634568/120728320-7d837000-c491-11eb-8a88-d921d6d75b4e.png">


- Answer Question
  - Here the user can enter the question they need an answer to and the context required to answer it, in the respective text boxes, along with the model they want to use, and the answer will be displayed. The question, context and model are also displayed for reference.
 
<img width="785" alt="Screen Shot 2021-06-03 at 10 14 54 PM" src="https://user-images.githubusercontent.com/20634568/120735798-128d6580-c4a0-11eb-9f11-464d9176ad72.png">

- View Models
  - This functionality can be used to view all the existing models in the database. 
<img width="939" alt="Screen Shot 2021-06-03 at 8 27 08 PM" src="https://user-images.githubusercontent.com/20634568/120728231-55940c80-c491-11eb-913d-8f9f753f2242.png">

# Run the app using deployed link 
 - Use the following link to use the app without installing it locally : https://assignment3-7kfwjamufq-uc.a.run.app/
 
# Run the app locally
## Install dependencies
- streamlit - https://streamlit.io/
```
$ pip install streamlit
```
- docker - https://www.docker.com/

### Installing Docker on mac
 

•          Double-click Docker.dmg to open the installer, then drag the Docker icon to the Application folder.

 

•          Double-click Docker.app in the Application folder to start Docker.

 

•          Click the Docker menu to see Preferences and other options

 

•          Select About Docker to verify that you have the latest version

 

### Creating a Docker File


- Create a file called Docker File and edit it using vim. Please note that the name of the file has to be "Dockerfile" with "D" as capital.

- Build your Docker File using the following instructions.

```
FROM ubuntu

MAINTAINER demousr@gmail.com

RUN apt-get update

RUN apt-get install –y nginx

CMD [“echo”,”Image created”]
```
 

- Save the file


- The Docker file can be built by the following command


Syntax

docker build  -t ImageName:TagName dir


### Adding files to the Docker Container 

For copying the files from the host to the docker container :

1. First, set the path in your localhost to where the file is stored.
2. Next set the path in your docker container to where you want to store the file inside your docker container.
3. Then copy the file which you want to store in your docker container with the help of CP command.

ex: sudo docker cp /home/(name)/(folder_name)/(file_name)  (container_id):/(to_the_place_you_want_the_file_to_be)

 
 
