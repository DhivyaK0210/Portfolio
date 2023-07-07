/*===== MENU SHOW =====*/ 
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show')
        })
    }
}
showMenu('nav-toggle','nav-menu')

/*===== REMOVE MENU MOBILE =====*/
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*===== SCROLL SECTIONS ACTIVE LINK =====*/
const sections = document.querySelectorAll('section[id]')

window.addEventListener('scroll', scrollActive)

function scrollActive(){
    const scrollY = window.pageYOffset

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50;
        sectionId = current.getAttribute('id')

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active')
        }else{
            document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active')
        }
    })
}

/*===== SCROLL REVEAL ANIMATION =====*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 2000,
    reset: true
})

/*SCROLL RESUME*/
sr.reveal('.resume__img', {delay: 500})
sr.reveal('.resume__subtitle', {delay: 300})
sr.reveal('.resume__profession', {delay: 400})
sr.reveal('.resume__text', {delay: 500})

/*SCROLL EDUCATION*/
sr.reveal('.edu__img', {delay: 500})
sr.reveal('.edu__subtitle', {delay: 300})
sr.reveal('.edu__profession', {delay: 400})
sr.reveal('.edu__text', {delay: 500})

/*SCROLL ACHIEVEMENTS*/
sr.reveal('.ach__img', {delay: 500})
sr.reveal('.ach__subtitle', {delay: 300})
sr.reveal('.ach__profession', {delay: 400})
sr.reveal('.ach__text', {delay: 500})

/*SCROLL PROJECTS*/
sr.reveal('.pro__img', {delay: 500})
sr.reveal('.pro__subtitle', {delay: 300})
sr.reveal('.pro__profession', {delay: 400})
sr.reveal('.pro__text', {delay: 500})

/*SCROLL PERSONL DETAILS*/
sr.reveal('.pd__img', {delay: 500})
sr.reveal('.pd__subtitle', {delay: 300})
sr.reveal('.pd__profession', {delay: 400})
sr.reveal('.pd__text', {delay: 500})

/*SCROLL HOBBIES*/
sr.reveal('.hob__img', {delay: 500})
sr.reveal('.hob__subtitle', {delay: 300})
sr.reveal('.hob__profession', {delay: 400})
sr.reveal('.hob__text', {delay: 500})







