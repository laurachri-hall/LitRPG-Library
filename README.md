# LitRPG Library
=======
<p align="center">
  <img src="documentation/screenshots/home.png">
</p>

## Introduction

LitRPG Library is a review websites specifically for books in the LitRPG and LitRPG adjacent genre. It has been developed ad part of the Code Insititutes 16 Week Fult-Stack Developer Bootcamp as my final project - demonstrating all I have learned so far. Essential criteria include use of Django, database manipulation and CRUD functionality. It is for educational purposes only (for right now).

View live site here : [LitRPG Library](https://litrpg-library-2e24401b712e.herokuapp.com/)  
  
For Admin access with relevant sign-in information: [LitRPG Admin](lhttps://litrpg-library-2e24401b712e.herokuapp.com/admin/)

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

At mentioned above the design aspect was more of a struggle than usual. I had no clear idea of what I wanted but did have a vague notion that the colour scheme should be on the darker side based on the covers of most LitRPG. Dark but vibrant. I eventually found some options in the [Figma | UI UX Community](https://www.facebook.com/groups/207220915184146) facebook group and narrowed it down to too options. When consulted, one colleague mentioned option one reminded them of Gryffindor, so option two it was. 


![colour palatte](documentation/screenshots/colours.png)  
*Dark blues and purple used for backgrounds, lighter purple for accents, off-white colour for text and the pinkish colour for highlights.

![colour blind tests](documentation/screenshots/colour_blind.png)
*The colour palatte was test in [Adobe Colour](https://color.adobe.com/create/color-wheel) for both colour blindness and contrast. It passed both tests.

![contrast](documentation/screenshots/contrast.png)

### Font

Using [Google Fonts](https://fonts.google.com/), I imported 'Alef', 'Raleway' and 'Cabin' to my CSS file. Alef I picked out when creating my logo and decided to carry over to headings in my website It's a clear sans-serif with a bit of character. Raleway is one of my go tos for clear and readable. I did still make use of letter spacing several times. I'm a big reader and clarity is important to me, so I can read faster! I imported Cabin as a second, no-fills option for headers but ended up not using it. 
  
# Project Planning  
 
## Strategy Plane

My goal was to build the beginnings of a book review and tracking app, with an intial focus on the review side. Users can add books to the site (this would hopefully be sourced by an API in future releases) and write reviews. I currently have it set up for one review per book with other users being able to add their own thoughts on a particular book through the comments. The beginnings of the tracking side of the site can be seen in the To Be Read List, to which users can add books they are interested in reading.


### Site Goals

- Create a welcoming environment for readers to share their thoughts on LitRPG books (and adjacent genres)
- Dark colour palatte inspired by book covers
- Coomon icons with some redesigns to fit the theme
- CRUD functionalities
- Responsive UX 
- Scalable idea, for addition of future features 

## Agile Methodologies - Project Management

LitRPG is my first proper project following Agile planning methods. As someone who finds the planning side of things tricky at the very beginning (it gets easier further in!), it was a useful experience to have. I used my [Github Projects Board](https://github.com/users/laurachri-hall/projects/6/views/1) to plan and document all of my work. It worked quite well, though I found the tasks section of the user stories difficult to fill in beforehand - not really understand what each user story might need to complete it. Consequently, these were often added after the fact as I reflected on what I had actually done to accomplish the feature. It definitely did help keep me within Scope.

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
| As a **new or current user**, I want to **sign in with Google** so that I can **easily access the full features of the website with ease**.| **COULD HAVE** |

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

## Scope Plane

The scope for the requirements for this project are quite narrow, but my idea for what the website could be was fairly large. This forced me to think about what essentials I needed to make it work. I looked at several APIs that I could possibly implement, including Google Books, but found when I searched for specific LitRPG books they weren't there. So, I knew I needed a form to add books instead of relying on the API. I wanted the users to write reviews, but not multiple reviews for the same book. The discussion and interaction about a book would come in the comments. Of course, it was important for users to have control over their own content and to be able to edit and delete it. The abilty to register/login/logout was essential for users to have that control. A simple To Be Read List was the final element I wanted to implement in this first round. 


Essential features of my project were:

- **User Authentication**
  - Registration, login, and logout functionality
  - User profile management

- **Book Management**
  - Custom form for adding LitRPG books
  - Ability to edit and delete book entries

- **Review System**
  - One review per book per user
  - Option to edit or delete own reviews

- **Interaction Features**
  - Comment section for each book
  - User control over their comments (edit/delete)

- **Personal Reading List**
  - Simple "To Be Read" list functionality

- **API Considerations**
  - Custom book addition form due to limited coverage in existing APIs like Google Books

## Structural Plane
This was one of the most difficult bits for me. I normally have a very clear image in my head about what I want a project to look like, but not this time! My inital plan was to stick with basic bootstrap components, build from there and not get too complicate. This had the advantage of being quick and adaptable in case I changed my mind when I was feeling less overwhelmed by the project. I mostly stock with font awesome icons for any basic icon needs. I created my logo on [Logo](logo.com) and other images, including the hero image, I created using [Canva](https://www.canva.com/). This being a book review website, I had the advantage of using book covers for additional visual interest. 

## Skeleton & Surface Planes

### Wireframes

The wireframes for LitRPG are fairly low fidelity, using stand in images and icons and were created in Figma [Figma](www.figma.com). I have kept loosly to the design but I did originally plan for the mobile navbar to be centered. I quickly went back to the bootstrap default after not liking the implemented look. 

**Mobile/Tablet view for:**  

- Homepage

<details open>
    <summary>Mobile/Tablet Home Page Wireframe</summary>  
    <img src="documentation/wireframes/wireframe_home.png">  
</details>


### Database Schema - Entity Relationship Diagram

![ERD Image](documentation/images/erd.png)  
*Database Schema (ERD) for LitRPG Library*

#### Entity Relationship Diagram (ERD) Overview for LitRPG Library

The Entity Relationship Diagram (ERD) for the **LitRPG Library** illustrates how various features interact with one another and how they connect to the PostgreSQL Database. This ERD image was generated by [Django Extensions](https://django-extensions.readthedocs.io/en/latest/index.html), specifically using [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html?highlight=graph). Utilizing Django's User Model and Django AllAuth for user authentication, the system generates a user_id upon registration with a username and email. This enables users to:

- Edit their profiles
- Create new articles
- Add comments and photos that display their usernames
- Create and manage their book entries

##### Google Sign-In Integration

In addition to standard email and password authentication, the **LitRPG Library** integrates Google Sign-In to enhance user convenience and security. By allowing users to authenticate using their Google accounts, the application simplifies the login process and reduces the need for users to remember additional credentials. This integration is achieved through Django AllAuth, which facilitates seamless connection with Google's OAuth 2.0 authentication system. Users can easily register or log in using their Google credentials, providing a streamlined experience while maintaining robust security measures.

##### Image Uploading with Cloudinary

For image uploads, the **LitRPG Library** utilizes Cloudinary, a cloud-based service that provides efficient management of images and other media files. This integration allows users to upload images seamlessly while ensuring optimal performance and storage management. Cloudinary handles image transformations, resizing, and delivery, enhancing the overall user experience when interacting with visual content.

##### Primary Models

The primary models in the **LitRPG Library** include:

1. **Profile Model**: Allows users to customize their profile information linked to their user accounts.
   
2. **Articles Model**: Facilitates the creation and management of articles related to LitRPG content.

3. **Comments Model**: Enables users to comment on articles, with each comment associated with both the user and the article.

4. **Booking Model**: Collects data about users and their book-related activities, allowing for management of reading lists and reviews.

5. **Gallery Model**: Manages photo uploads related to user activities within the library.

##### Security Measures

Security measures implemented in the **LitRPG Library** include:

- The use of Django AllAuth for secure user authentication.
- Defensive design practices such as input validation and error messages.
- Restricted access for unregistered users.
- Author-only functionality for editing or deleting content.
- Confirmation modals for actions such as deleting a review or comment, ensuring that users confirm their intent before any irreversible actions are taken.
- CSRF tokens in all forms to protect against cross-site request forgery.

The Admin Dashboard provides comprehensive management capabilities, allowing administrators to oversee user accounts and associated data effectively. The implementation of `on_delete=models.CASCADE` ensures that all related data is removed if a user account is deleted.

This ERD reflects a well-organized and security-focused design, catering to both user needs and administrative functionalities within the **LitRPG Library** platform.


# Features

## User View - Registered/Unregistered

Most of the readable content is available to an unregistered user. Posting, editing and deleting of reviews or comments is limited to registered users. Naturally, the navbar changes depending on the user's status. Additionally, on the home page some buttons and sections also change. 

| Feature   | Unregistered User | Registered, Logged-In User |
|-----------|-------------------|-----------------|
| Home Page | Visable - content changes          | Visable - content changes        |
| Review List  | Visible | Visable  |
| Review Detail | Review and comments visable - no interactions/ 'Add to TBR' button not visable| Visable and full feature interaction available depending on authorship|
| TBR List   | Not Visable | Visable and full feature interaction available |
| Gallery   | Visable but no option to 'Add Photo' | Visable and full feature interaction available |
| Visit Us  | Visable and map interaction available | Visible and map interaction available |
<!-- 



It was important to me from the beginning that FreeFido be accessible to an unregistered user, in some capacitites. I wanted the website to sell the product to a new user quickly by immediately inviting them into the community through the park's information, articles and gallery sections. The following is a breakdown of the site's accessibility for registered/unregistered users:




## CRUD Functionality

Users are able to Create, Read, Update and Delete their shared information on FreeFido. Some features make full CRUD functionality available, whilst others present the necessary options only. Here is my CRUD breakdown for FreeFido:

| Feature | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Profile | Created upon registration | Yes | Yes | Full Profile deletion is currently only available to Admin upon User Account deletion, the profile dashboard clears automatically if a user removes all of their articles or bookings |
| Articles | Yes | Yes | Yes | Yes |
| Bookings | Yes | Yes | Yes | Yes |
| Gallery | Yes | Yes | No - this feature felt unneccessary as it's intention is a 'quick-sharing' of a photo, a minimal amount of information is required and users are able to delete the image if they wish | Yes |

## Feature Showcase 
  
**Header/Navigation & Footer**

*For features showcase, screenshots of the features in use were taken on Laptop/iPad Pro/iPhone 12 Pro*

<details open>
    <summary>Header & Navigation - All Users (Profile Icon only visible to Registered, Logged-In Users)</summary>  
    <img src="documentation/final_views/nav.png">  
</details>

![Profile Icon](documentation/final_views/profileicon_nav.png)  
*Registered, Logged In view with Profile Icon*  
  
As mentioned in the [Structural Plane](#structural-plane) section above, the icon navigation bar allows the user to make their way around the FreeFido site. The icons have a small amount of animation when hovered/clicked on and to reinforce the icon meaning, have tooltips on hover/touch (on mobile) that display their intention.
  
The 'header.html' has been created as a separate template and using Jinja templating language, called into the 'base.html' using ```{% include 'includes/header.html' %}```. The templating format and file setup took a little while to get used to when putting it together at first but felt very powerful once I became acclimatised to it. 

<details open>
    <summary>Footer - Visible to all Users</summary>  
    <img src="documentation/final_views/footer.png">  
</details>

The FreeFido footer has been created with a 'wave' background in grey, to complement the whitespace. The social-media icons, from [Flaticon](https://www.flaticon.com), open in a new tab when clicked. Tooltips are again used for those who may not be familiar with the icons. FreeFido does not have any active social media currently so the Facebook link only brings the user to the Facebook sign up page. Twitter, LinkedIn and GitHub bring the user to my own personal accounts connected to the production of this project.

**Home Page**

<details open>
    <summary>Home Page - Visible to all Users</summary>  
    <img src="documentation/final_views/home.png">  
</details>

In the Home Page 'Hero' section, when a user is not registered they will see a 'Sign Up' button under the section text, which will bring them to the Sign Up page. When logged in, they will see 'Book Today!' which will bring them to the booking page.


**About Page**

<details>
    <summary>About Page - Visible to all Users</summary>  
    <img src="documentation/final_views/about.png">  
</details>  


The 'About' section of the Home Page contains three sections of information for the user, 'About', 'Safety', 'Benefits'. These sections display paragraphs and bulleted lists of information about the park and its positive values and benefits. Within each paragraph is a colour-coded word which acts as a link to bring the user to an important section of the website.

![Paragraph link](documentation/final_views/linkarea.png)  
*'visit' provides a link to the Visit Us page as the user reads through the park's information*

<hr>

**Registration/SignUp**

<details open>
    <summary>Sign Up Page</summary>  
    <img src="documentation/final_views/signup.png">  
</details>
  
Users are required to add their Email, Username and Password twice, to ensure the correct one is saved. If any field is not filled in appropriately then a display message is used to inform the user with how to procede to complete the form. The Sign up and Sign in pages are created with default templates available with the AllAuth package. These templates are combined with the power of Bootstraps Crispy Forms pack to give extra control over the forms' appearance.

**Sign In**

<details open>
    <summary>Sign In Page</summary>  
    <img src="documentation/final_views/login.png">  
</details>

On successful Sign In, the user is greeted with feedback through a message which confirms sign in. The 'open padlock' Log In icon now changes to a 'closed padlock' Log Out icon that the user can click to begin the Log Out process. A 'Forgot Password' page is also re-designed from the AllAuth templates but it's full functionality is not yet activated for this version.

![incorrect username/email warning](documentation/final_views/incorrect_sign_in.png)  
*User is given feedback if they submit incorrect details where one item is correct and the other is incorrect*  


![fill out field warning](documentation/final_views/fill_field_warning.png)  
*Django built in field warnings for incorrect/forgotten fields input*  


![Sign In message and Log In icon change](documentation/final_views/signin_message.png)  
*Sign In message and Log In icon change*


**Sign Out**

<details open>
    <summary>Sign Out Page</summary>  
    <img src="documentation/final_views/logout.png">  
</details>
  
A user may choose to return to the Home page and stay logged in or leave the site, logged out.

![sign out message](documentation/final_views/signed_out.png)  
*User is given feedback in message format to confirm sign out, Profile icon no longer visible in navigation bar - message disappears after 3 seconds or if user clicks 'x'*  

<hr>

**Profile**

<details open>
    <summary>Profile Page - Registered Users only</summary>  
    <img src="documentation/final_views/profile.png">  
</details>
  
The user profile is created upon registration and displays a placeholder image and 'Edit Profile' button to allow the user to personalise their view. With future releases this page will be accessible to other users and allow connection, currently it is only viewable to the user.
  
<details>
    <summary>Profile Page - Placeholder image for Profile</summary>  
    <img src="documentation/final_views/placeholder_profile.png">  
</details>
  
  
**Profile Edit**

<details>
    <summary>Edit Profile Modal</summary>  
    <img src="documentation/final_views/edit_profile.png">  
</details>

Modal appears over the Profile page and allows users to edit their Profile Picture, Display Name (Display Name will be required for the future features of leaving Feedback/Reviews, Adding Friends and Direct Messaging) and Bio. Using the RichTextField input field, user's have more control of the formatting of their text if they wish.

<hr>

**Articles**

<details open>
    <summary>Articles Page - Unregistered User View (mobile/tablet), Registered User View with 'Add Article' icon (desktop)</summary>  
    <img src="documentation/final_views/articles.png">  
</details>

<details>
    <summary>Read Article Page - Unregistered User View</summary>  
    <img src="documentation/final_views/art_unregview.png">  
</details>  
  
Unregistered Users have access to all articles available on FreeFido. When registered and logged in, they may access the 'Add Article' button, 'Like/Unlike' icon and leave a comment for Admin approval. Articles created are displayed on individual 'cards' which display in rows for larger screens and columns for portrait, mobile view.

![site pagination arrow for moving page every 6 articles](documentation/final_views/site_pag.png)  
*Site pagination kicks in to display 6 articles per page. Arrows at the base of the article section allow users to move forward and back*  


Unregistered Users are free to read the articles and comments left on FreeFido but they cannot 'Like/Comment' them until they have signed up and logged in.

![like/comment count under article](documentation/final_views/like_comment.png)  
*A Likes and Comments counter is visible under every article. Logged-In Users can interact by clicking the heart outline to like. 'Heart outline' icon is replaced by filled Heart icon*  


![zero likes icon](documentation/final_views/zerolikes.png)  
*Likes icon is represented by an outlined heart icon. When it receives a like from the logged-in user, it becomes a filled heart icon*  
  

<details open>
    <summary>Add a Comment - Registered User View</summary>  
    <img src="documentation/final_views/comments.png">  
</details>

A comment box is visible to logged-in users only. Their comment is submitted for review by the Admin, once approved, the comment appears on the website.

![comment awaiting approval message](documentation/final_views/approval_comment.png)  
*Comment is awaiting approval message displayed after comment submit*
  

<details>
    <summary>Delete Comment - Registered User View for Comment Author only</summary>  
    <img src="documentation/final_views/comm_del_icon.png">  
</details>

For the author of the comment, when logged in, a trash icon will appear to allow them to delete the comment if they wish. 


**Create Article**

<details open>
    <summary>Create Article Page - Registered, Logged In User View</summary>  
    <img src="documentation/final_views/add_article.png">  
</details>  
  
The user may create an article and include their own image or allow a placeholder image. Feedback is given to the user to guide them if they do not fill out the required sections appropriately. The Submit button saves the article for Admin approval. Once approved, the article will appear on the main page.  
  

<details>
    <summary>Placeholder image for Articles - credit: Pattern Monster with FreeFido purple</summary>  
    <img src="documentation/final_views/placeholder_img.png">  
</details>


![feedback that article is awaiting spproval by Admin](documentation/final_views/art_approve.png)  
*Admin approval is required for articles to keep FreeFido on topic. Feedback is provided to the user by message that the article is awaiting approval*


**Edit Article**

<details open>
    <summary>Edit Article Page - Registered, Logged In User View - Article Author View - Edit/Delete Icon</summary>  
    <img src="documentation/final_views/art_eddel_reg.png">  
</details>

<details>
    <summary>Edit Article Page - Only accessible to the Article Author</summary>  
    <img src="documentation/final_views/edit_article.png">  
</details>
  
If a user spots a typo, error or wants to add new information to their article, then they may edit the article and submit for immediate reposting. A certain amount of trust exists between Admin and the FreeFido community to hope that no inappropriate or off-topic content will be shared, which will result in an immediate deletion of the user's account by the Admin. These issues will be locked down in the future development of FreeFido to allow certain content/words to be flagged and removed by the Admin or not allow the form to be submitted in the first place. Community guidelines will also be developed.

<details>
    <summary>Edit Article Message</summary>  
    <img src="documentation/final_views/art_updated_msg.png">  
</details>


**Delete Article**

<details>
    <summary>Delete Article Page - Only accessible to the Article Author </summary>  
    <img src="documentation/final_views/delete_article.png">  
</details>

![delete article successful message](documentation/final_views/del_art_msg.png)  
*User is informed that their article has been deleted - message disappears after 3 seconds*


**Search Function**

<details open>
    <summary>Search Function - Visible on Article pages only</summary>  
    <img src="documentation/final_views/search.png">  
</details>  
  
A user may search for something particular using the 'Search' field, which only appears on article related pages. If the search yields no results then the user is informed and provided with a link back to the articles.

<details>
    <summary>Search Function No Articles Found - Visible on Article pages only</summary>  
    <img src="documentation/final_views/no_articles.png">  
</details>

<hr>

**Bookings**

<details open>
    <summary>Bookings Page - Registered, logged-in Users only</summary>  
    <img src="documentation/final_views/booking.png">  
</details>
  
The booking system that has been created for FreeFido is a basic booking system that 'gets the job done' for the starting business. The user may create, edit and delete their bookings, they are informed if a date/time is unavailable and they see a display message if their booking is saved. For future development, the UI of this booking system will improve to make unavailable times shaded-out/hidden and the user will receive confirmation emails for all bookings saved. Only 4 bookings may be held for each user and currently this includes past bookings, which the user must delete themselves. This is to remind the user of all bookings incase they may have forgotten and not attended their booked time slot, making it unavailable for someone else. In the future booking feature, the user will receive an email informing them that they have missed a booking, the booking will be flagged with a red text message on the dashboard and the user will be reminded that repeated no-shows for bookings will have their access to bookings revoked for a period of time.

<details>
    <summary>Bookings Page - Max Bookings Reached</summary>  
    <img src="documentation/final_views/maxbooking.png">  
</details>


**Booking Create**

<details open>
    <summary>Booking Create Page - Visible only to Logged-In Users</summary>  
    <img src="documentation/final_views/booking_c.png">  
</details>  
  
For creating a booking, the user is informed of the necessary fields to be filled in to secure the booking via feedback. The user may add a second dog if they wish, or leave this to another time. A dropdown selection of 'Breed Choices' is made available for quicker booking, with 'Other' included for mixed breeds. This information is important to the FreeFido staff member who maybe operating the gate for allowing entry. The dog's appearance will help them to identify and confirm the booking along with the human user information.
Date and time is selectable via a calendar widget for date and dropdown selection menu displaying the hour slots from 8am to 8pm. FreeFido is super kind and opens every single day of the year for it's community members.

![past booking warning](documentation/final_views/past_book.png)  
*Warning shown to Users if they choose a date in the past, can only save a booking with a valid date/time*  
 
  
![unavaialable date/time](documentation/final_views/unavailable_datetime.png)  
*If a date/time combo is unavailable then the user is informed via warning message - future version of the booking system will have shaded out portions for the unavailable dates/times to make it easier on the user*  


![booking saved message](documentation/final_views/booking_saved_msg.png)  
*User feedback is delivered by message once a booking has been submitted through creation or edit- message disappears after 3 seconds*


**Edit Booking**

<details>
    <summary>Edit Booking Page - Visible for Logged-In Users who have made a previous Booking</summary>  
    <img src="documentation/final_views/booking_e.png">  
</details>

**Delete Booking**

<details>
    <summary>Delete Booking Page - Visible for Logged-In Users who have made a previous Booking</summary>  
    <img src="documentation/final_views/booking_d.png">  
</details>
  
A user may delete thier booking or return to the booking page incase they clicked the delete icon in error.

![deleted booking message](documentation/final_views/booking_del_msg.png)  
*User feedback is delivered by message once a booking has been deleted - message dissappears after 3 seconds*

<hr>

**Gallery**

<details open>
    <summary>Gallery Page - Registered, Logged-In User View with 'Add Photo' icon, Unregistered User View without icon</summary>  
    <img src="documentation/final_views/gallery.png">  
</details>
  
The FreeFido Gallery page allows the user and Admin to quickly upload snapshots from the park's activities to create a continuous flow of updated images. An overlay on hover/touch on mobile shows the user brief information about the photograph. The carousel of images at the top of the page shows some highlighted photos. For future development this carousel will display a collection of randomly selected images from the bulk of images availabale and stored in the Cloudinary database.    

<details>
    <summary>Gallery Page - Unregistered User view with photo info on hover(Desktop)/touch (on Mobile)</summary>  
    <img src="documentation/final_views/gal_unreg_info.png">  
</details>

**Add Photo**

<details open>
    <summary>Add Photo Page - Registered Users only</summary>  
    <img src="documentation/final_views/add_photo.png">  
</details>
  
All fields are required for the Upload Image form to be submitted and saved correctly. Feedback prompts the user if they have neglected a field.

**Delete Photo**

<details open>
    <summary>Photo Delete - Registered User View - delete icon only visible over the photos uploaded by that logged-in user. </summary>  
    <img src="documentation/final_views/gal_reg_del.png">  
</details>

<details>
    <summary>Delete Photo Page</summary>  
    <img src="documentation/final_views/del_photo_modal.png">  
</details>
  
If a user no longer wants their image to appear, or if they have made a mistake, thay may delete their image. Admin approval is not needed for images to be posted and future development will include community posting guidelines and a form of AI software to check the image for any unwanted content.  
   
![delete photo user message, successful deletion](documentation/final_views/photo_del_msg.png)  
*User feedback is provided by message, informing user that the photo has been deleted successfully - message disappears after 3 seconds*

<hr>

**Visit Us**

<details>
    <summary>Visit Us Page</summary>  
    <img src="documentation/final_views/visit.png">  
</details>
  
This page offers the user business information including opening hours and address. An embedded interactive Google Map allows the user to see FreeFido's location without leaving the site. If they require driving directions to the park, they can click on the map's 'View larger map' link to go to Google Maps in a new browser tab.

For future development, this page will hold the 'Feedback' feature for registered users to leave a review of the park. 

<hr>

**403, 404, 500 Pages**

These templates were added to this project in order to give the user the functionality to return to the website by using the links in the navigation bar or the Back to Homepage button on the Error page.

![404 error page](documentation/final_views/404error.png)

- They are triggered when a user tries to access:
  - information that is not theirs - 403,
  - information that does not exist anymore - 404,
  - something has gone wrong with the server and cannot retrieve database - 500

**Admin Panel**

Through Django's built-in Administration Panel, the Admin has full access over the data submitted to the website by registered Users. To access the Admin panel the Admin user adds '/admin/' to the end of the URL to display [https://freefido.herokuapp.com/admin/](https://freefido.herokuapp.com/admin/). A username and password is requested. For FreeFido, Admin approval is needed for articles and comments to keep the site on topic and to prevent spamming. Registered, logged-in users' have instant access to make a booking and upload images.

![django admin panel view](documentation/final_views/dj_adminpanel.png)  
*Django Admin panel view for FreeFido Administrator - content selection menu on left hand side*  


Users articles and comments require approval by the Admin of FreeFido to keep the website content on topic. Admin can change the status of articles from 'Draft' to 'Published'.

<details>
    <summary>Dropdown menu allowing Admin to 'publish' a users article, 'Save' button must be clicked to confirm</summary>  
    <img src="documentation/final_views/draft_art.png">  
</details>  

  
<details>
    <summary>Dropdown menu allowing Admin to 'approve' a users comment, 'Go' must be clicked to confirm</summary>  
    <img src="documentation/final_views/comment_apprv.png">  
</details>
    

Admin can control users bookings via the Django Admin panel.  

<details>
    <summary>All bookings are made available to the Admin</summary>  
    <img src="documentation/final_views/djbooking.png">  
</details> -->


## Future Features

Future enhancements for the **LitRPG Library** will focus on improving user experience and functionality. Planned features include:

- **Enhanced Categorization**: Better categorization of subgenres to help users navigate the vast array of LitRPG books more easily.

- **Profile Page and/or Dashboard**: A place where the user can change/update their details, control their book tracking lists, see and edit/delete their reviews/comments.
  
- **Tagging System**: Allowing users to add tags to reviews, making it easier to find related content and themes.

- **Search Functionality**: Implementing a robust search function to help users quickly locate specific titles or authors.

- **Improved Tracking Systems**: Enabling users to add entire series to their reading lists, addressing the common issue in LitRPG of having large series that can be cumbersome to add book by book.

- **API Integration**: Linking to a book API while still allowing users to add books that aren’t found in the database, ensuring a comprehensive collection.

# Technologies & Languages Used

- HTML
- CSS
- JavaScript
- Python
- [Git](https://git-scm.com/) used for version control.
- [Github](https://www.github.com) used for online storage of codebase and Projects tool.
- [GitPod](https://codeinstitute-ide.net/workspaces) as the IDE Code Institute recommeneds we use.
- [Figma](https://www.figma.com) for project design planning and wireframe creation.
- [Adobe Color](https://color.adobe.com) for colour theme creation and accessibility checkers.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
- [Cloudinary](https://cloudinary.com/) was used for cloud media storage of user uploaded images.
- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) create and host the database.
- [Heroku](https://www.heroku.com) was used to host the LitRPG Library application.
- [WAVE](https://wave.webaim.org/) to evaluate the accessibility of the site.
- [Canva](https://canva.com/) for image creation and editing.
- [Adobe Firefly](https://firefly.adobe.com/) for AI image generating.


## Libraries & Frameworks

- cloudinary==1.41.0
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- Django==4.2.16
- django-allauth==0.57.2
- django-crispy-forms==2.3
- django-erd==1.0
- django-extensions==3.2.3
- django-star-ratings==0.9.2
- django-summernote==0.8.20.0
- google-api-core==2.23.0
- gunicorn==20.1.0
- psycopg==3.2.3
- whitenoise==5.3.0
  
Further information is available in the [requirements.txt file](requirements.txt)

## Tools & Programs


- [Miro](https://www.miro.com) for inital basic ERD (entity relationship diagram) creation.
- [Perplexity AI](https://www.perplexity.ai/) for breaking down Python concepts and Django documentation into more understandable chunks, helping problem solve coding issues and generating most of the website text.
- [Chat GPT](https://chatgpt.com/) As above.
- [Favicon](https://favicon.io/) for converting an icon into favicon.
- [Logo](https://www.logo.com/) for logo design.

# Testing

- For all testing, please refer to the [TESTING.md](TESTING.md) file.


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
