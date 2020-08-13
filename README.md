#Title -TBC
This project will be an educational database aimed at children and teenagers with information about different dinosaur species. It will have information stored for them already and will encourage them to research additional information themselves, providing links to sources. The user will be able to add and store information that they find expanding the database.

#UX
*As a user I want to learn about dinosaurs.
*As a user I want to have an organised place to store what I am learning so that I can look at it again.
*As a user want to be able to update and delete the information I am inputting if there is new information to add   to what I already have.

##Technologies Used
* ~~I will likely use Bootstrap to assist with my page layout- https://getbootstrap.com/~~ 
* I will likely use hvr.css to add hover effects to elements on my page-https://ianlunn.github.io/Hover/
* I will likely use W3C to validate my HTML and CSS- https://jigsaw.w3.org/css-validator/ 
* I am using Materialize for layout and navbar- 
* I will likely use W3C to validate my HTML and CSS- https://jigsaw.w3.org/css-validator/ 


##Testing
* Testing my links- 'logo', 'home', 'database', 'more info', 'add', top_return' and 'edit' by clicking on them. All go to their correct url.
* Testing my CRUD 'create'- Clicking on the #add_info_btn on main_page.html takes the user to add_info.html. This page shows the user the input catagories. THe user can then input the desired data into each - any category that does not have input (aside from the 'Time Period' currently which needs fixing) gets a 'please fill out this field' popup warning. Once the user has finished inputting their data and clicks 'Submit', the data is successfully sent to my mongo db. I have tested this several times and see the data both in my atlas mongo database and on the website itself as the user will see it.
* Testing my CRUD 'edit'- Clicking on the #edit_info_btn on main_page.html that is linking to each database entry takes the user to the same page setup as add_info.hmtl, except that the fields are already filled in(aside from the 'Time Period' currently which needs fixing). The user may then edit the desired information and hit the Edit button. The user will then be redirected to main_page.html and the information they wanted to edit will have been successfully altered.
* Testing my CRUD 'delete'- Clicking on the #delete_info_btn on main_page.html that is linking to each database entry will delete that particular entry from the database. As it is removed from the db, it will no longer be visible to the user.
##Deployment
##Credits
###Content
* Is utilised videos from the Code Institure course to helpw write my code, especially in app.py
* I used Materialize for my navbar, buttons and general structure. Code in main.js is pulled from Materialize.
###Media
* background_img taken from https://blog.scienceborealis.ca/wp-content/uploads/sites/2/2019/11/TMP95.110.01_Skeleton2.jpg
###Acknowledgements
