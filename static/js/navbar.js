const menu_btn = document.querySelector('.hamburger');
const mobile_menu = document.querySelector('.mobile-nav');

menu_btn.addEventListener('click', function () {
    menu_btn.classList.toggle('is-active');
    mobile_menu.classList.toggle('is-active');
})

document.addEventListener('click', function(e) { 
    console.log(e) 
    if ( e.target!=link && link) { 
        popup.style.display = "none" 
    } 
})

function search() {
    document.querySelector('.m-search').style.left = '50%';
    document.querySelector('.m-search').style.transform = 'translateX(-50%)';
    document.querySelector('.search-mobile').style.display = 'none';
    document.querySelector('.cancel').style.display = 'block'
}

function cancel() {
    document.querySelector('.m-search').style.top = '50%';
    document.querySelector('.search-mobile').style.display = 'block';
    document.querySelector('.cancel').style.display = 'none'
}