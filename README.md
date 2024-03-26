# Afro Giftshop
[Afro Giftshop](https://afro-giftshop-4485fce00cde.herokuapp.com/) is a project created in order for small tourism businesses to easily keep track of their Giftshop sales, day batch and inventory. It will allow them to keep track of souvenirs sold as well as update them.
It is customisable and editable to allow the user to change their shop batch and inventory items through multiple options.

View the live site [here](https://afro-giftshop-4485fce00cde.herokuapp.com/)

![Mockup](docs/test/Responsiveness.png)

# User Experience/User Interface (UX/UI)  

## User Goals
Afro Giftshop is designed like a 'digital notebook', interactive, safe way for tourism agency to keep track of their mini shop data. 
The data will be viewable via the CLI (Command Line Interface) but stored in a connected, secure, Google worksheet which is not directly accessible to the user. 
Some key user goals for this project have been:

* It must be easy to navigate, with clear Menu options.
* An attractive, bright user interface to engage the user.
* Clear instructions are made available for correct data input.
* The option to clear data if needed.
* Data must be completely editable.


## User Stories 

* As a User, I would like to be able to easily find the various menus so that I can view information or add / edit records.
* As a User, I would like to be able to edit / remove data as neccessary.
* As a User, I would like to be able to view and manage sales so that I can add and find out daily sales with ease.
* As a User, I would like to be able to view daily batch of souvenirs, add, edit / remove data so I can see which souvenirs our customers prefer.
* As a User, I would like to be able to view stor inventory, add, edit / remove data so I can see which items needs to be ordered.
* As a User, I would like to be able to return to the main menu without having to restart the application.

## Structure

### Features

Implementation

* Mian Menu

![Main Menu](docs/features/Welcome.png)

* Sales Menu

![Sales Menu](docs/features/SalesMenu.png)

![Sales Data](docs/features/Sales.png)

* Store Day Batch

![Store Day Batch](docs/features/BatchView0.png)

![Store Day Batch](docs/features/BatchView1.png)

* Store Inventory

![Store Inventory](docs/features/InventoryView.png)

![Store Inventory](docs/features/InventoryView1.png)

* Return to Menu Page

![Exit Menu](docs/features/Menu.png)


### Features Left to Implement

As a future enhancement, I would like to add some basic functionality to keep track of sales and when to restock the store. 
I would also like to implement reporting to the application that will allow users to know when to put in new orders for restock the inventory.

## Logical Flow

**Main Menu**

![Main Menu](docs/design/StartFlowchat.png)

**Sales Menu**

![Sales Menu](docs/design/SalesFlowchat.png)

**Shop Day Batch**

![Shop Day Batch](docs/design/BatchFlowchat.png)

**Shop Inventory**

![Shop Inventory](docs/design/BatchFlowchat.png)


## Database Design



## Technologies

* Python - Python code written is my own unless referenced in the source code or the below Credits section.
* [Lucidchart](https://www.lucidchart.com) - used to create the flowchart needed during project planning.
* [GitHub](https://github.com/) - used for hosting the program's source code.
* [Gitpod](https://www.gitpod.io/) - used as a workspace for developing the code and testing the program.
* Replit Desktop - used as a workspace for developing the code and testing the program.
* Git - used for version control.
* [Google Sheets](https://docs.google.com/spreadsheets/) - used for storing edited and saved user data.
* [Google Cloud Platform](https://cloud.google.com/) - used to provide the APIs for connecting the data sheets with the Python code.
* [Heroku](https://heroku.com/apps) - used for deploying the project.
* [PEP8 Validator](https://pep8ci.herokuapp.com/#) - used for validating the Python code.


## Libraries & Packages 
**gspread** - gspread was imported and used to add, remove and manipulate data in the connected Google Sheets worksheets.  

**google.oauth.service_account** - This library was used for the authentication needed to access the Google APIs for connecting the Service Account with the Credentials function. A `CREDS.json` file was generated from this with the details needed for the API to access my Google account which holds the Google Sheets worksheet containing the applications data. When deploying to Heroku, this information is then stored in the config var section to ensure the application will run.  

**time & sys** -the time & sys libraries were used for the text-typing effect for typePrint and typeInput statements to create a visual effect 0f the text appearing on screen in real time.  

**os** - os library was used to add the clearScreen() function to assist in creating a neater flow from Menu options by clearing the screen for the user's choice from the Menu to be displayed. 

**colorama** - colorama was imported to give the terminal text colour and style to create a bright and engaging UI and to provide some visual feedback when a user's input is validated.


## Testing

### Pep8 Validation

All python code was ran through pep8online.com validator and any warnings or errors were fixed. Code then validated successfully.

![Pep8](docs/test/Test.png)


### Bugs and Fixes


## Deployment

### Version Control

### Heroku Deployment

## Credits