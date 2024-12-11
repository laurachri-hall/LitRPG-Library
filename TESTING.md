# Testing

This is the TESTING file for the [LitRPG Library](https://litrpg-library-2e24401b712e.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)

## Validation

### HTML Validation
Three pages had errors, as shown below. All errors were related to summer note or django forms.

<details open>
    <summary>Register - Errors</summary>  
    <img src="documentation/testing/register_htmlerrors.png">  
</details>
<br>
<details open>
    <summary>Add Review - Errors</summary>  
    <img src="documentation/testing/addreview_htmlerrors.png">  
</details>
<br>
<details open>
    <summary>Review Edit - Errors</summary>  
    <img src="documentation/testing/reviewedit_htmlerrors.png">  
</details>
<br>


| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- | 
| Index | 0 | 0 |
| Sign In | 0 | 0 |
| Register | 4 | 0 |
| SI w/ Google | 0 | 0 |
| Log out| 0 | 0 |
| Add Book | 0 | 0 |
| Add Review | 9 | 0 |
| Review Detail | 0 | 0 |
| Review List | 0 | 0 |
| Review Edit | 9 | 0 |
| tbr_list | 0 | 0 |
| TOS | 0 | 0 |
| PP| 0  | 0 |
  
<hr>  

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript code added to the project. External JS, for Bootstrap purposes, obtained via [CDN](https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/js/bootstrap.min.js) was not validated through JSHint.

| JS File | Screenshot | Errors | Warnings |
| ---- | ---------- | ------ | -------- |
| cover_preview.js | ![cover_previews.js](documentation/testing/image_preview.png) | none | none |
| edit_delete.js| ![js from edit_delete.js](documentation/testing/edit_delete.png) | none | none |
| likes.js| ![js from likes.js](documentation/testing/likes.png) | none | none |
| pause.js| ![js from pause.js](documentation/testing/pause.png) | none | none |
| summernote.js| ![js from summernote.js](documentation/testing/summernote.png) | none | none |


<hr>

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files that were created or edited by me. There were no issues, screenshots can be seen below.

| Feature | admin.py | forms.py | models.py | urls.py | views.py |
|---------|----------|----------|-----------|---------|----------|
| To Be Read | [no errors](documentation/testing/py/review_admin.png) | [no errors](documentation/testing/py/review_forms.png) | [no errors](documentation/testing/py/review_models.png) | [no errors](documentation/testing/py/review_urls.png) | [no errors](documentation/testing/py/review_views.png) |
| To Be Read | [no errors](documentation/testing/py/tbr_admin.png) | N/A | [no errors](documentation/testing/py/tbr_models.png) | [no errors](documentation/testing/py/tbr_urls.png) | [no errors](documentation/testing/py/tbr_views.png) |
| config | settings.py: [no errors](documentation/testing/py/config_settings.png) | N/A | N/A | [no errors](documentation/testing/py/config_urls.png) | N/A |


<hr>

### CSS Validation 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS file. External CSS was not tested. No issues.

![css validation](documentation/testing/css_validation.png)
  
<hr> 
   
### Lighthouse Scores
Testing was carried out in Lighthouse with the overall scores being fairly reasonable on desktop and quite a bit lower on mobile. I will consider image size and other possible ways to handle user uploaded images to limit size and format in the next version of LitRPG Library.

**Desktop**  

![Lighthouse scores desktop](documentation/testing/index_desk.png)  
*Desktop Home Page*  
  
![Lighthouse scores desktop](documentation/testing/reviewdetail_desktop.png)  
*Desktop Article Page*
  
**Mobile**  

![Lighthouse scores mobile](documentation/testing/index_mobile.png) 
*Mobile Home Page*  
  
![Lighthouse scores mobile](documentation/testing/reviewdetail_mobile.png) 
*Mobile Article Page*
  
<hr>  

### Wave Accessibility Evaluation

<!-- ![WAVE Web Accessibility Evaluation Tools](documentation/testing/wave_report.png)  
  
Accessibility was included in every planning stage for FreeFido, through the use of the WAVE report tool I could ensure that any necessary changes were made to make the website as accessible as it could be. A minor contrast issue with a word rendered in orange for the feature theme and the absence of text in article image cards, due to their design, was noted in the report. These will be considered in the next version of FreeFido to better it's score. -->
  
<hr>  

## Manual Testing

### User Input/Form Validation

<!-- Testing was carried out on desktop using a Chrome browser to ensure all forms take the intended input and process the input appropriately.

| Feature                    | Tested?  | User Input Required | User Feedback Provided     | Pass/Fail | Fix |
|----------------------------|----------|---------------------|----------------------------|-----------|-----|
| Navbar Logo and Icons | Yes | Click | Logo takes user to 'Home', icons take user to intended location. Tooltips used in desktop/mobile view to provide accessibility and further information about the icons purpose and intention | Pass | - |
| Home Page color text - 'visit', 'Join', 'articles' | Yes | Click | Users are informed of links purpose vis tooltip and link takes user to intended location | Pass | - |
| Sign Up Page               | Yes      | Email/Username/Password | Empty fields deliver prompt to user, email field demands '@' symbols, [username/password](documentation/testing/signup_input.png) too similar, password too short | Pass | - |
| Sign In | Yes | Username/Email and Password | Username/Email/Password must be exactly as registered originally in either lowercase/uppercase or mixture | Pass | - |
| Edit Profile (Registered User) | Yes | User may replace the placeholder image for Profile Image. All other fields are optional. | No feedback needed as placeholder profile picture is provided as default, user may change it they wish, other fields optional. | Pass | - |
| Search Field | Yes | Any input accepted | User will be presented with the results of their search, if their search input matches an article then they will receive the applicable articles, otherwise 'No article found' will display | Pass | - |
| Add Article (Registered User) | Yes | Mixture of required image/text fields | 'Please fill out this field' is displayed to user, article receives placeholder image if no image provided if RichTextField is left blank then user receives [this](documentation/testing/art_required.png) feedback | Pass | - |
| Comment Box (Registered User) | Yes | Text input accepted | User is informed that their comment is awaiting approval | Pass | - |
| Like/Unlike button (Registered User) | Yes | Click | Button changes from empty heart to full heart and number of likes changes | Pass | - |
| Edit Article (Registered, Author) | Yes | Image/Text fields | Changes made to Article are saved and displayed | Pass | - |
| Delete Article (Registered, Author) | Yes | Click button to choose 'Confirm' or 'Return to Articles' | Article is deleted or user returns to main article page | Pass | - |
| Delete Comment (Registered, Author) | Yes | Click button to choose 'Delete' or 'Return to Articles' | Comment is deleted or user returns to main article page | Pass | - |
| Create Booking (Registered User only) | Yes | Test input and selection from date/time widget/dropdown selection | User is prompted to 'Fill out this Field' for required fields, if date/time is unavailable they are informed by message to pick another date/time | Pass | - |
| Edit Booking (Registered User)| Yes | Text fields | User may make changes to be saved, prompted to 'Fill out this field' is anything is left blank,  if date/time is unavailable they are informed by message to pick another date/time | Pass | - |
| Delete Booking (Registered User) | Yes | Click button to choose 'Delete' or 'Return to Bookings' | Booking is deleted or user is returned to bookings page | Pass | - |
| Upload Image (Registered User) | Yes | Image/Text fields | User is prompted to fill out the required fields, user may exit the page using icons if they change their mind | Pass | - |
| Gallery Image | Yes | Hover/touch(on mobile) | User is presented with an overlay on the chosen image giving details on the image, photo uploader receives 'delete' icon when logged in | Pass | - |
| Delete Photo (Registered, Uploader) | Yes | Click to 'Cancel' or 'Delete' | Cancel hides the modal, delete removes image and returns user to gallery | Pass | - |
| Back to Top button - Gallery Page | Yes | Click | Button returns user to top when clicked | Pass | - |
| Sign Out (Registered User) | Yes | Click to choose 'It's time to go' or 'Return home' | User is signed out and informed by message on screen, return home button brings user back to home page, still logged in | Pass | - |
| Footer icons | Yes | Click | Icons take user to intended location via a new tab, tooltips provided inform user of icon purpose if they are not familiar with them | Pass | - | -->

### Browser Compatibility

<!-- Freefido was tested on the following browsers, new users were created, old users data edited and all features were tested:

- Chrome v114.0.5735.199
- Firefox v114.0.2
- Edge v114.0.1823.79
- Safari v16.5.1

| Browser | Issue | Functionality |
|---------|-------|---------------|
| FireFox | Profile Edit/Upload Image - File input 'Browse' Button centered in input field | Button works as expected |
| FireFox | Profile Dashboard - scrollbars following Mozilla styling | No issue |
| Safari  | Scrollbars following Safari styling | No issue | -->

<hr>

### Testing User Stories

<!-- User Stories are documented in the FreeFido [GitHub Projects Board](https://github.com/users/amylour/projects/4). User Stories are numbered, with Acceptance Criteria and Tasks detailed within. Testing was carried out on Dev Tools for desktop/tablet/mobile, by creating multiple accounts for test users: FidoTest1, FidoTest2, FidoTest3 etc and following through by ensuring that the Acceptance Criteria were met. All features were tested to ensure that they provided the user with the expected output and action.


| User Story                 | Acceptance Criteria Met?  | Tested | Response     | Pass/Fail | Fix     |
|----------------------------|---------------------------|--------|--------------|-----------|---------|
| #1 - Home/About Template   | Yes                       | Yes    | No issues    | Pass      |    -    |
| #2 - Navigation            | Yes                       | Yes    | No issues    | Pass      |    -    |
| #3 - Footer                | Yes                       | Yes    | No issues    | Pass      |    -    |
| #4 - Login Page            | Yes                       | Yes    | No issues    | Pass      |    -    |
| #5 - SignUp/Register Page  | Yes                       | Yes    | No issues    | Pass      |    -    |
| #6 - Profile SetUp         | Yes                       | Yes    | No issues    | Pass      |    -    |
| #7 - Make a Booking Page   | Yes                       | Yes    | No issues    | Pass      |    -    |
| #8 - Create a Booking Page | Yes                       | Yes    | No issues    | Pass      |    -    |
| #9 - Visit Us Page         | Yes                       | Yes    | No issues    | Pass      |    -    |
| #10 - Logout Page          | Yes                       | Yes    | No issues    | Pass      |    -    |
| #11 - Booking Confirmation Email | Feature not included in this version - 'Should Have' item | | | | |
| #12 - Edit User Profile    | Yes                       | Yes    | No issues    | Pass      |    -    |
| #13 - Delete User Profile  | Feature left in backlog as currently unnecessary, User can delete individual items and Admin can delete complete account, future version will include delete account | | | | |
| #14 - Edit Booking         | Yes                       | Yes    | No issues    | Pass      |    -    |
| #15 - Delete Booking       | Yes                       | Yes    | No issues    | Pass      |    -    |
| #16 - Error Pages          | Yes                       | Yes    | No issues    | Pass      |    -    |
| #17 - Articles             | Yes                       | Yes    | No issues    | Pass      |    -    |
| #18 - Site Pagination      | Yes                       | Yes    | No issues    | Pass      |    -    |
| #19 - View Likes           | Yes                       | Yes    | No issues    | Pass      |    -    |
| #20 - View Articles        | Yes                       | Yes    | No issues    | Pass      |    -    |
| #21 - Open Article         | Yes                       | Yes    | No issues    | Pass      |    -    |
| #22 - Like/Unlike Article  | Yes                       | Yes    | No issues    | Pass      |    -    |
| #23 - Comment on a Post    | Yes                       | Yes    | No issues    | Pass      |    -    |
| #24 - Gallery Page         | Yes                       | Yes    | No issues    | Pass      |    -    |
| #24(mistake-allocated #24 twice) | Alert Messages | Yes   | No issues    | Pass      |    -    |
| #25 - Create Article       | Yes                       | Yes    | No issues    | Pass      |    -    |
| #26 - Delete Article       | Yes                       | Yes    | No issues    | Pass      |    -    |
| #27 - Edit Article         | Yes                       | Yes    | No issues    | Pass      |    -    |
| #28 - Search Function      | Yes                       | Yes    | No issues    | Pass      |    -    |
| #29 - Delete Comment       | Yes                       | Yes    | No issues    | Pass      |    -    |
| #30 - User Feedback for max Booking Allowance | Yes                       | Yes    | No issues    | Pass      |    -    |
| #31 - Upload Image to Gallery Wall | Yes                       | Yes    | No issues    | Pass      |    -    |
| #32 - Add Review           | Feature not included in this version - 'Could Have' item | | | | |
| #33 - Edit Review          | Feature not included in this version - 'Could Have' item | | | | |
| #34 - Delete Review        | Feature not included in this version - 'Could Have' item | | | | |
| #35 - Delete Photo         | Yes                       | Yes    | No issues    | Pass      |    -    | -->

<hr>
  
### Dev Tools/Real World Device Testing

<!-- Responsiveness testing was carried out using Google Dev Tools on the devices detailed within the below table. Responsiveness was evident on all features throughout all tested devices. Occassionally I would have to refresh the page by clicking the 'FreeFido' logo as the page would load zoomed in or out on the simualted device. When refreshed and CSS checked the desired outcome was observed. I put this down to a caching issue in Chrome as this issue was not observed when testing on the available real world devices. -->
  

**Dev Tools Device Testing - all features tested, issues noted below**
Tested with responsive dimensions and no issues.
   
  
**Real World Device Testing**
| Device      | Feature    | Issue  | Fix  | 
| ------------| ---------- | ------ |------|
| iPhone 15| All features |  No issues  | None needed |
| iPhone 13 mini  | All features | No issues | None needed |
| iPad Air 2022 |    All features      |    No issues    |  None needed |
| MacBook Air M3 2024| All features | No issues | None needed |


## Bugs  
  
As a newcomer to Django and database development, I faced numerous challenges typical of first-time projects. The following bugs were particularly complex, requiring extensive troubleshooting and occasional guidance from support resources.

| No. | Bug | Solved | Fix | Solution Credit | Commit no. |
| --- | ---------------- | ---- | ------------- | -------------- | ------------|
| 1   | Unable to deploy to Heroku | Yes | Procfile set up incorrect - missing "web:" and removed a trailing backslash from a url in allowed hosts | Me! I Found it! Win! | a9f523b and e9057d4 |
| 2   | CSS not showing in development or deployed site | Yes | Debug was set to False for deployment - swaped back to True and everything worked. | A wild Amy appeared in Coding Coach| none |
| 3  | Migrations not migrating | Yes | In the book model I changed "book" to "book_title" | Me! I fixed it! Another Win!| 6c98937 |
| 4 | When editing a comment, form forces you to select a rating again. This appears in the comment as a double rating | Yes | the javascript was fetching all of the innter conent of the element with the ID of comment{{ comment.id }} and I needed to move the review content outside of this div | The Wonderful Coding Wizard Ruu at Coding Coach| e3a0f90 |


### Known Bugs

