# Title -The Dino Database
This project will be an educational database aimed at children and teenagers with information about different dinosaur species. It will have information stored for them already and will encourage them to research additional information themselves, providing links to sources. The user will be able to add and store information that they find expanding the database.

# UX
* As a user I want to learn about dinosaurs.
* As a user I want to have an organised place to store what I am learning so that I can look at it again.
* As a user want to be able to update and delete the information I am inputting if there is new information to add to what I already have.

# Design Choices
* As this website is an educational tool aimed at children, I wanted it the appeal to them visually. I tried a few different fonts and colour schemes and felt that the final ones chosen offered the best visual experience. A slightly childlike, easy to read font ND a 'scary' colour scheme given the subject matter.
* I kept the layout simple and easy to follow, with instructions on how best to enter information into the database. I feel that the site is intuitive but still wanted to give extra instructions without overwhelming the user.

## Technologies Used 
* I used W3C to validate my HTML and CSS- https://jigsaw.w3.org/css-validator/ 
* I am using Materialize for layout and navbar- https://materializecss.com/
* I am using Heroku to deploy my project
* I am using MongoDb Atlas to store my database

## Testing
* Testing my links- In the navbar, both regular and mobile:'logo', 'home', 'database', 'more info'. ON all three pages: 'top_return' On index.html:  an additional 'database button that links to main_page.html. ON main_page.html: 'add', and 'edit'.  When clicked, each of these buttons sends the user to the correct URL.
* Testing my CRUD 'create'- Clicking on the #add_info_btn on main_page.html takes the user to add_info.html. This page shows the user the input categories. The user can then input the desired data into each - any category that does not have input (aside from the 'Time Period' currently which needs fixing) gets a 'please fill out this field' popup warning. Once the user has finished inputting their data and clicks 'Submit', the data is successfully sent to my mongo db. I have tested this several times and see the data both in my atlas mongo database and on the website itself as the user will see it.
* Testing my CRUD 'edit'- Clicking on the #edit_info_btn on main_page.html that is linking to each database entry takes the user to the same page setup as add_info.hmtl, except that the fields are already filled in(aside from the 'Time Period' currently which needs fixing). The user may then edit the desired information and hit the Edit button. The user will then be redirected to main_page.html and the information they wanted to edit will have been successfully altered.
* Testing my CRUD 'delete'- Clicking on the #delete_info_btn on main_page.html that is linking to each database entry will delete that particular entry from the database. As it is removed from the db, it will no longer be visible to the user.

## Deployment
### Remote Deployment
* This site was deployed using Heroku. Deployed site- https://dinodatabase.herokuapp.com/
* To do this I created a Heroku account and connected it to my GitHub account. I then enabled the 'automatic deploys' option and then 'Deploy Branch'. Heroku then generated the app and it is now accessible online through the above link. The branch deployed is my master branch.
## Issues
* I am aware of the linting errors in my html files in templates. All of these are extentions of 'base.html' and therefore do no need the boilerplate with DOCTYPE etc. 
* In app.py and env.py I had errors "'env' imported but unused" and "line too long (122 > 79 characters)" respectively. These are both linting errors and do not affect the project so I used the # noqa comment to disable the error warning.
## Credits
### Content
* Is utilised videos from the Code Institute course to help write my code, especially in app.py
* I used Materialize for my navbar, buttons and general structure. Code in main.js is pulled from Materialize.
* Fact Retriever was used to source some facts- https://www.factretriever.com/dinosaur-facts#:~:text=Some%20dinosaurs'%20tails%20were%20over,keep%20their%20balance%20when%20running.&text=Dinosaurs%20were%20reptiles%20that%20lived,about%2065%20million%20years%20ago.&text=The%20earliest%20named%20dinosaur%20found,(%E2%80%9Cdawn%20stealer%E2%80%9D).
### Media
* Skeleton2.jpg taken from https://blog.scienceborealis.ca/wp-content/uploads/sites/2/2019/11/TMP95.110.01_Skeleton2.jpg
* trex.jp taken from https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.rd.com%2Flist%2Fbest-dinosaur-museums%2F&psig=AOvVaw2uj_VPEDJ9lZNOWhePYKuW&ust=1597926422141000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLjUxfqhp-sCFQAAAAAdAAAAABAD
* steg.jpeg and titanosaruas.jpg taken from https://www.rd.com/list/best-dinosaur-museums/
### Acknowledgements
