function showMore() {
    var showMoreOptionElem = document.getElementsByClassName('know-more-option')[0];

    showMoreOptionElem.style.opacity = "0";
    showMoreOptionElem.style.transition = "opacity 0.5s ease-in-out";
}

function showLess() {
    console.log('hit')
    var showMoreOptionElem = document.getElementsByClassName('know-more-option')[0];
    showMoreOptionElem.style.opacity = "1";
}


function addActiveClass(navBtn) {
    var navBtn = document.getElementById(navBtn);
    navBtn.style.color = "#926402";
}


// lightbox
// Open the Modal
function openModal() {
    document.getElementById("myModal").style.display = "block";
}
//
// // Close the Modal
function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    var captionText = document.getElementById("caption");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
    captionText.innerHTML = dots[slideIndex - 1].alt;
}

