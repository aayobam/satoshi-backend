//Owl Carousel JS control

//Navbar Toggling
function classToggle() {
  const navs = document.querySelectorAll('.navbar__Items');
    
  navs.forEach(nav => nav.classList.toggle('navbar__ToggleShow'));
}
  
document.querySelector('.navbar__Link-toggle').addEventListener('click', classToggle);


// //like toggle function
// const likeBtn = document.querySelector('.like-btn');
// const likeIcon = document.querySelector('.ri-heart-line');
// const likeNumber = document.querySelector('.action-number__like');


// likeBtn.addEventListener('click', function(){
//   likeIcon.classList.toggle("ri-heart-line");
//   likeIcon.classList.add("ri-heart-fill");
// })


/*======share button function========*/
const shareBtn = document.querySelector(".share-btn");
const socialLinks = document.querySelector('.social-sharing');

socialLinks.classList.add('hidden');

shareBtn.addEventListener("click", function () {
  // console.log("button clicked");
  socialLinks.classList.toggle("hidden");
});