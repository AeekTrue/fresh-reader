var y = 0;
function saveScrollPos() {
    var back_btn = document.getElementById("back-button")
    back_btn.style.display = 'block';
    return window.scrollY;
}

function goToScrollPos() {
    var back_btn = document.getElementById("back-button")
    back_btn.style.display = 'none';
    window.scrollTo(0, y);
}