To create a web based application whilst making use of supporting the tools, methodologies and technologies that have been presented as the core learning material during the training with the functionality of randomisation distrubuted across several services with one main service and 3 side services all carrying out their own piece of functionality related to that of the main.

Solution
Having previously created a personal movie database application that would allow the user to keep track of the films that they had watched and rate them.
I decided that it would be a handy feature to add in the possibility of randomizing films within the database with the intent of recommending a random film to a friend or watching a random film. 

Original Requirements:

The home page should just give a brief description of what the app is and be the default navigation page.

The user should be able to navigate from/to any page in the website.

The web app should have a page to allow users to input/delete/update movie data that they have entered this includes Genre, Director and rating which can be either a number rating system or an A-F grading system.

New Feature Requirements:

To create a service that will randomise the genre from the database.

To create a service that will randomise the director from the database.

To create a service that will randomise the director from the database.

To create a service that will randomise the director from the database.

All services will act to their own devices in a docker container and interact with the database as well as the main service (the original app now contained within it's own docker container as well.)

The result will be displayed only within the main service whilst the other services are responsible for only carrying out it's own required functionality.

Project Log:

To keep track of my progress I created a Trello board so I was aware of the functions that I had completed and still had to complete.

Below you can see two screenshots of my Trello board, I wrote the functionality with the user in mind, this was doing in the form of a user story. I again scored each functional aspect based on the difficulty level based on my current skill set.

<img src="https://i.imgur.com/cxQnuBr.jpg" />
<img src="https://i.imgur.com/ZTMNvJj.png" />

Risk Assessment:

(Please click on the image to see it clearly)
<img src="https://i.imgur.com/h7xDO3n.png" />


The database remained unchanged so I have just included the ER diagrams from the previous iteration.
ER Diagrams can be seen below:

Initial Plan:
<img src="https://i.imgur.com/rIoSJV0.png" />


Delivered Solution: 
<img src="https://i.imgur.com/M8orczV.png" />

Here I have included a new diagram which shows the new architecture of the entire application now. This shows how each of the services work with one another.
<img src="https://i.imgur.com/NFrJZVn.png" />


Testing:
As the testing script was omitted due to complexities no automated testing was conducted. Throughout the development of the project and by making use of AGILE, the features were continuously testing manually either by myself or my colleagues.

Strengths:

•	Allows user to enter data to a database.
•	Allows users to delete data from a database.
•	Allows users to Update and view data from database.
•	Allows users to randomly have a movie presented to them.
•	Each service is containerised in a docker container so they can all communicate with eachother but are somewhat isolated as well.

Weaknesses:

•	It is pretty basic but at my current skill level it is perfect and it works this does not really qualify as a weakness. But encourages me to continue to improve.
•	Easy to get carried away with as I was extremely passionate about the creation of the app. You will be able to see this from the improvements I have in mind, listed below. Overall it satisfies the MVP.

Improvements:
•	Pull Movie Posters 
•	Allow the user to write a little review in a text box.
•	Allow users to include TV Shows/Games and Comics
•	Allow the user to send an aggregated list based on genre and personal rating via email.
•	Allow users to get ratings from online movie databases like IMDB and/or Rotten Tomatoes.
•	More complicated database so for example many genres for one movie as well as thinking of a way to included actor information and more.
•	Add a service for release dates instead, go by the year the film was created and query it by that rather than the director.


Summary:
It was something new and challenging for myself to create multiple services that all interacted with one another. Docker is something that is quite new to me as well as Ansible.


The Final Product was then deployed to Jenkins via the use of Ansible also automating Docker and any changes made to my GitHub was automatically carried over to the build on Jenkins:
(Please click on the image to see it clearly)
<img src="https://i.imgur.com/zEocnfy.png" />


