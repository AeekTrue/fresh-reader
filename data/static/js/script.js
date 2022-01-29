let y = 0;

const local_links = document.getElementsByClassName("local-link")
for (let i = 0; i < local_links.length; i++) {
    local_links[i].setAttribute('onclick', 'y = getScrollPos()');
}

function getScrollPos() {
    const back_btn = document.getElementById("back-button");
    back_btn.style.display = 'block';
    return window.scrollY;
}

function goToScrollPos() {
    const back_btn = document.getElementById("back-button");
    back_btn.style.display = 'none';
    window.scrollTo(0, y);
}