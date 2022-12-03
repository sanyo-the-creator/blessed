var contactbtn=document.getElementById("contact-btn")
contactbtn.addEventListener('click', () => {
    window.scrollTo(0,document.body.scrollHeight); });



function imageView() {
    document.querySelector('.view').style.left = '50%';
    document.querySelector('.view').style.transform = 'translateX(-50%)';
    document.querySelector('.row, .row-1, .navcontainer').style.opacity = '50%';
}

function cancel() {
    document.querySelector('.view').style.left = '-100%';
    document.querySelector('.row, .row-1, .navcontainer').style.opacity = '0';
}