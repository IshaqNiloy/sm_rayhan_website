function showMore() {
    var hiddenPartElem = document.getElementsByClassName('hidden-part')[0];
    var showMoreOptionElem = document.getElementsByClassName('know-more-option')[0];
    
    hiddenPartElem.style.display = "block";
    showMoreOptionElem.style.display = "none";
}

function showLess() {
    var hiddenPartElem = document.getElementsByClassName('hidden-part')[0];
    var showMoreOptionElem = document.getElementsByClassName('know-more-option')[0];
    
    hiddenPartElem.style.display = "none";
    showMoreOptionElem.style.display = "block";
}