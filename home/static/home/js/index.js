function showMore() {
    var showMoreOptionElem = document.getElementsByClassName('know-more-option')[0];
    
    showMoreOptionElem.style.opacity = "0";
    showMoreOptionElem.style.transition = "opacity 0.5s ease-in-out";
}

function showLess() {
    var showMoreOptionElem = document.getElementsByClassName('know-more-option')[0];
    
    showMoreOptionElem.style.opacity = "1";
}


function addActiveClass(navBtn){
    var navBtn = document.getElementById(navBtn);
    navBtn.style.color = "#926402";
}