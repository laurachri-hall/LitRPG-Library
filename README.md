# LitRPG Library
=======
<p align="center">
  <img src="documentation/screenshots/home.png">
</p>

## Introduction

LitRPG Library is a review websites specifically for books in the LitRPG and LitRPG adjacent genre. It has been developed ad part of the Code Insititutes 16 Week Fult-Stack Developer Bootcamp as my final project - demonstrating all I have learned so far. Essential criteria include use of Django, database manipulation and CRUD functionality. It is for educational purposes only (for right now).

View live site here : [LitRPG Library](https://litrpg-library-2e24401b712e.herokuapp.com/)  
  
For Admin access with relevant sign-in information: [LitRPG Admin](link goes here)

<hr>

## Table of Contents

- [LitRPG Library](#flitrpglibrary)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [User Registration](#user-registration)
    - [Book Reviews](#book-reviews)
    - [Comments](#comments)
    - [To Be Read List](#to-be-read-list)
    - [User Profile](#user-profile)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Feature Showcase](#feature-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Elephant SQL](#elephant-sql)
  - [Heroku deployment](#heroku-deployment)
  - [Clone project](#clone-project)
  - [Fork Project](#fork-project)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)

## Overview

LitRPG Library is a book review and ‘to be read’ book tracking app for all readers of the LitRPG and adjacent genres. Users are invited to:

- Join the LitRPG community
- Add a book they want to review
- Write and comment on book reviews
- Add books reviewed on the site to a ‘To Be Read’ list

LitRPG is accessible via all browsers with full responsiveness on different screen sizes. Its aim is to simplify the process of selecting books, foster a vibrant community centred around LitRPG and related genres and create a 'To Be Read' (TBR) wishlist. I have created this site to meet the needs of LitRPG readers. While, there are other book review and tracking sites out there most do no handle the different nuances of the LitRPG genre well. LitRPG aims to offer a more tailored experience for those who love Progression Fantasy, GameLit, Wuxia and LitRPG. In future developments of this this project, I hope to offer users an upgraded tracking system (select which books in a series to add to TBR or read list as the number of books in a LitRPG series can be quite large). A full list of all books added to the library and the ability to search the reviews and books. I'd also like to add the ability to move books to a read list from the tbr list and add categories and tags to help organise the books.



# UX - User Experience

## Design Inspiration

The design of my LitRPG review website evolved gradually as I navigated the learning curve of Django. Initially, I found myself overwhelmed by the framework's complexities, which left little room for creative expression. However, as I began to piece together the foundational elements of the site, I discovered more about my vision for the project and how it aligned with my growing capabilities.
Throughout this process, I drew inspiration from various sources, particularly book tracking websites like [hardcover.app](https://hardcover.app/). Their clean and intuitive interfaces highlighted the importance of user experience, motivating me to create a space where readers could easily navigate through reviews and track their reading progress.

### Colour Scheme

As mentioned above, the colour scheme and logo drove the design of the website. I wanted to create a 'fun' environment for the user to create the connection with the enjoyment that they would have with their dog at the park. The colours represent different sections/features of the website. I balanced the vibrant shades with a classic, ```#fff``` white background and an off-black shade of ```#0d0d0d```, as I felt that it yielded a slightly more matte effect that ```#000``` black. This combination also yielded a high contrast ratio of 19.44 for accessibility, with my colour scheme also passing a Colour Blind Safe check via [Adobe Color](https://color.adobe.com/create/color-wheel). This check was important for accessibility as the colours would form the base for my page and feature icons. Each colour in the scheme was also contrast checked with black ```#0d0d0d``` to ensure no contrast issue, all passed.

The corresponding sections and colours and identifying CSS variables are:

- Authentication: ```#AC44F2``` '--purple'
- Gallery: ```#3BD952``` '--green'
- User Profile: ```#F29F05``` '--orange'
- Visiting Information: ```#F25C5C``` '--coral'
- Booking: ```#4CE0C3``` '--blue'

For the Login/Logout icon, a grey ```#a6a6a6``` was used as a base colour. I felt this grey helped to balance the colours and prevent the icons from 'popping' too much for the eye in the navigation bar.

![balancing colours for website text,background and Login/Logout icon](documentation/final_views/safe_colours.png)  
*Black, white and grey used for backgrounds, text and Login/Logout icon*

![screenshot of colour scheme](documentation/final_views/color_small.png)  
*Colour Scheme for FreeFido website*

![colour blind safe colour swatch](documentation/final_views/color_blind_safe.png)  
*Accessibility check for colour scheme*

### Font

Using [Google Fonts](https://fonts.google.com/), I imported 'Outfit' and 'Montserrat' as a complementary font to my CSS file. Outfit is a playful, clear sans-serif which I felt worked well in designing my logo and for headers in my project. For future use, I envisoned merchandise bearing the logo for the FreeFido stall at the dog park. Montserrat was chosen as it gave more structure to the paragraph sections.

![outfit font design sheet](documentation/final_views/outfit.png)  
*Outfit, a Google Font designed by Rodrigo Fuenzalida*

In development, 'Outfit' was identified by variable ```--title```, whilst 'Montserrat' was set as ```--main-font``` within the CSS file. Similar to my setup for the project's colours, using variables helped to speed up the frontend process.
  
# Project Planning  
 
## Strategy Plane

The project goal was to build a simple booking app for a service. The 'product' was a one hour slot in a private, secure dog park and the 'users' were dog owners, trainers and walkers. As the service itself was uncomplicated, I aimed to create an easy, uncomplicated booking system for the user. Through planning and design prep work, I realised that there was an opportunity to treat this service like a 'brand' and develop the idea further. A social element was born from this with an idea for dog owners to be able to share advice and images of their furry friends on the website. This would hopefully help to create a happy group of park users who would recommend the park to others, share articles outside of the core group, and attract more users to sign up. Following common social-media design trends, I planned to use icons, high-quality, photographic images and an attractive, connected colour scheme.

### Site Goals

- Create a safe, happy environment for dog owners
- Use of playful colour to identify connected features of the website, plenty of white space to keep it fresh and to-the-point
- Commonly-used, identifiable icons with some redesigns to fit the theme
- Easy UI for quick fulfillment of feature CRUD functionalities
- UX remains the same whether on mobile, tablet or desktop
- Scalable idea, for addition of future features to easily grow the business
### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for LitRPG Library, identifying and labelling my:

- **Must Haves**: the 'required', critical components of the project. 
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release. 

## User Stories
User stories and features recorded and managed on [GitHub Projects](<https://github.com/users/laurachri-hall/projects/6/views/1>)

### User Registration
| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|    
| As a **new user**, I want to **register an account** so that I can **access the full features of the website**.| **MUST HAVE** |

### Book Reviews
| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|    
| As a **logged-in user**, I want to **post a review for a LitRPG book** so I can **share my opinion**.| **MUST HAVE** |
| As a **review author**, I want to **edit my posted reviews** so I can **update or correct information**.| **MUST HAVE** |
| As a **review author** I can **delete my reviews** so that **my content is no longer avaiable to view**.| **MUST HAVE** |
|As a **site user** I can **click on a post** so that **I can read the full text**.| **MUST HAVE** |
|As a **site user** I can **view a paginate list of posts** so that **I can select which post I want to view**.| **MUST HAVE** |
|As a **logged-in user** I can **like reviews** so that **I can show appreciation for helpful content and give feedback to the community**.| **SHOULD HAVE** |

### Comments
| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|    
| As a **logged-in user** I can **post comments on reviews** so that **I can engage in discussions**.| **MUST HAVE** |
| As a **comment author** I can **edit my comments** so that **I can update or correct information**.| **MUST HAVE** |
| As a **comment authors** I can **delete my comments** so that **they are no longer viewable**.| **MUST HAVE** |
|As a **logged-in user** I can **like comments** so that **I can show agreement or appreciation for a review**.| **SHOULD HAVE** |

### To Be Read List
| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|    
| As a **logged in user** I can **add books to my TBR list from book reviews** so that **I can keep track of which books interest me**.| **MUST HAVE** |
| As a **user with a TBR list** I can **remove books I've read or no longer interested in** so that **they no longer show on my TBR**.| **MUST HAVE** |
| As a **user** I can **move a book from my TBR list to a read list** so that **I can track books that I have read**.| **COULD HAVE** |

### User Profile
| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|    
| As a **logged-in user** I can **access my profile page** so that **I can view my activity, personal info, TBR and read lists**.| **COULD HAVE** |
| As a **logged-in user** I can **view and manage my posted reviews from my profile page** so that **I can easily edit and delete my reviews**.| **COULD HAVE** |
| As a **logged-in user** I can **view and mange my comments on reviews** so that **easily edit and delete them**.| **COULD HAVE** |

# Deployment
  
## Connecting to GitHub  

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the green 'open' button to generate a new workspace.

## Django Project Setup

1. Install Django and supporting libraries: 
   
- ``` pip3 install Django~=4.2.1 ```
- ``` pip3 install gunicorn~=20.1```
- ``` pip3 install dj-database-url~=0.5 psycopg```
- ``` pip3 install dj3-cloudinary-storage~=0.0.6```
- ```pip3 install urllib3~=1.26.15``` 
- ``` pip3 install django-summernote~=0.8.20.0```
  
2. As you are installing any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip3 freeze --local > requirements.txt``` command in the terminal.  
3. Create a new Django project in the terminal ```django-admin startproject config.```
4. Create a new app eg. ```python3 mangage.py startapp review```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'review',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python3 manage.py createsuperuser```
7. Migrate the changes with commands: ```python3 manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<PostgreSQL_URL_from_CI>"``` [CI Database Maker](https://dbs.ci-dbs.net/)
- ```os.environ["SECRET_KEY"]="insertYourOwnKeyHere"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:
- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn config.wsgi```
12. Make the necessary migrations again.

## Cloudinary API 

Cloudinary provides a cloud hosting solution for media storage. All users uploaded images in the LitRPG Library project are hosted here.

Set up a new account at [Cloudinary](https://cloudinary.com/) and add your Cloudinary API environment variable to your **env.py** and Heroku Config Vars.
In your project workspace: 

- Add Cloudinary libraries to INSTALLED_APPS in settings.py 
- In the order: 
```
 'django.contrib.staticfiles',
  'cloudinary_storage',
  'cloudinary',

```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Set Cloudinary as storage for media and static files in settings.py:
- ```STATIC_URL = '/static/'```
```
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌  
  MEDIA_URL = '/media/'  
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## CI DB Maker
1. Open the CI DB maker (https://dbs.ci-dbs.net/)
2. Input your email address and click ‘Submit’
3. Read the important notes- there’s a limit to the amount of concurrent databases you can create
4. Check your email for the new PostgreSQL database url. Copy it and follow the steps above.


## Heroku deployment

To start the deployment process, please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create new app**'.
3. Enter an app name and choose your region. Click '**Create App**'. 
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your: 
   
   - **CLOUDINARY_URL**: **cloudinary://....** 
   - **DATABASE_URL**:**postgres://...** 
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   -  **SECRET_KEY** and value  
  
5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['herokuappname', ‘localhost’, ‘8000 port url’].```
6. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9.  Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC**  may be removed from the Config Vars once you have saved and pushed an image within your project.
11. Double check that your dynos are on and configured correctly in **Overview**. If you need to change the type of dynos being used or turn them on go to **Resources**.
